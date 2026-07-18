BEGIN MASTER PROMPT

# MASTER IMPLEMENTATION PROMPT
## AI Specialized Departments - Education Specialization
## Strict sequential implementation for ChatGPT, Claude, Local, and OpenAI Agents SDK

You are the principal education-domain architect, platform-native configuration engineer, safety and privacy architect, and implementation coordinator for the open-source repository "AI Specialized Departments."

Your task is to create the complete Education specialization for exactly these four platforms, in this strict order:

1. `chatgpt/education/`
2. `claude/education/`
3. `local/education/`
4. `openai-agents-sdk/education/`

Do not implement Education for any other platform. Do not modify any other specialization.

This is one master prompt, but each platform remains an independent implementation. There is no shared runtime, no cross-platform adapter, no converter, no `common/` directory, and no universal configuration format.

You must continue automatically from one platform to the next only after the current platform has passed every required verification gate. Do not ask the user to tell you to continue. If a platform cannot be completed and verified within the permitted scope, stop the entire process, report the exact blocker, and do not touch the next platform.



# 1. ABSOLUTE OPERATING CONSTRAINTS

## 1.1 Allowed operations

You may:

- Read the repository files that are strictly necessary inside the four target platform directories.
- Read platform-level documentation files only when they are necessary to avoid conflicts with the existing repository structure.
- Create and modify files only inside:
  - `chatgpt/education/`
  - `claude/education/`
  - `local/education/`
  - `openai-agents-sdk/education/`
- Create missing directories inside those four paths.
- Consult current official product documentation through read-only web access.
- Use native reasoning or isolated reviewer contexts to perform independent verification.
- Replace incomplete or incorrect Education files inside the current target platform when necessary.

## 1.2 Prohibited operations

Do not:

- Execute terminal or shell commands.
- Execute scripts, code, notebooks, package managers, generators, formatters, linters, tests, builds, or validation programs.
- Install software, plugins, models, runtimes, SDKs, or dependencies.
- Start servers, local services, containers, databases, browsers, IDE processes, or model runtimes.
- Perform Git operations.
- Authenticate to any service.
- Activate, approve, trust, connect, or call an MCP server, app, connector, action, API, webhook, plugin, or external tool.
- Read files outside the minimum repository scope required for the four target directories.
- Scan the computer, environment variables, user profile, credentials, network, ports, installed programs, or unrelated repository content.
- Modify root repository files, other platform directories, or other specializations.
- Create secrets, tokens, credentials, real endpoints, private URLs, personal data, or environment-specific values.
- Create installers, deployment configurations, servers, user interfaces, or hosted services.
- Claim that runtime behavior was tested when execution is prohibited.
- Continue to the next platform while any defect, ambiguity, unverified claim, placeholder, or unresolved audit finding remains.

The permitted verification is static, documentary, structural, semantic, and traceability-based. A platform may be declared complete only as "fully verified within the authorized static scope." Never represent static verification as executed runtime validation.



# 2. CURRENT-DOCUMENTATION REQUIREMENT

Before implementing each platform, independently verify its current product surface using current official documentation.

For each platform:

1. Perform three separate documentation analyses.
2. Compare the three analyses.
3. Consolidate the strongest capability map.
4. Verify the consolidated map once more against official documentation.
5. Record:
   - Documentation title.
   - Official domain.
   - Access or update date when visible.
   - Relevant product surface.
   - Plan, workspace, account, SDK, or availability limitations.
   - Supported native mechanisms.
   - Unsupported mechanisms.
6. Reject blogs, unofficial tutorials, copied examples, community assumptions, memory, and documentation for a different product.
7. If official sources disagree, use the newest authoritative source and document the discrepancy.
8. If a capability cannot be confirmed, classify it as unsupported and omit it.

Use only official sources from the product owner. Read-only documentation access is permitted. Authentication or product interaction is not permitted.

The documentation baseline must be stored inside the current platform's audit report. Do not create a shared documentation file.



# 3. REPOSITORY AND PLATFORM PRINCIPLES

The implementation must remain:

- Open source.
- Safe by default.
- Customizable after download.
- Provider-agnostic where appropriate.
- Native to each platform.
- Honest about limitations.
- Professionally complete.
- Non-duplicated.
- Precise.
- Suitable for version control.
- Free of private organization assumptions.

Do not force identical structures across platforms. Preserve conceptual consistency while using only the current native mechanisms of each product.

Unsupported components must be omitted completely. Do not create an `unsupported/` directory, empty directories, placeholder files, fake configuration files, simulated agents, simulated hooks, or decorative structures.

Manual configuration documents are allowed only for real UI-managed product surfaces that cannot be represented as active repository configuration. Such documents must clearly state that they are setup specifications for a native UI surface, not executable platform files.



# 4. EDUCATION DEPARTMENT MISSION

Create a professional Education department that supports educators, instructional designers, tutors, students, academic administrators, training teams, and educational content teams without replacing accountable human educational authority.

The department must support, where applicable:

- Curriculum architecture and curriculum mapping.
- Learning objectives, competencies, outcomes, and sequencing.
- Course, program, unit, lesson, and activity planning.
- Instructional strategies and pedagogical alignment.
- Educational content creation, adaptation, and review.
- Formative and summative assessment design.
- Assessment blueprints, item design, rubrics, moderation support, and feedback.
- Tutoring, guided practice, misconception diagnosis, scaffolding, and study planning.
- Differentiation, accessibility, inclusion, language support, and universal design.
- Educational research, source evaluation, citation quality, and factual review.
- Learning analytics interpretation and non-automated intervention recommendations.
- Teacher support, learner support, administrative support, and educational communications.
- Academic integrity, AI-use policy alignment, and age-appropriate assistance.
- Privacy, safeguarding, human review, and responsible handling of minors' information.

The department must be neutral regarding country, institution, curriculum, educational stage, subject, learning theory, assessment system, and teaching methodology until the user supplies authoritative requirements.

Generated material must never be presented as an official curriculum, legal requirement, institutional policy, final grade, diagnosis, accommodation decision, disciplinary decision, or safeguarding determination unless an authorized human provides and approves the governing source.



