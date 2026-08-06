# Semgrep Findings

| Vulnerability | File | Line | Severity | Rule ID | Description | Suggested Fix |
|---------------|------|------|----------|----------|-------------|---------------|
| Hardcoded Secret | tests/vulnerable.py | (line) | Medium | (Rule ID) | Hardcoded password found | Use environment variables |
| SQL Injection | tests/vulnerable.py | (line) | High | (Rule ID) | SQL query constructed using user input | Use parameterized queries |
| Command Injection | tests/vulnerable.py | (line) | High | (Rule ID) | User input passed to os.system() | Use subprocess with fixed arguments |
| Weak Cryptography | tests/vulnerable.py | (line) | Medium | (Rule ID) | MD5 is insecure | Use SHA-256 |
| Unsafe Deserialization | tests/vulnerable.py | (line) | High | (Rule ID) | pickle.loads() executes arbitrary code | Use JSON or safe serialization |
