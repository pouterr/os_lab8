def sjn_scheduling(processes):
    time = 0
    waiting_time = 0
    remaining_time = [process['burst_time'] for process in processes]

    while True:
        min_burst = float('inf')
        shortest_job = None
        done = True

        for i in range(len(processes)):
            if processes[i]['arrival_time'] <= time and remaining_time[i] < min_burst:
                min_burst = remaining_time[i]
                shortest_job = i
                done = False

        if done:
            break

        remaining_time[shortest_job] -= 1
        time += 1

        if remaining_time[shortest_job] == 0:
            waiting_time += time - processes[shortest_job]['arrival_time']

    average_waiting_time = waiting_time / len(processes)
    return average_waiting_time

# Example usage
processes = [
    {'name': 'P1', 'arrival_time': 0, 'burst_time': 7},
    {'name': 'P2', 'arrival_time': 2, 'burst_time': 4},
    {'name': 'P3', 'arrival_time': 4, 'burst_time': 1},
    {'name': 'P4', 'arrival_time': 5, 'burst_time': 4}
]

average_waiting_time = sjn_scheduling(processes)
print(f'Average Waiting Time (SJN): {average_waiting_time}')