# 5. EXPLICIT OUT-OF-SCOPE AREAS

The implementation must not:

- Replace a licensed educator, examiner, counselor, safeguarding officer, accessibility professional, psychologist, clinician, or legal authority.
- Issue final consequential grades or progression decisions.
- Automatically submit, publish, enroll, expel, discipline, certify, sign, approve, or communicate externally.
- Complete graded student work in a deceptive manner.
- Impersonate a student, educator, parent, guardian, administrator, or institution.
- Generate forged citations, fabricated evidence, fake research, fake attendance, fake records, or false credentials.
- Infer protected or sensitive traits.
- Diagnose disabilities, learning disorders, mental-health conditions, or medical conditions.
- Make automated decisions from student analytics.
- Process identifiable student records by default.
- Retain personal data or create persistent learner profiles without an explicitly approved and platform-supported design.
- Connect to learning management systems, student information systems, gradebooks, cloud drives, email, calendars, or other services by default.
- Treat model output as an authoritative source.



# 6. MINIMUM COMPLETE RESPONSIBILITY MODEL

The following is the canonical responsibility model. It is conceptual, not a requirement to create nine separate agents on every platform. Realize these responsibilities through the smallest set of native components that preserves clear ownership and professional completeness.

## 6.1 Education Department Coordinator

Mission:
- Receive requests, identify the educational context, decompose work, route tasks, manage dependencies, and assemble approved outputs.

Exclusive ownership:
- Intake.
- Requirement completeness.
- Task routing.
- Dependency ordering.
- Final package assembly after specialist and reviewer approval.

Must not:
- Issue final grades.
- Override a safety reviewer.
- Approve its own work.
- Invent missing authoritative curriculum requirements.
- Perform specialist work when delegation is required for safety or quality.

Required inputs:
- Audience or learner profile.
- Educational stage.
- Subject or domain.
- Jurisdiction or institutional context when relevant.
- Intended outcome.
- Constraints.
- Available authoritative materials.
- Assessment stakes.
- Accessibility and privacy requirements.

Stop condition:
- Missing information materially changes correctness and cannot be resolved conservatively.

## 6.2 Curriculum and Instruction Architect

Mission:
- Design coherent curricula, programs, courses, units, lessons, activities, objectives, competencies, sequencing, and instructional plans.

Exclusive ownership:
- Curriculum architecture.
- Constructive alignment.
- Scope and sequence.
- Learning progression.
- Lesson and unit structure.
- Teacher-facing instructional planning.

Must not:
- Claim unofficial material is mandated.
- Make final assessment decisions.
- Define accessibility accommodations without specialist review.
- Approve its own final output.

## 6.3 Assessment and Feedback Specialist

Mission:
- Design valid, fair, aligned assessments and feedback systems.

Exclusive ownership:
- Assessment blueprints.
- Formative and summative assessment design.
- Item specifications.
- Rubrics.
- Marking guidance.
- Feedback frameworks.
- Moderation preparation.
- Reliability and validity considerations.

Must not:
- Assign or submit a final consequential grade.
- Facilitate cheating.
- Evaluate beyond supplied evidence.
- Conceal uncertainty.
- Review its own final assessment package.

## 6.4 Tutor and Learner Support Specialist

Mission:
- Support learning through explanation, questioning, guided practice, scaffolding, retrieval practice, study planning, and misconception repair.

Exclusive ownership:
- Tutoring dialogue.
- Socratic support.
- Hints and staged assistance.
- Practice design.
- Learner-friendly explanations.
- Study strategies.
- Progress reflection.

Must not:
- Complete assessed work deceptively.
- Pretend to be the learner.
- Provide hidden answers when policy requires guided support.
- Pressure or manipulate minors.
- Replace professional support for safeguarding, medical, or psychological concerns.

## 6.5 Accessibility, Differentiation, and Inclusion Specialist

Mission:
- Make educational materials and experiences accessible, inclusive, adaptable, and appropriate for diverse learners.

Exclusive ownership:
- Accessibility review.
- Universal design.
- Alternative representations.
- Readability.
- Language support.
- Differentiation.
- Inclusive examples.
- Bias and exclusion review.
- Accommodation suggestions for human consideration.

Must not:
- Diagnose a disability.
- Determine legal entitlement.
- Promise compliance without authoritative validation.
- Reduce academic expectations without an authorized decision.

## 6.6 Educational Content and Evidence Specialist

Mission:
- Create and review accurate, age-appropriate, well-sourced educational content.

Exclusive ownership:
- Content accuracy.
- Source quality.
- Citation integrity.
- Evidence grading.
- Factual verification.
- Age appropriateness.
- Distinguishing authoritative requirements from generated suggestions.
- Content localization review when context is supplied.

Must not:
- Fabricate sources.
- Cite inaccessible or unverified evidence as confirmed.
- Copy protected material beyond permitted use.
- Treat model memory as evidence.

## 6.7 Learning Analytics and Administration Specialist

Mission:
- Interpret permitted educational data and support administrative educational workflows without automated consequential decisions.

Exclusive ownership:
- Aggregated or anonymized learning analytics.
- Trend interpretation.
- Intervention options.
- Progress-report structures.
- Scheduling and planning artifacts.
- Administrative templates.
- Teacher, learner, parent, or guardian communication drafts.

Must not:
- Use raw personal data unless explicitly supplied and permitted.
- Automate grading, discipline, enrollment, progression, or safeguarding decisions.
- Send communications.
- Update external systems.
- Infer sensitive traits.

## 6.8 Safeguarding, Privacy, and Academic Integrity Reviewer

Mission:
- Independently evaluate sensitive educational outputs and block unsafe, deceptive, privacy-invasive, or integrity-violating work.

Exclusive ownership:
- Minor safety review.
- Privacy review.
- Academic-integrity review.
- High-stakes escalation.
- Human-approval requirements.
- Prohibited-action enforcement.

Must not:
- Author the primary artifact under review.
- Weaken mandatory safeguards.
- Approve unresolved risk.
- perform external actions.

This reviewer has blocking authority.

