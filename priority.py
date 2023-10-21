def priority_scheduling(processes):
    processes.sort(key=lambda x: x['priority'])
    time = 0
    waiting_time = 0

    for process in processes:
        waiting_time += time
        time += process['burst_time']

    average_waiting_time = waiting_time / len(processes)
    return average_waiting_time

# Example usage
processes = [
    {'name': 'P1', 'priority': 2, 'burst_time': 10},
    {'name': 'P2', 'priority': 1, 'burst_time': 4},
    {'name': 'P3', 'priority': 3, 'burst_time': 5}
]

average_waiting_time = priority_scheduling(processes)
print(f'Average Waiting Time (Priority Scheduling): {average_waiting_time}')