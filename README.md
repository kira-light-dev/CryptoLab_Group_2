# Semgrep Static Application Security Testing

## Installation

```bash
pip3 install semgrep
```

## Scan Project

```bash
semgrep scan --config auto .
```

## Save Results

```bash
semgrep scan --config auto . > outputs/semgrep_results.txt
```

JSON Output

```bash
semgrep scan --config auto --json . > outputs/semgrep_results.json
```

## Reports

- analysis/semgrep_report.md
- analysis/semgrep_findings.md

## Vulnerable Test File

```
tests/vulnerable.py
```
