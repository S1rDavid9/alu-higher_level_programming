-- List all privileges for user_0d_1
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- List all privileges for user_0d_2
SHOW GRANTS FOR 'user_0d_2'@'localhost';
REVOKE AUDIT_ABORT_EXEMPT, FIREWALL_EXEMPT, AUTHENTICATION_POLICY_ADMIN, GROUP_REPLICATION_STREAM, PASSWORDLESS_USER_ADMIN, SENSITIVE_VARIABLES_OBSERVER, TELEMETRY_LOG_ADMIN ON *.* FROM 'user_0d_1'@'localhost', 'user_0d_2'@'localhost';
