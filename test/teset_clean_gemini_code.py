import json
import html
import sys
import pathlib
import pytest

# Ensure project root is on sys.path so `TTA` can be imported when running tests
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from TTA import clean_gemini_code


def test_extract_from_valid_json():
    raw = json.dumps({"python": "print('hello')\n"})
    out = clean_gemini_code(raw)
    assert isinstance(out, str)
    assert out.strip() == "print('hello')"


def test_unescape_html_and_json():
    raw_obj = {"python": "a = 1\nprint(a)\n"}
    raw = html.escape(json.dumps(raw_obj))
    # simulate content that was HTML-escaped by the UI
    out = clean_gemini_code(raw)
    assert out.strip().startswith("a = 1")
