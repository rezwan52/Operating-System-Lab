def elevator_disk_scheduling(requests, head_start, disk_size, direction):
    requests = [r for r in requests if r != 0]

    seek_count = 0

    left = [r for r in requests if r <= head_start]
    right = [r for r in requests if r >= head_start]

    if direction == "left":
        for r in sorted(left, reverse=True):
            seek_count += abs(head_start - r)
            head_start = r
        seek_count += head_start
        head_start = 0

        for r in sorted(right):
            seek_count += abs(head_start - r)
            head_start = r
    else:
        for r in sorted(right):
            seek_count += abs(head_start - r)
            head_start = r
        seek_count += disk_size - 1 - head_start
        head_start = disk_size - 1

        for r in sorted(left, reverse=True):
            seek_count += abs(head_start - r)
            head_start = r

    return seek_count


requests = [137, 240, 179, 75, 118, 29, 15, 51]
head_start = 55
disk_size = 241
direction = "right"


total_seek = elevator_disk_scheduling(requests, head_start, disk_size, direction)


print("Total Seek Time:", total_seek)
