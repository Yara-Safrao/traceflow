# TraceFlow

A command-line tool for chronological log analysis, built to support incident investigation.

> **Status:** early development (work in progress). Only the features listed under "Current features" exist today.

## Why

During an incident, evidence is scattered across different log files. TraceFlow's goal is to merge them into one timeline so the sequence of events is easy to follow.

## Current features

- Parse log lines (`YYYY-MM-DD HH:MM:SS LEVEL message`) into structured events
- Sort events chronologically

## Roadmap

- [ ] Merge multiple log sources into a single timeline
- [ ] Detect suspicious patterns (e.g. repeated failed logins followed by a success)
- [ ] Command-line interface
- [ ] Handling of malformed lines and different time zones
- [ ] Automated tests

## Project structure

```
src/traceflow/   source code (parser, timeline)
samples/         synthetic example logs (no real data)
tests/           tests (coming soon)
```

## Try it

Requires Python 3.12+.

```
python3 -m venv .venv
source .venv/bin/activate
python -c "from src.traceflow.parser import read_log; [print(e) for e in read_log('samples/auth.log')]"
```

## Sample data

All logs in `samples/` are synthetic. IP addresses use the `203.0.113.0/24` range, which is reserved for documentation.

## License

MIT
