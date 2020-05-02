import time

def itarator():
    time_monotonic_codes = []
    for x in range(3660):
        time_monotonic_codes.append(str(time.monotonic_ns())[5:10])
    time_monotonic_codes = [time_monotonic_codes[0],time_monotonic_codes[3659]]
    return time_monotonic_codes

def randomize():
    time_monotonic_codes = itarator()
    if time_monotonic_codes[0] == time_monotonic_codes[1]:
        randomize()
    return time_monotonic_codes[1]