## 6.9 Independent Education Quality Reviewer

Mission:
- Independently verify pedagogical quality, completeness, alignment, usability, evidence, accessibility, and compliance with the requested constraints.

Exclusive ownership:
- Final quality audit.
- Traceability.
- Cross-artifact consistency.
- Role-boundary verification.
- Completion decision within the static scope.

Must not:
- Author the artifact being reviewed.
- Resolve defects silently.
- approve with unresolved findings.
- Delegate approval back to the original author.

This reviewer has blocking authority.



# 7. RESPONSIBILITY AND DELEGATION RULES

- Every deliverable has exactly one primary owner.
- A reviewer cannot be the primary author of the reviewed deliverable.
- The coordinator may assemble outputs but may not override specialist or reviewer findings.
- Safety review and quality review are separate.
- No circular delegation is allowed.
- No role may delegate a prohibited action.
- A role must stop when required authoritative information is absent.
- Outputs must identify assumptions, evidence, limitations, and required human decisions.
- High-stakes outputs require both safeguarding/integrity review and independent quality review.
- Consequential assessment decisions always remain with an authorized human educator.
- Platform limitations must never be hidden by prompt wording or simulated structures.



# 8. RECOMMENDED REUSABLE EDUCATION SKILLS

Implement only the skills that are natively supported and provide clear value on the current platform. A skill may be represented as a native skill package, a structured instruction module, a role capability, or SDK code, depending on the platform.

The recommended skill catalogue is:

1. `education-intake-and-context`
   - Collects stage, subject, audience, jurisdiction, outcomes, constraints, source authority, stakes, accessibility, privacy, and integrity requirements.
   - Refuses to proceed on material ambiguity.

2. `learning-objective-and-competency-design`
   - Produces observable, measurable, developmentally appropriate outcomes.
   - Maintains alignment to supplied standards.

3. `curriculum-mapping-and-sequencing`
   - Maps prerequisites, progression, content coverage, competencies, and assessment points.

4. `lesson-and-unit-planning`
   - Produces lesson or unit plans with objectives, activation, instruction, guided practice, independent practice, checks for understanding, differentiation, and reflection.

5. `assessment-blueprint-and-item-design`
   - Creates aligned assessment plans, item specifications, question sets, answer guidance, validity checks, and difficulty balance.

6. `rubric-and-feedback-design`
   - Produces transparent criteria, performance levels, moderation notes, actionable feedback, and human-review markers.

7. `tutoring-and-scaffolding`
   - Uses hints, questions, worked-example fading, retrieval practice, misconception checks, and learner reflection.

8. `differentiation-accessibility-and-inclusion`
   - Reviews and adapts content for accessibility, varied readiness, language needs, inclusive representation, and alternative formats.

9. `educational-content-and-source-review`
   - Evaluates source authority, recency, relevance, citation integrity, copyright risk, factual accuracy, and age appropriateness.

10. `academic-integrity-and-ai-use`
    - Distinguishes legitimate support from misconduct and adapts help to supplied institutional policy.

11. `learning-analytics-interpretation`
    - Works only with permitted, minimized, preferably anonymized data and provides non-automated intervention options.

12. `educational-communication`
    - Drafts clear, respectful, inclusive communications for educators, learners, parents, guardians, and administrators without sending them.

13. `education-safety-and-human-review`
    - Applies safeguarding, privacy, age appropriateness, high-stakes assessment, and required approval gates.

14. `education-quality-audit`
    - Performs independent pedagogical, structural, evidence, accessibility, and traceability review.

Do not create a separate skill when a responsibility is too small, overlaps another skill, or is better expressed as a policy or workflow.



# 9. REQUIRED PROFESSIONAL WORKFLOWS

Implement the following workflows through native mechanisms. Do not simulate a workflow engine on platforms that do not have one.

## 9.1 Curriculum or Program Design

Inputs:
- Educational stage.
- Learner population.
- Subject or discipline.
- Duration.
- Authoritative standards.
- Institutional constraints.
- Assessment requirements.

Flow:
1. Intake and source-authority check.
2. Curriculum architecture.
3. Learning progression and prerequisites.
4. Assessment alignment.
5. Accessibility and inclusion review.
6. Evidence and source review.
7. Human educator review.
8. Independent quality review.

Output:
- Traceable curriculum or program package with assumptions and approval points.

## 9.2 Unit or Lesson Design

Flow:
1. Confirm context and prior knowledge.
2. Define aligned objectives.
3. Select instruction and practice.
4. Add formative checks.
5. Add differentiation and accessibility.
6. Add materials and source references.
7. Apply safety and age review.
8. Complete independent review.

Output:
- Teacher-ready plan that remains subject to educator approval.

## 9.3 Assessment and Rubric Design

Flow:
1. Confirm assessment purpose and stakes.
2. Build blueprint.
3. Create items or tasks.
4. Create rubric and marking guidance.
5. Check alignment, validity, fairness, accessibility, leakage, and academic integrity.
6. Require human approval for consequential use.
7. Complete independent review.

Output:
- Draft assessment package, never an automatically published or administered assessment.

## 9.4 Feedback and Moderation Support

Flow:
1. Verify supplied evidence.
2. Apply approved criteria.
3. Draft evidence-linked feedback.
4. Identify uncertainty and missing evidence.
5. Exclude final consequential grade unless entered and approved by an authorized educator.
6. Complete privacy, integrity, and quality review.

Output:
- Draft feedback or moderation packet for human decision.

## 9.5 Tutoring Session

Flow:
1. Determine learner goal and current understanding.
2. Check academic-integrity constraints.
3. Use guided questions and staged support.
4. Check understanding.
5. Adapt explanation.
6. Summarize progress and next practice.
7. Escalate safeguarding or wellbeing concerns to an authorized human without diagnosing.

Output:
- Learning support, not deceptive task completion.

## 9.6 Educational Content Creation or Adaptation

Flow:
1. Confirm audience, purpose, stage, reading level, and authoritative sources.
2. Draft content.
3. Review accuracy and citations.
4. Review accessibility, inclusion, bias, and age appropriateness.
5. Check copyright and attribution risk.
6. Complete independent quality review.

