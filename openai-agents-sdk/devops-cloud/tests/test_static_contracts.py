from devops_cloud_department.agents import ROLE_CONTRACTS


def test_section_01_roles_have_distinct_ownership():
    assert set(ROLE_CONTRACTS) == {"devops-cloud-orchestrator", "cloud-and-platform-architect"}
    assert "self-approval" in ROLE_CONTRACTS["devops-cloud-orchestrator"].excludes
    assert "ADRs" in ROLE_CONTRACTS["cloud-and-platform-architect"].owns
