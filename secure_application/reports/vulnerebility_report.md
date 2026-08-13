# Vulnerability Report - Group 2

1. **SQL Injection**: Login uses string formatting `f"SELECT... '{username}'"`.
2. **Broken Access Control (IDOR)**: `check_balance()` allows viewing any account ID without checking ownership.
3. **Sensitive Data Exposure**: `login()` prints plain text passwords to console logs.