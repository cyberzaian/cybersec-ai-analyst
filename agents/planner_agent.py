def plan_task(log_line):
    if "Failed password" in log_line:
        return "Analyze for brute force"
    elif "index.php" in log_line:
        return "Check for SQL injection"
    else:
        return "Basic anomaly check"
