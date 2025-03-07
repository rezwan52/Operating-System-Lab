from tabulate import tabulate


def priority_scheduling_preemptive(process_list, time_quantum=1):
    process_list.sort(key=lambda x: (x[1], -x[0]))
    t = 0
    gantt = []
    final_list = {}
    remaining_bt = {p[3]: p[2] for p in process_list}
    first_execution = {}
    all_processes_arrived = False

    while remaining_bt:
        available_processes = [
            p for p in process_list if p[1] <= t and p[3] in remaining_bt
        ]

        if available_processes:
            available_processes.sort(key=lambda x: -x[0])
            process = available_processes[0]
            priority, arrival_time, burst_time, p_id = process

            if p_id not in first_execution:
                first_execution[p_id] = t

            gantt.append(p_id)

            if all_processes_arrived:
                execution_time = remaining_bt[p_id]
            else:
                execution_time = min(time_quantum, remaining_bt[p_id])

            t += execution_time
            remaining_bt[p_id] -= execution_time

            if remaining_bt[p_id] == 0:
                completion_time = t
                turn_around_time = completion_time - arrival_time
                waiting_time = turn_around_time - burst_time
                final_list[p_id] = [
                    arrival_time,
                    burst_time,
                    completion_time,
                    turn_around_time,
                    waiting_time,
                ]
                del remaining_bt[p_id]
        else:
            gantt.append("Idle")
            t += time_quantum

        if not all_processes_arrived and all(p[1] <= t for p in process_list):
            all_processes_arrived = True
            process_list.sort(key=lambda x: -x[0])
            for p in process_list:
                if p[3] in remaining_bt:
                    if p[3] not in first_execution:
                        first_execution[p[3]] = t

                    gantt.extend([p[3]] * remaining_bt[p[3]])
                    t += remaining_bt[p[3]]
                    completion_time = t
                    turn_around_time = completion_time - p[1]
                    waiting_time = turn_around_time - p[2]
                    final_list[p[3]] = [
                        p[1],
                        p[2],
                        completion_time,
                        turn_around_time,
                        waiting_time,
                    ]
                    del remaining_bt[p[3]]

    sorted_completed = sorted(final_list.items(), key=lambda x: int(x[0][1:]))

    response_times = {
        p_id: first_execution.get(p_id, final_list[p_id][0]) - final_list[p_id][0]
        for p_id, _ in sorted_completed
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
    table_data = [
        [p_id, *final_list[p_id], response_times[p_id]] for p_id, _ in sorted_completed
    ]

    print("\nGantt Chart:", gantt)
    print(tabulate(table_data, headers=headers, tablefmt="plain"))


if __name__ == "__main__":
    process_list = [
        [10, 0, 5, "P1"],
        [20, 1, 4, "P2"],
        [30, 2, 2, "P3"],
        [40, 4, 1, "P4"],
    ]
    priority_scheduling_preemptive(process_list, time_quantum=1)
