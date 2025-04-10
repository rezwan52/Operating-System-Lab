def scan_disk_scheduling(requests, head_start, disk_size, direction):

    requests = [r for r in requests if r != 0]

    seek_sequence = []
    seek_count = 0

    left = [r for r in requests if r < head_start]
    right = [r for r in requests if r >= head_start]

    if direction == "left":
        for r in sorted(left, reverse=True):
            seek_sequence.append(r)
            seek_count += abs(head_start - r)
            head_start = r
        seek_count += head_start
        head_start = 0
        for r in sorted(right):
            seek_sequence.append(r)
            seek_count += abs(head_start - r)
            head_start = r
    else:
        for r in sorted(right):
            seek_sequence.append(r)
            seek_count += abs(head_start - r)
            head_start = r
        seek_count += disk_size - 1 - head_start
        head_start = disk_size - 1
        for r in sorted(left, reverse=True):
            seek_sequence.append(r)
            seek_count += abs(head_start - r)
            head_start = r

    return seek_sequence, seek_count


requests = [0, 14, 41, 53, 65, 67, 98, 122, 124, 183, 199]
head_start = 53
disk_size = 200
direction = "right"

sequence, total_seek = scan_disk_scheduling(requests, head_start, disk_size, direction)

print("Seek Sequence:\n", sequence)
print(" ")
print("Total Seek Time:", total_seek)
