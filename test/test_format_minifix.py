import sys
import pathlib

# Ensure project root is on sys.path so `TTA` can be imported when running tests
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from TTA import format_and_autofix_code


def test_minifix_indentation():
    # Missing indentation for print inside loop — formatter should fix AST
    bad = "for i in range(2):\nprint(i)\n"
    final, report = format_and_autofix_code(bad)
    assert isinstance(final, str)
    # Expect final AST to be valid (True) after minifix/format attempts
    assert report.get("final_ast_ok") is True