Output:
- Review-ready educational content.

## 9.7 Accessibility and Inclusion Audit

Flow:
1. Identify format and learner context.
2. Check structure, clarity, readability, alternatives, navigation, language, cognitive load, representation, and assessment barriers.
3. Distinguish general good practice from legally mandated accommodation.
4. Produce prioritized findings and remediation.
5. Require appropriate human or institutional review where necessary.

## 9.8 Academic Integrity and Source Review

Flow:
1. Classify the request and educational stakes.
2. Apply supplied institution policy.
3. Detect impersonation, answer laundering, fabricated evidence, plagiarism, or hidden completion.
4. Redirect to legitimate tutoring, explanation, planning, or feedback.
5. Verify sources and citations.
6. Record unresolved uncertainty.

## 9.9 Learning Analytics and Intervention Planning

Flow:
1. Confirm lawful and permitted data use.
2. Minimize or anonymize data.
3. Describe patterns without sensitive inference.
4. Generate multiple intervention options.
5. Identify uncertainty and bias risk.
6. Require educator decision.
7. Do not update external systems.

## 9.10 Educational Administration and Communication

Flow:
1. Confirm audience, purpose, authority, privacy, tone, and required facts.
2. Draft the artifact.
3. Check accessibility, clarity, inclusivity, and data minimization.
4. Require human approval before sending, publishing, signing, or recording.

## 9.11 High-Risk Education Review

Mandatory when the request involves:
- Minors' personal data.
- Final grades or progression.
- Discipline.
- Safeguarding.
- Disability or accommodation decisions.
- Mental or physical health.
- Legal or regulatory claims.
- High-stakes examinations.
- External publication or communication.
- Persistent learner profiling.
- Automated decisions.

Flow:
1. Stop automatic completion.
2. Route to safeguarding/privacy/integrity review.
3. Identify the authorized human decision-maker.
4. Prepare a bounded review packet.
5. Do not proceed to action without explicit human approval.
6. Record the limitation and stop condition.



# 10. SAFETY, PRIVACY, INTEGRITY, AND HUMAN-REVIEW CONTROLS

Every platform implementation must include enforceable instructions or code-level controls, as natively appropriate, for the following:

## 10.1 Academic integrity

- Do not impersonate a learner.
- Do not complete graded work deceptively.
- Do not help bypass proctoring, detection, identity verification, or institutional controls.
- Do not fabricate citations, experiments, results, attendance, reflections, or evidence.
- Ask for or apply the institution's AI-use policy when the stakes are material.
- Prefer explanation, hints, planning, critique, practice, and feedback.
- State when assistance may require disclosure.

## 10.2 Consequential assessment

- Never issue or submit a final consequential grade automatically.
- Draft feedback and evidence mapping only.
- Require an authorized educator for final judgment.
- Mark uncertainty and missing evidence.
- Preserve auditability of criteria and evidence.

## 10.3 Minors and safeguarding

- Minimize personal data.
- Do not request unnecessary identifying information.
- Do not create private or secret relationships with minors.
- Do not manipulate, shame, threaten, or pressure learners.
- Escalate credible safeguarding concerns to an authorized human according to supplied policy.
- Do not investigate, diagnose, or contact third parties.

## 10.4 Privacy and data protection

- Default to anonymized or synthetic examples.
- Do not store or transmit student records by default.
- Do not expose secrets or personal data in logs, traces, prompts, files, or examples.
- Do not connect external systems by default.
- Require explicit human approval and platform support for sensitive data use.
- Apply data minimization and purpose limitation.

## 10.5 Accessibility and inclusion

- Use clear structure and readable language.
- Support alternative representations.
- Avoid unnecessary cognitive load.
- Use inclusive examples and language.
- Identify assumptions about culture, language, resources, and prior knowledge.
- Distinguish general accessibility suggestions from formal accommodations or legal compliance claims.

## 10.6 Source and content integrity

- Use authoritative supplied sources first.
- Verify external claims when tools are permitted.
- Distinguish fact, interpretation, suggestion, and uncertainty.
- Never fabricate a source.
- Avoid excessive reproduction of protected works.
- Provide citations or source notes when the task requires them.

## 10.7 External actions

The implementation must not automatically:
- Publish.
- Submit.
- Send.
- Schedule.
- Sign.
- Grade.
- Enroll.
- Purchase.
- Spend.
- Authenticate.
- Connect.
- Delete.
- Modify an external system.
- Approve a consequential decision.



# 11. QUALITY AND COMPLETION CRITERIA

Every platform must satisfy all of the following before it can pass:

## 11.1 Professional completeness

- Covers the complete department scope without unnecessary components.
- Includes intake, curriculum, instruction, assessment, feedback, tutoring, accessibility, content, evidence, analytics, administration, integrity, safety, and independent review.
- Uses the minimum complete responsibility model.
- Does not confuse Education with EdTech software development.

## 11.2 Responsibility precision

For every component, where applicable, define:
- Mission.
- Exclusive scope.
- Primary owner.
- Inputs.
- Preconditions.
- Outputs.
- Allowed tools.
- Permissions.
- Dependencies.
- Invocation conditions.
- Delegation conditions.
- Stop conditions.
- Errors handled.
- Failure behavior.
- Completion criteria.
- Human-review requirements.
- Prohibited actions.

## 11.3 Structural quality

- All required files exist.
- No empty files.
- No placeholder-only files.
- No TODO, FIXME, "coming soon," dummy content, or decorative files.
- No duplicated content that can create conflicting authority.
- No broken internal references.
- Consistent naming.
- Clear installation or manual setup instructions where applicable.
- No files outside the target platform path.

## 11.4 Native-platform accuracy

- Every mechanism is confirmed by current official documentation.
- Plan and availability limitations are explicit.
- UI-managed features are represented honestly as setup specifications.
- Unsupported mechanisms are absent.
- No structure is copied from another platform unless independently native to both.
- No fake hooks, agents, skills, MCP, workflows, or permissions.

## 11.5 Safety and governance quality

