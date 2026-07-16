from web_development_department.policy import requires_human_approval


def test_sensitive_actions_require_approval() -> None:
    assert requires_human_approval("deployment")
    assert requires_human_approval("secret_access")
    assert requires_human_approval("git_mutation")


def test_read_only_analysis_is_not_automatically_sensitive() -> None:
    assert not requires_human_approval("read_workspace")
