import subprocess

def test_add():
    result = subprocess.run(["./calculator"], input="+ 2 3\n", text=True, capture_output=True)
    assert "5" in result.stdout

def test_subtract():
    result = subprocess.run(["./calculator"], input="- 5 2\n", text=True, capture_output=True)
    assert "3" in result.stdout
