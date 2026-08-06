# Static Application Security Testing (SAST) Lab Report

## 1. Objective

The objective of this lab is to gain practical experience with Static Application Security Testing (SAST) using Semgrep. The lab involves installing and configuring Semgrep, creating an intentionally vulnerable Python program, performing a static security scan, analyzing the detected vulnerabilities, and documenting the findings and remediation techniques.

---

## 2. System Information

**Operating System**

Ubuntu 22.04 LTS

**Kernel Version**

(Output of uname -a)

**Python Version**

(Output of python3 --version)

**Semgrep Version**

(Output of semgrep --version)

---

## 3. Installation Procedure

### Step 1

Updated package list.

```bash
sudo apt update
```

### Step 2

Verified Python installation.

```bash
python3 --version
```

### Step 3

Verified pip installation.

```bash
pip3 --version
```

### Step 4

Installed Semgrep.

```bash
pip3 install semgrep
```

### Step 5

Verified installation.

```bash
semgrep --version
```

---

## 4. Dependencies

- Python 3
- pip3
- Semgrep

---

## 5. Test Program

A Python program named **tests/vulnerable.py** was created.

The program intentionally contains:

- Hardcoded credentials
- SQL Injection vulnerability
- Command Injection vulnerability
- Weak Cryptographic Hash (MD5)
- Unsafe Deserialization using pickle

These vulnerabilities were deliberately introduced so that Semgrep could detect them.

---

## 6. Static Analysis

The scan was executed using:

```bash
semgrep scan --config auto .
```

Results were saved as:

```
outputs/semgrep_results.txt
outputs/semgrep_results.json
```

---

## 7. Findings

Semgrep successfully detected multiple security issues.

The detected issues include:

- Hardcoded Secret
- SQL Injection
- Command Injection
- Weak Cryptography
- Unsafe Deserialization

Detailed findings are documented in **analysis/semgrep_findings.md**

---

## 8. Conclusion

Semgrep successfully identified multiple security vulnerabilities without executing the application. The tool provided clear descriptions of each issue and suggested secure coding practices for remediation. Static analysis helps developers identify security weaknesses early in the software development lifecycle, thereby reducing security risks before deployment.
