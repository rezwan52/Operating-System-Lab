arrival = [2, 0 , 4]
burst = [5, 3 ,4]


process = sorted(range(len(arrival)), key=lambda x: arrival[x])

arrival_sorted = [arrival[i] for i in process]
burst_sorted = [burst[i] for i in process]

print("Sorted Arrival Times:", arrival_sorted)
print("Sorted Burst Times:", burst_sorted)

print(" ")

completion_times = []
current_time = 0  

for i in range(len(arrival_sorted)):
    
    start_time = max(current_time, arrival_sorted[i])
    
    completion_time = start_time + burst_sorted[i]
    completion_times.append(completion_time)
    
    current_time = completion_time


turn_around_times = []
for i in range(len(arrival_sorted)):
    waiting_time = (completion_times[i] - arrival_sorted[i] )
    turn_around_times.append(waiting_time)

waiting_times = []
for i in range(len(arrival_sorted)):
    waiting_time = (completion_times[i] - arrival_sorted[i] ) - burst_sorted[i]
    waiting_times.append(waiting_time)
 

print("Completion Times:", completion_times)
print("Turn Around Times:", turn_around_times)
print("Waiting Times:", waiting_times) 