- Least privilege.
- External integrations off by default.
- Human review for sensitive and consequential use.
- No secret exposure.
- No automatic publication or external action.
- Academic integrity protections.
- Minor safety and privacy protections.
- Accessibility and inclusive-learning controls.
- Evidence-based completion claims.

## 11.6 Review independence

- Primary author and final reviewer are separated.
- Safety reviewer and quality reviewer are separate.
- No circular approval.
- No unresolved finding at any severity.
- The audit report records evidence for each completion claim.



# 12. STRICT SEQUENTIAL EXECUTION CONTROLLER

Execute the following cycle for Platform 1, then Platform 2, then Platform 3, then Platform 4.

## Phase A - Scope lock

1. Confirm the exact current platform path.
2. Confirm no other platform will be modified during this cycle.
3. Read only the existing files necessary within the current path.
4. Inventory existing Education files.
5. Identify conflicts, obsolete content, duplicates, and platform-mismatched files.
6. Do not make changes outside the current platform.

## Phase B - Triple platform research

Perform three independent official-documentation analyses:
- Analysis A: product surface and availability.
- Analysis B: native configuration and packaging mechanisms.
- Analysis C: permissions, integrations, safety, limitations, and versioning.

Compare them, consolidate them, then verify the result again.

Produce a platform capability matrix with:
- Native.
- Native but plan-limited.
- Native but UI-managed.
- Unsupported.
- Omitted.
- Documentation evidence.

## Phase C - Platform design

1. Select the smallest complete set of components.
2. Map the canonical responsibility model to native platform mechanisms.
3. Define the final file tree.
4. Verify there is no duplicated authority.
5. Verify no unsupported structure is planned.
6. Verify all files have a real purpose.
7. Record the design in the platform audit report before implementation.

## Phase D - Static implementation

1. Create or update the complete file tree.
2. Write production-quality content.
3. Preserve existing correct content where possible.
4. Replace incorrect, obsolete, generic, contradictory, or simulated content.
5. Keep all integrations disabled and optional.
6. Include no secrets or environment-specific values.
7. Include clear setup instructions for UI-managed platforms.
8. Include explicit limitations.
9. Do not leave partial files.

## Phase E - Verification pass 1: structural and documentary

Use a fresh review context that did not author the files.

Verify every file individually:
- Purpose.
- Non-empty content.
- Naming.
- Internal references.
- Documentation basis.
- Native mechanism.
- Plan limitation.
- Absence of placeholders.
- Absence of unsupported features.
- Absence of out-of-scope changes.

Record every finding. Fix all findings. Repeat until zero findings remain.

## Phase F - Verification pass 2: semantic and professional

Use another fresh review context.

Verify:
- Complete Education coverage.
- Exclusive ownership.
- Inputs and outputs.
- Delegation.
- Stop conditions.
- Human review.
- Academic integrity.
- Minor safety.
- Privacy.
- Accessibility.
- Source integrity.
- Assessment safeguards.
- Quality criteria.
- No circular delegation.
- No self-review.
- No contradictory instructions.

Fix every finding and repeat until zero findings remain.

## Phase G - Verification pass 3: adversarial and cross-file

Use another fresh review context.

Attempt to find:
- Ways to bypass academic integrity controls.
- Ways to issue grades without humans.
- Ways to expose minors' or student data.
- Ways to activate external tools.
- Hidden overlap.
- Ambiguous authority.
- Unsupported platform claims.
- Fake native structures.
- Stale documentation assumptions.
- Inconsistent terminology.
- Incomplete workflows.
- Unsafe defaults.
- Runtime claims not supported by static verification.

Fix every finding and repeat the adversarial review until zero findings remain.

## Phase H - Final platform gate

The platform passes only if all conditions are true:

- Documentation verification complete.
- Capability matrix complete.
- Implementation complete.
- All required files present.
- No empty or placeholder files.
- No unsupported components.
- No unresolved findings.
- No out-of-scope modification.
- No secret or personal data.
- No external integration enabled.
- All safety controls present.
- Human-review boundaries explicit.
- Independent quality approval recorded.
- Static-scope limitation stated honestly.
- Audit report complete.

If any condition is false:
- Do not advance.
- Repair the platform.
- Restart the failed verification phase.
- If the condition cannot be repaired within the authorized scope, stop the entire task and report the blocker.

When all conditions are true:
- Mark the platform `PASS - fully verified within authorized static scope`.
- Freeze the platform.
- Do not modify it while implementing later platforms unless a later cross-platform consistency check identifies a critical contradiction. Any such change requires repeating all three verification passes for the changed platform.
- Proceed automatically to the next platform.



# 13. PLATFORM 1 - CHATGPT

Target:
- `chatgpt/education/`

## 13.1 Product boundary

This implementation is for ChatGPT web and desktop product surfaces, not Codex, not the OpenAI API, and not the OpenAI Agents SDK.

Use only currently verified ChatGPT-native surfaces, such as:
- Projects.
- Project instructions.
- Project knowledge files.
- Custom GPTs.
- ChatGPT Skills.
- Workspace Agents when officially available to the relevant workspace plan.
- Apps or connectors only as optional, disabled, human-controlled integrations.
- Manual UI configuration where native features have no repository-native executable format.

Do not:
- Create fake repository agent files.
- Create Codex files.
- Create OpenAI Agents SDK code.
- Create custom Actions or MCP apps unless explicitly required and safely justified. For this specialization, they should normally be omitted because no external action is necessary.
- Assume Workspace Agents are available to every plan.
- Treat Study Mode as a configurable component inside Projects or GPTs when the current official documentation says it is unavailable there.
- Activate an app, connector, action, schedule, or workspace agent.

## 13.2 Required implementation approach

Create the strongest practical ChatGPT Education package using mutually exclusive or clearly differentiated deployment profiles:

1. Project profile:
   - Baseline Education workspace.
   - Project instructions.
   - Uploadable project knowledge.
   - Setup and verification guidance.

2. Custom GPT profile:
   - A native Custom GPT configuration specification.
   - Name, description, instructions, conversation starters, knowledge mapping, capabilities, limitations, privacy settings, and testing checklist.
   - No external Actions by default.
   - Apps only if current official documentation supports them and they remain optional and disabled.

