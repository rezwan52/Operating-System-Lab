def sjs(process_list):
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
            gantt.append("Idle")
            continue
        else:
            available.sort()
            process = available[0]

            brust_time = process[0]
            arrival_time = process[1]
            p_id = process[2]

            t += brust_time
            gantt.append(p_id)
            BT.append(brust_time)
            AT.append(arrival_time)

            completion_time = t
            turn_around_time = completion_time - arrival_time
            waiting_time = turn_around_time - brust_time
            process_list.remove(process)
            completed[p_id] = [
                completion_time,
                turn_around_time,
                waiting_time,
            ]
    print("Gantt:\n", gantt)
    print("Arrival Time:\n", AT)
    print("Burst Time:\n", BT)
    print("Completion, Turnaround and Waiting Times:\n", completed)


if __name__ == "__main__":
    process_list = [
        [6, 2, "p1"],
        [2, 5, "p2"],
        [8, 1, "p3"],
        [3, 0, "p4"],
        [4, 4, "p5"],
    ]
    sjs(process_list)
