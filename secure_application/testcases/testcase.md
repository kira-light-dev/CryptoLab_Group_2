# Test Cases

1. **SQLi Test**: Input `' OR '1'='1` in username to bypass login.
2. **IDOR Test**: Log in as Alice (ID 1) and query balance for Account ID 2 (Bob).
3. **Log Exposure**: Input password and verify it appears in console output logs.