import json
from pathlib import Path

REPORT = Path("/app/report.json")

# Known-correct values for the access.log bundled with this task.
EXPECTED_TOTAL_REQUESTS = 6
EXPECTED_UNIQUE_IPS = 3
EXPECTED_TOP_PATH = "/index.html"


def _load_report():
    assert REPORT.exists(), "no report found at /app/report.json"
    try:
        data = json.loads(REPORT.read_text())
    except json.JSONDecodeError as exc:
        raise AssertionError(f"report.json is not valid JSON: {exc}")
    assert isinstance(data, dict), "report.json must be a single JSON object"
    return data


def test_report_is_valid_json_object():
    """Success criterion 1: /app/report.json exists and contains a single valid JSON object."""
    _load_report()


def test_total_requests():
    """Success criterion 2: total_requests equals the exact number of request lines."""
    data = _load_report()
    assert data.get("total_requests") == EXPECTED_TOTAL_REQUESTS, (
        f"total_requests: expected {EXPECTED_TOTAL_REQUESTS}, got {data.get('total_requests')!r}"
    )


def test_unique_ips():
    """Success criterion 3: unique_ips equals the exact number of distinct client IPs."""
    data = _load_report()
    assert data.get("unique_ips") == EXPECTED_UNIQUE_IPS, (
        f"unique_ips: expected {EXPECTED_UNIQUE_IPS}, got {data.get('unique_ips')!r}"
    )


def test_top_path():
    """Success criterion 4: top_path equals the most frequently requested path."""
    data = _load_report()
    assert data.get("top_path") == EXPECTED_TOP_PATH, (
        f"top_path: expected {EXPECTED_TOP_PATH!r}, got {data.get('top_path')!r}"
    )