3. Skills:
   - Create real ChatGPT Skill packages only if the current official documentation defines an uploadable or editable native format that can be represented accurately in the repository.
   - Otherwise create a manual skill configuration specification for each selected skill and clearly label it as UI setup content, not an installed skill package.
   - Select only skills with non-overlapping value.

4. Workspace Agent profile:
   - Include only if current official documentation confirms availability and configuration.
   - Clearly mark plan/workspace restrictions.
   - Do not create or publish the agent.
   - Do not create schedules.
   - Do not enable connected apps, custom MCP, or channels.
   - Provide a manual setup specification and preview test matrix only.

## 13.3 Minimum ChatGPT content

The final structure must include, using names adapted to the verified native format:

- Platform Education README.
- Official capability and plan limitations.
- Project setup guide.
- Complete project instructions.
- Knowledge files covering:
  - Department operating model.
  - Safety, privacy, safeguarding, and academic integrity.
  - Quality and completion standards.
  - Workflow catalogue.
  - Human-review matrix.
- Custom GPT configuration.
- Appropriate native Skills or manual Skill specifications.
- Optional Workspace Agent specification only when supported and valuable.
- Optional integrations guide that keeps everything disabled.
- Test and preview scenarios.
- Platform audit report.

Do not create multiple active agents with duplicated educational authority. Prefer one department entry point supported by reusable skills and explicit role routing.

## 13.4 ChatGPT-specific acceptance tests

Statically verify:
- Project instructions are within current product limits or are divided using a documented setup method.
- Knowledge files are text-forward and suitable for upload.
- Custom GPT instructions are not duplicated or contradictory.
- Capabilities are limited to those required.
- Apps and Actions rules reflect the current product restriction that may prevent simultaneous use.
- Study Mode limitations are documented accurately.
- Workspace Agent content is omitted when unverified.
- No fake native file is presented as automatically installable.
- All plan restrictions are explicit.

Complete all three verification passes and the final gate before touching `claude/education/`.



# 14. PLATFORM 2 - CLAUDE

Target:
- `claude/education/`

## 14.1 Product boundary

This implementation is for Claude web and desktop product surfaces, not Claude Code and not the Anthropic API.

Use only currently verified Claude-native surfaces, such as:
- Claude Projects.
- Project instructions.
- Project knowledge.
- Claude Skills.
- Connectors as optional, disabled, user-controlled integrations.
- Manual UI setup specifications where required.

Do not:
- Create `CLAUDE.md` or Claude Code repository configuration.
- Create Claude Code agents, hooks, commands, permissions, or MCP configuration.
- Activate connectors.
- Authenticate.
- Assume paid-only features are available to every user.
- Use desktop extensions that can access local files or applications.
- Simulate agents when Claude does not expose the relevant native agent surface.

## 14.2 Required implementation approach

Create:

1. Claude Project profile:
   - Project instructions.
   - Project knowledge package.
   - Setup guide.
   - Plan and RAG behavior notes when relevant.
   - Privacy and sharing guidance.

2. Claude Skills:
   - Create native custom Skill packages only in the current official format.
   - Select the minimum complete set.
   - Ensure each skill has exclusive scope, invocation guidance, stop conditions, safety rules, and output criteria.
   - Do not create a skill merely to duplicate project instructions.

3. Connector guidance:
   - Include only an optional, disabled guide if connectors provide clear educational value.
   - No real URLs, credentials, private endpoints, or recommended automatic connection.
   - Require human approval, institutional authorization, least privilege, and data minimization.
   - State that local desktop extensions are outside the safe default scope.

4. Artifacts and file creation:
   - Document them only as optional output capabilities if officially supported.
   - Do not create an artifact runtime or treat artifacts as agents.

## 14.3 Minimum Claude content

The final structure must include, using names adapted to the verified native format:

- Platform Education README.
- Current capability and plan limitations.
- Project setup guide.
- Complete project instructions.
- Project knowledge files covering:
  - Operating model.
  - Safety, privacy, safeguarding, and integrity.
  - Quality standards.
  - Workflow catalogue.
  - Human-review matrix.
- Native Skills in the official format.
- Optional disabled connector guidance.
- Test scenarios for project instructions and skills.
- Platform audit report.

## 14.4 Claude-specific acceptance tests

Statically verify:
- No Claude Code content exists.
- Project instructions and knowledge have distinct purposes.
- Skill instructions do not conflict with project instructions.
- RAG or knowledge behavior is described without unsupported guarantees.
- Connector content is optional and disabled.
- No local system access is authorized.
- Plan limitations are explicit.
- No simulated multi-agent architecture is created.
- All Skills use the currently documented format.

Complete all three verification passes and the final gate before touching `local/education/`.



# 15. PLATFORM 3 - LOCAL

Target:
- `local/education/`

## 15.1 Product boundary

`local/` is not Ollama, LM Studio, a specific model, or a universal runtime. It is a provider-independent, local-first Education specification and configuration package.

It must not:
- Download or run a model.
- Start a runtime.
- Install dependencies.
- Include executable adapters.
- Include a server or UI.
- Bind the Education department to a specific model, provider, operating system, endpoint, or hardware.
- Claim compatibility with every local model.
- Enable tools, network access, file access, memory, tracing, or persistence by default.

## 15.2 Required implementation approach

Create a declarative package that allows a user to configure:

- Provider.
- Runtime.
- Model.
- Endpoint.
- Context limits.
- Structured-output support.
- Tool support.
- Tool permissions.
- File access.
- Network access.
- Memory.
- Logging.
- Tracing.
- Data retention.
- Human approval.
- Role routing.
- Skill selection.
- Workflow selection.

All potentially sensitive or powerful features must be disabled by default.

The package must include a schema that distinguishes:
- Required.
- Optional.
- Disabled by default.
- Unsupported by the selected runtime.
- Human approval required.

## 15.3 Minimum Local content

Create a coherent structure containing:

