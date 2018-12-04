import sys

input = [line.rstrip() for line in sys.stdin.readlines()]
input.sort()

current_guard_id = ""
current_sleep_minute = 0
minute_now = 60
guard_sleep_minutes = {}
for line in input:
    if "begins shift" in line:
        current_guard_id = int(line.split()[3].split("#")[1])
    if "falls asleep" in line:
        current_sleep_minute = int(line.split()[1].split(":")[1].split("]")[0])
    if "wakes up" in line:
        minute_now = int(line.split()[1].split(":")[1].split("]")[0])
        if current_guard_id not in guard_sleep_minutes:
            guard_sleep_minutes[current_guard_id] = [0]*60
        for min in range(current_sleep_minute, minute_now):
            guard_sleep_minutes[current_guard_id][min] += 1

max_guard_sleep = 0
sleepiest_guard_id = 0
for guard_id,sleep_mins in guard_sleep_minutes.items():
    total_guard_sleep = sum(sleep_mins)
    if total_guard_sleep > max_guard_sleep:
        max_guard_sleep = total_guard_sleep
        sleepiest_guard_id = guard_id

sleepiest_schedule = guard_sleep_minutes[sleepiest_guard_id]
sleepiest_minute = sleepiest_schedule.index(max(sleepiest_schedule))

print sleepiest_guard_id * sleepiest_minute
