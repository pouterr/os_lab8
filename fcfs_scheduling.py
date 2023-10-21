def fcfs_scheduling(processes):
    time = 0
    waiting_time = 0

    for process in processes:
        waiting_time += max(0, time - process['arrival_time'])
        time = max(time, process['arrival_time']) + process['burst_time']

    average_waiting_time = waiting_time / len(processes)
    return average_waiting_time

# Example usage
processes = [
    {'name': 'P1', 'arrival_time': 0, 'burst_time': 10},
    {'name': 'P2', 'arrival_time': 1, 'burst_time': 4},
    {'name': 'P3', 'arrival_time': 2, 'burst_time': 5}
]

average_waiting_time = fcfs_scheduling(processes)
print(f'Average Waiting Time (FCFS): {average_waiting_time}')
