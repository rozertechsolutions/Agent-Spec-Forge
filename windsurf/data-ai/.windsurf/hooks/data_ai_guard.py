#!/usr/bin/env python3
import json
import re
import shlex
import sys


BLOCKED_COMMAND_PATTERNS = [
    r"(?i)\brm\s+-[^\n]*[rf]",
    r"(?i)\bsudo\b",
    r"(?i)\bchmod\s+(-R\s+)?777\b",
    r"(?i)\b(chown|mkfs|diskutil|dd)\b",
    r"(?i)\bgit\s+(reset|clean|checkout|restore|push|pull|merge|rebase|branch|switch|commit|tag|stash)\b",
    r"(?i)\b(npm|pnpm|yarn|bun|pip|uv|poetry|conda|brew)\b.*\b(install|add|update|upgrade|sync)\b",
    r"(?i)\b(curl|wget|scp|rsync|aws|az|gcloud|kubectl|terraform|tofu|pulumi|docker)\b",
    r"(?i)\b(deploy|publish|release|submit|sign|notary|upload|production)\b",
    r"(?i)\b(model\s+download|huggingface-cli|ollama\s+pull|mlflow|wandb|dvc\s+push)\b",
]

SHELL_OPERATOR_RE = re.compile(r"(\|\||&&|;|\||`|\$\(|<\(|>|>>|<<)")
SECRET_SHAPE_RE = re.compile(
    r"(?i)(api[_-]?key|access[_-]?token|secret|password|private[_-]?key|"
    r"BEGIN (RSA|OPENSSH|PRIVATE)|sk-[A-Za-z0-9]{20,})"
)
PROTECTED_PATH_RE = re.compile(
    r"(?i)(^|/)(\.env|\.git|id_rsa|id_ed25519|credentials|secrets?)(/|$)|"
    r"\.(pem|key|p12|pfx)$"
)
UNSAFE_PROMPT_RE = re.compile(
    r"(?i)(ignore previous|bypass|disable.+(guard|hook|permission)|exfiltrate|"
    r"dump.+(dataset|secret|credential)|production.+(deploy|delete|publish)|"
    r"train.+on.+personal data)"
)


def block(message):
    print(f"data_ai_guard: {message}", file=sys.stderr)
    sys.exit(2)


def event_name(data):
    return str(data.get("agent_action_name") or data.get("hook_event_name") or "")


def text_fields(value):
    if isinstance(value, dict):
        for key, item in value.items():
            if isinstance(item, (dict, list)):
                yield from text_fields(item)
            elif item is not None:
                yield str(item)
    elif isinstance(value, list):
        for item in value:
            yield from text_fields(item)
    elif value is not None:
        yield str(value)


def command_line(data):
    tool_info = data.get("tool_info") or {}
    tool_input = data.get("tool_input") or {}
    return str(
        tool_info.get("command_line")
        or tool_info.get("command")
        or tool_input.get("command")
        or ""
    )


def changed_path(data):
    tool_info = data.get("tool_info") or {}
    tool_input = data.get("tool_input") or {}
    return str(
        tool_info.get("path")
        or tool_info.get("file_path")
        or tool_input.get("path")
        or tool_input.get("file_path")
        or ""
    )


def check_all_text(data):
    for item in text_fields(data):
        if "\x00" in item:
            block("blocked null byte in hook input")
        if SECRET_SHAPE_RE.search(item):
            block("blocked secret-shaped or credential-related input")


def check_command(data):
    command = command_line(data)
    if not command.strip():
        block("missing command line")
    if SHELL_OPERATOR_RE.search(command):
        block("blocked shell chaining, pipe, redirection, or substitution")
    try:
        tokens = shlex.split(command, posix=True)
    except ValueError as exc:
        block(f"malformed command quoting: {exc}")
    if not tokens:
        block("missing command tokens")
    for pattern in BLOCKED_COMMAND_PATTERNS:
        if re.search(pattern, command):
            block("blocked command requiring explicit human approval")


def check_write(data):
    path = changed_path(data)
    if path and PROTECTED_PATH_RE.search(path):
        block("blocked write to protected or credential-like path")


def check_prompt(data):
    prompt_text = "\n".join(text_fields(data))
    if UNSAFE_PROMPT_RE.search(prompt_text):
        block("blocked unsafe prompt request for Data and AI work")


def main():
    try:
        data = json.loads(sys.stdin.read() or "{}")
    except json.JSONDecodeError as exc:
        block(f"malformed hook JSON: {exc}")

    check_all_text(data)
    event = event_name(data)
    if event == "pre_run_command":
        check_command(data)
    elif event == "pre_write_code":
        check_write(data)
    elif event == "pre_mcp_tool_use":
        block("MCP tool use is disabled by default for Data and AI")
    elif event == "pre_user_prompt":
        check_prompt(data)


if __name__ == "__main__":
    main()
