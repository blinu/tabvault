from tabvault.classifier import classify

def test_git():
    assert classify("git checkout main") == "git"
