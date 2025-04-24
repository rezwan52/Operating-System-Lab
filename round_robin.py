def round_robin(process_list, time_quant=5):
    t = 0
    gantt_chart = []
    completed = {}
    burst_times = {}   

    for i in process_list:
        p_id = i[2]
        burst_time = i[1]
        burst_times[p_id] = burst_time

    while process_list != []:
        available = []

        for i in process_list:
            at = i[0]
            if at <= t:
                available.append(i)

        if available == []:
            gantt_chart.append("idle")
            t += 1
            continue

        else:
            process = available[0]
            gantt_chart.append(process[2])
            process_list.remove(process)

            rem_burst = process[1]

            if rem_burst <= time_quant:
                t += rem_burst
                ct = t
                p_id = process[2]
                arrival_time = process[0]
                burst_time = burst_times[p_id]
                tat = ct - arrival_time
                wt = tat - burst_time

                completed[process[2]] = [ct, tat, wt]
                continue
            else:
                t += time_quant
                process[1] -= time_quant
                process_list.append(process)
    print("Gantt:\n", gantt_chart)
    print("Final_list:\n", completed)

      
        


if __name__=="__main__":
    process_list = [
        [0, 7, "p1"],
        [1, 4, "p2"],
        [2, 15, "p3"],
        [3, 11, "p4"],
        [4, 20, "p5"],
        [4, 9, "p6"],
    ]
    time_quant = 5
    round_robin(process_list, time_quant=5)