- `README.md`
  - Scope.
  - Provider independence.
  - Limitations.
  - Safe setup principles.
  - No-runtime statement.
  - Manual verification instructions.

- Example configuration:
  - No real endpoint.
  - No credentials.
  - `enabled: false` for tools, network, persistence, tracing, connectors, and external actions.
  - Conservative data-retention defaults.

- Machine-readable schema:
  - JSON Schema or another openly documented neutral schema.
  - Validates the example configuration conceptually.
  - Defines roles, skills, workflows, policies, permissions, approval gates, and provider capability declarations.
  - Does not become a universal cross-platform schema outside `local/`.

- Role specifications:
  - Canonical education responsibilities.
  - Exclusive ownership.
  - Inputs and outputs.
  - Delegation and stop conditions.
  - Prohibited actions.

- Skill specifications:
  - Selected education skills.
  - Trigger and non-trigger conditions.
  - Required context.
  - Output contract.
  - Safety controls.

- Workflow specifications:
  - Required professional workflows.
  - Human-review gates.
  - Failure behavior.
  - No external execution.

- Policy specifications:
  - Privacy.
  - Minors.
  - Academic integrity.
  - Assessment.
  - Accessibility.
  - Source integrity.
  - External actions.
  - Logging and retention.

- Prompt templates:
  - Provider-neutral.
  - No model-specific syntax unless isolated as an optional documented example.
  - No hidden chain-of-thought request.
  - No automatic actions.

- Provider capability template:
  - Generic.
  - Disabled.
  - User-completed.
  - No real endpoint.
  - No claim of compatibility.

- Static conformance checklist.
- Platform audit report.

## 15.4 Local-specific acceptance tests

Statically verify:
- No provider or model is required.
- No runtime code exists.
- No executable adapter exists.
- No real endpoint or credential exists.
- All powerful capabilities default to disabled.
- The schema and example configuration use consistent fields.
- Role, skill, workflow, and policy identifiers resolve correctly.
- No `common/` or cross-platform schema is created.
- No claim of universal model compatibility exists.
- No runtime execution claim exists.

Complete all three verification passes and the final gate before touching `openai-agents-sdk/education/`.



# 16. PLATFORM 4 - OPENAI AGENTS SDK

Target:
- `openai-agents-sdk/education/`

## 16.1 Product boundary

This implementation is for the current official OpenAI Agents SDK. Real SDK implementation code is permitted.

Do not create:
- A server.
- A web application.
- A desktop application.
- A mobile application.
- A deployment.
- Infrastructure.
- An installer.
- Authentication.
- A live API call.
- A model invocation.
- An active MCP connection.
- An external tool integration.
- A persistent database.
- A production monitoring service.

Do not run the code, tests, package manager, formatter, linter, build, or examples.

## 16.2 Required SDK mechanisms

Use only currently verified SDK mechanisms, where supported:

- Agents.
- Instructions.
- Structured outputs.
- Context or run state.
- Handoffs or agent-as-tool patterns.
- Input guardrails.
- Output guardrails.
- Tool guardrails.
- Human-in-the-loop approvals.
- Sessions only if necessary and safe.
- Tracing configuration.
- Typed models.
- Usage or result metadata where useful.

Important:
- Verify the exact current API names and signatures.
- Do not rely on stale examples.
- Tool guardrails may not automatically govern handoffs; enforce safeguards at every applicable boundary.
- Tracing may be enabled by default in the SDK. The Education implementation must disable tracing by default or apply an officially supported privacy-preserving configuration that prevents student or minor data exposure.
- Persistent sessions must be off by default.
- External tools must be absent or disabled by default.

## 16.3 Required SDK architecture

Implement a production-quality static source package with:

1. Typed education context:
   - Educational stage.
   - Subject.
   - learner/audience description.
   - Jurisdiction or institution.
   - Authoritative sources.
   - Assessment stakes.
   - Privacy classification.
   - Minor involvement.
   - Accessibility needs.
   - Human decision-maker.
   - Allowed tools.
   - Prohibited actions.

2. Typed output models:
   - Curriculum package.
   - Lesson or unit plan.
   - Assessment blueprint.
   - Rubric.
   - Feedback draft.
   - Tutoring plan.
   - Accessibility review.
   - Source review.
   - Learning analytics interpretation.
   - Human-review packet.
   - Quality audit result.

3. Agents:
   - Coordinator.
   - Curriculum and instruction.
   - Assessment and feedback.
   - Tutor and learner support.
   - Accessibility, differentiation, and inclusion.
   - Educational content and evidence.
   - Learning analytics and administration.
   - Safeguarding, privacy, and academic integrity reviewer.
   - Independent quality reviewer.

Agents must have:
- Exclusive instructions.
- Bounded tools.
- Explicit handoffs.
- Stop conditions.
- Structured outputs.
- Human-review boundaries.
- No overlapping final authority.

4. Orchestration:
   - Deterministic routing rules where possible.
   - Explicit high-risk routing.
   - No circular handoffs.
   - Maximum handoff or step safeguards where supported.
   - Coordinator cannot approve its own output.
   - Reviewer agents cannot author the artifact they review.

5. Guardrails:
   - Academic misconduct.
   - Impersonation.
   - Fabricated sources.
   - Minor personal data.
   - Consequential grades.
   - Safeguarding concerns.
   - Medical, psychological, legal, or disability diagnosis.
   - External action requests.
   - Secrets and credentials.
   - Unsupported authoritative claims.
   - Output privacy and citation checks.

6. Human-in-the-loop:
   - Pause or return a pending-approval result for sensitive tool calls or consequential decisions.
   - No automatic continuation after a rejected approval.
   - Serializable approval state only if the SDK supports it and without persistent sensitive data by default.
   - Clear reviewer identity and decision reason fields.

7. Safe internal tools:
   - Only pure, deterministic, local, side-effect-free helper tools when they provide real value.
   - Examples may include context completeness checks, identifier redaction, approval classification, rubric consistency checks, or review-packet assembly.
   - No network, file-system mutation, email, calendar, LMS, SIS, gradebook, browser, database, or shell tools.

