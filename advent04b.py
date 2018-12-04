import sys
import operator

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

guard_max_sleep = {k: max(v) for k,v in guard_sleep_minutes.items()}
guard_max_sleep = sorted(guard_max_sleep.items(), key=operator.itemgetter(1))
(sleepy_guard_id, sleepy_value) = guard_max_sleep[-1]
sleepy_minute = guard_sleep_minutes[sleepy_guard_id].index(sleepy_value)

print sleepy_guard_id * sleepy_minute
