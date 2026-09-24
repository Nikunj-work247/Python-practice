logs = [
    {
        "timestamp": "2026-09-24 10:15:00",
        "log_level": "INFO",
        "message": "User logged in",
        "user_id": 101
    },
    {
        "timestamp": "2026-09-24 10:20:00",
        "log_level": "ERROR",
        "message": "Database connection failed",
        "user_id": 102
    },
    {
        "timestamp": "2026-09-24 10:25:00",
        "log_level": "WARNING",
        "message": "High memory usage",
        "user_id": 101
    },
    {
        "timestamp": "2026-09-24 11:05:00",
        "log_level": "ERROR",
        "message": "Database connection failed",
        "user_id": 103
    },
    {
        "timestamp": "2026-09-24 11:15:00",
        "log_level": "INFO",
        "message": "User logged out",
        "user_id": 101
    },
    {
        "timestamp": "2026-09-24 11:30:00",
        "log_level": "ERROR",
        "message": "Invalid authentication token",
        "user_id": 102
    },
    {
        "timestamp": "2026-09-24 12:10:00",
        "log_level": "INFO",
        "message": "Request processed",
        "user_id": 104
    },
    {
        "timestamp": "2026-09-24 12:20:00",
        "log_level": "WARNING",
        "message": "Slow request detected",
        "user_id": 101
    }
]


# Filter logs by log level

error_logs = [
    log for log in logs
    if log["log_level"] == "ERROR"
]

warning_logs = [
    log for log in logs
    if log["log_level"] == "WARNING"
]

info_logs = [
    log for log in logs
    if log["log_level"] == "INFO"
]


print("ERROR logs:")
print(error_logs)

print("\nWARNING logs:")
print(warning_logs)

print("\nINFO logs:")
print(info_logs)

# Count occurrences of each log level

log_level_count = {}

for log in logs:
    level = log["log_level"]

    if level in log_level_count:
        log_level_count[level] += 1
    else:
        log_level_count[level] = 1

print("\nLog Level Count:")
print(log_level_count)

# Find the most active user

user_count = {}

for log in logs:
    user_id = log["user_id"]

    if user_id in user_count:
        user_count[user_id] += 1
    else:
        user_count[user_id] = 1

most_active_user = max(user_count, key=user_count.get)

print("\nUser Count:")
print(user_count)

print("\nMost Active User:")
print(most_active_user)

# Group errors by hour

errors_by_hour = {}

for log in error_logs:
    hour = log["timestamp"][11:13]
    hour = int(hour)

    if hour in errors_by_hour:
        errors_by_hour[hour] += 1
    else:
        errors_by_hour[hour] = 1

print("\nErrors by Hour:")
print(errors_by_hour)

total_logs = len(logs)
error_count = len(error_logs)

error_rate = (error_count / total_logs) * 100

error_message_count = {}

for log in error_logs:
    message = log["message"]

    if message in error_message_count:
        error_message_count[message] += 1
    else:
        error_message_count[message] = 1

top_5_errors = sorted(
    error_message_count.items(),
    key=lambda x: x[1],
    reverse=True
)[:5]

most_error_hour = max(errors_by_hour, key=errors_by_hour.get)

summary_report = {
    "total_logs_processed": total_logs,
    "error_rate_percentage": error_rate,
    "top_5_common_error_messages": top_5_errors,
    "time_period_with_most_errors": most_error_hour
}

print("\nSummary Report:")
print(summary_report)