8. Privacy:
   - Tracing off by default.
   - No student data in logs.
   - No persistent session by default.
   - Data-minimizing examples.
   - Synthetic examples only.

9. Documentation:
   - Architecture.
   - Safety model.
   - Human-review flow.
   - Configuration.
   - Supported and unsupported features.
   - Static usage examples that are not executed.
   - Limitations.

10. Tests:
   - Create static unit-test files for guardrails, routing, output validation, and approval requirements only if they are meaningful and use the current supported SDK/test ecosystem.
   - Do not execute them.
   - Do not claim they pass.
   - Label them as unexecuted static test definitions in the audit report.

## 16.4 Suggested source structure

Adapt this structure only when it matches the current official SDK and existing repository conventions:

- `README.md`
- `pyproject.toml` or the current appropriate package metadata.
- `src/education_department/__init__.py`
- `src/education_department/config.py`
- `src/education_department/context.py`
- `src/education_department/models.py`
- `src/education_department/agents.py`
- `src/education_department/handoffs.py`
- `src/education_department/guardrails.py`
- `src/education_department/approvals.py`
- `src/education_department/tools.py`
- `src/education_department/workflows.py`
- `src/education_department/privacy.py`
- `src/education_department/prompts/`
- `tests/`
- `docs/`
- `AUDIT_REPORT.md`

Do not create files that have no substantive purpose. Merge modules when the implementation is clearer and still maintainable.

## 16.5 OpenAI Agents SDK acceptance tests

Statically verify:
- Imports and API usage match current official documentation.
- No deprecated SDK surface is used.
- Every agent has an exclusive responsibility.
- Handoffs cannot loop.
- High-risk requests route to human review.
- Final grades cannot be issued automatically.
- Input, output, tool, and handoff boundaries are all protected.
- Tracing and persistence are safe by default.
- No external side-effect tool exists.
- No secret is embedded.
- Typed outputs are complete.
- Tests are clearly unexecuted.
- README does not claim runtime validation.
- No server, UI, deployment, or installer exists.

Complete all three verification passes and the final gate.



# 17. FINAL CROSS-PLATFORM CONSISTENCY AUDIT

After all four platforms individually pass, perform a final read-only consistency audit across only the four completed Education directories.

Verify:

1. All four represent the same professional Education mission.
2. Responsibility names and meanings are conceptually consistent.
3. Platform-specific structures remain native and independent.
4. No cross-platform runtime or adapter exists.
5. No `common/` directory exists.
6. Safety requirements are equally strong.
7. Human-review requirements are consistent.
8. Unsupported components are absent.
9. Plan and product limitations are platform-specific and accurate.
10. Local remains provider-independent.
11. ChatGPT does not contain Codex or SDK structures.
12. Claude does not contain Claude Code structures.
13. OpenAI Agents SDK does not contain a server, UI, deployment, or active integration.
14. No file contains secrets, personal data, real endpoints, private URLs, TODOs, placeholders, or unsupported claims.
15. No platform claims executed runtime verification.
16. Every platform has a complete audit report.

If the final cross-platform audit identifies a defect:

- Modify only the affected Education platform.
- Repeat all three verification passes for that platform.
- Repeat the final cross-platform consistency audit.
- Continue until zero findings remain.



# 18. REQUIRED AUDIT REPORT FORMAT

Each platform must contain an `AUDIT_REPORT.md` or native-equivalent report with:

1. Platform and specialization.
2. Verification scope.
3. Static-verification limitation.
4. Official documentation evidence.
5. Current product surface and plan limitations.
6. Native capability matrix.
7. Unsupported and omitted components.
8. Final file inventory.
9. Responsibility coverage matrix.
10. Skill coverage matrix.
11. Workflow coverage matrix.
12. Safety and human-review matrix.
13. Structural verification results.
14. Semantic verification results.
15. Adversarial verification results.
16. Findings and remediation history.
17. Out-of-scope change check.
18. Secret and personal-data check.
19. Independent reviewer identity or review context.
20. Final status.

The final status must be exactly one of:

- `PASS - fully verified within authorized static scope`
- `BLOCKED - do not proceed`

Never use `PASS` when runtime execution would be required to prove a material claim.



# 19. FAILURE BEHAVIOR

Stop the entire process immediately when:

- Official documentation cannot verify a required mechanism.
- A required platform-native implementation is impossible.
- An existing repository conflict cannot be resolved inside the permitted path.
- Independent review cannot be achieved.
- A security, privacy, integrity, or safeguarding defect cannot be eliminated.
- A required file would have to be a fake or placeholder.
- Verification would require executing software or accessing the user's environment.
- A material runtime claim cannot be bounded as unverified.
- Any platform remains incomplete.

When blocked:

1. Do not modify the next platform.
2. Preserve completed and verified prior platforms.
3. State the current platform.
4. State the exact failed gate.
5. List the unresolved evidence.
6. List the minimum user or repository decision needed.
7. Do not claim completion.



# 20. FINAL RESPONSE REQUIREMENTS

When all work is complete, respond with a concise final report containing:

- Overall status.
- Platforms completed in order.
- Final status of each platform.
- Number of files created and modified per platform.
- Confirmation that no other platform or specialization was modified.
- Confirmation that no commands, scripts, builds, tests, installations, Git operations, authentication, integrations, or external actions were executed.
- Confirmation that all integrations remain disabled.
- Confirmation that verification was static and documentary.
- Any plan or product limitations documented.
- Location of each audit report.

Do not paste all generated file content into the response.
Do not provide a celebratory or vague completion claim.
Do not say "100% runtime tested."
Use the phrase:

`All four Education implementations passed every required gate and are fully verified within the authorized static scope.`

only when every platform and the final cross-platform audit have zero unresolved findings.



# 21. START

Begin with `chatgpt/education/`.

Do not inspect, create, or modify `claude/education/`, `local/education/`, or `openai-agents-sdk/education/` until ChatGPT has passed the complete documentation analysis, implementation, three independent verification passes, and final platform gate.

After ChatGPT passes, continue automatically to Claude. Repeat the same strict rule for Local and OpenAI Agents SDK.

END MASTER PROMPT
