from datetime import datetime

from src.traceflow.detector import find_bruteforce
from src.traceflow.parser import parse_line
from src.traceflow.timeline import sort_events


def make_event(hora, message):
    return {"timestamp": datetime(2026, 10, 7, 9, hora), "level": "INFO", "message": message}


def test_parse_line():
    event = parse_line("2026-10-07 09:15:02 INFO login success user=maria ip=10.0.0.5")
    assert event["level"] == "INFO"
    assert event["timestamp"] == datetime(2026, 10, 7, 9, 15, 2)


def test_sort_events():
    eventos = [make_event(30, "b"), make_event(10, "a")]
    assert sort_events(eventos)[0]["message"] == "a"


def test_bruteforce_detected():
    eventos = [make_event(i, "login failed user=x ip=1.1.1.1") for i in range(3)]
    eventos.append(make_event(5, "login success user=x ip=1.1.1.1"))
    assert len(find_bruteforce(eventos)) == 1


def test_no_alert_below_threshold():
    eventos = [make_event(1, "login failed user=x ip=1.1.1.1"),
               make_event(2, "login success user=x ip=1.1.1.1")]
    assert find_bruteforce(eventos) == []