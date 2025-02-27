from tabulate import tabulate


def round_robin(process_list, time_quantum):
    t = 0
    gantt = []
    queue = []
    completed = {}
    remaining_bt = {}
    first_execution = {}
    AT = []
    BT = []

    for process in process_list:
        remaining_bt[process[2]] = process[0]
        AT.append(process[1])
        BT.append(process[0])

    process_list.sort(key=lambda x: x[1])
    queue.append(process_list[0])
    process_index = 1

    while queue:
        process = queue.pop(0)
        p_id = process[2]
        arrival_time = process[1]
        burst_time = process[0]

        if p_id not in first_execution:
            first_execution[p_id] = t

        if remaining_bt[p_id] > time_quantum:
            t += time_quantum
            remaining_bt[p_id] -= time_quantum
            gantt.append(p_id)
        else:
            t += remaining_bt[p_id]
            gantt.append(p_id)
            completion_time = t
            turn_around_time = completion_time - arrival_time
            waiting_time = turn_around_time - burst_time
            completed[p_id] = [
                arrival_time,
                burst_time,
                completion_time,
                turn_around_time,
                waiting_time,
            ]
            remaining_bt[p_id] = 0

        while process_index < len(process_list) and process_list[process_index][1] <= t:
            queue.append(process_list[process_index])
            process_index += 1

        if remaining_bt[p_id] > 0:
            queue.append(process)

        if not queue and process_index < len(process_list):
            gantt.append("Idle")
            queue.append(process_list[process_index])
            process_index += 1

    response_times = {
        p_id: first_execution[p_id] - completed[p_id][0] for p_id in completed
    }

    headers = [
        "Process ID",
        "Arrival Time",
        "Burst Time",
        "Completion Time",
        "Turnaround Time",
        "Waiting Time",
        "Response Time",
    ]
    table_data = [[p_id, *completed[p_id], response_times[p_id]] for p_id in completed]

    print("\nGantt Chart:", gantt)
    print(tabulate(table_data, headers=headers, tablefmt="plain"))


if __name__ == "__main__":
    process_list = [
        [5, 0, "p1"],
        [4, 1, "p2"],
        [2, 2, "p3"],
        [1, 4, "p4"],
    ]
    time_quantum = 2
    round_robin(process_list, time_quantum)
