def sjf(process_list):
    t = 0
    gantt = []
    completed = {}
    BT = []
    AT = []

    while process_list != []:
        available = []
        for i in process_list:
            if i[1] <= t:
                available.append(i)
        if available == []:
            t += 1
            gantt.append("idle")
            continue
        else:

            available.sort()
            process = available[0]

            burst_time = process[0]
            arrival_time = process[1]
            p_id = process[2]

            t += burst_time
            gantt.append(p_id)
            BT.append(burst_time)
            AT.append(arrival_time)

            completion_time = t
            turn_around_time = completion_time - arrival_time
            waiting_time = turn_around_time - burst_time
            process_list.remove(process)

            completed[p_id] = [completion_time, turn_around_time, waiting_time]

    print("gantt:\n", gantt)
    print("Completion, Turnaround and Waiting Times:\n", completed)


if __name__ == "__main__":
    process_list = [
        [7, 0, "p1"],
        [4, 1, "p2"],
        [15, 2, "p3"],
        [11, 3, "p4"],
        [20, 4, "p5"],
        [9, 4, "p6"],
    ]
    sjf(process_list)
