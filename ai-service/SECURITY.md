# SECURITY.md

## 1. Prompt Injection
Users may try to manipulate AI using harmful inputs.
Example: "Ignore previous instructions"
Solution: Validate and sanitize inputs.

## 2. SQL Injection
Malicious queries like:
'; DROP TABLE users;
Solution: Input validation.

## 3. Rate Limiting
Too many requests can crash system.
Solution: Limit requests per user.

## 4. Unauthorized Access
Users accessing APIs without permission.
Solution: JWT authentication (handled in backend).

## 5. Data Leakage
Sensitive data sent to AI.
Solution: Avoid sending personal data in prompts.
