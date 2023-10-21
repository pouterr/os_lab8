def mlq_scheduling(processes):
    high_priority_queue = []
    low_priority_queue = []
    time = 0
    waiting_time = 0

    for process in processes:
        if process['priority'] == 'High':
            high_priority_queue.append(process)
        else:
            low_priority_queue.append(process)

    for queue in [high_priority_queue, low_priority_queue]:
        for process in queue:
            waiting_time += max(0, time - process['arrival_time'])
            time = max(time, process['arrival_time']) + process['burst_time']

    average_waiting_time = waiting_time / len(processes)
    return average_waiting_time

# Example usage
processes = [
    {'name': 'P1', 'priority': 'High', 'arrival_time': 0, 'burst_time': 10},
    {'name': 'P2', 'priority': 'Low', 'arrival_time': 1, 'burst_time': 4},
    {'name': 'P3', 'priority': 'High', 'arrival_time': 2, 'burst_time': 5}
]

average_waiting_time = mlq_scheduling(processes)
print(f'Average Waiting Time (Multiple-Level Queues Scheduling): {average_waiting_time}')