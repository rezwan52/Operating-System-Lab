def sstf_disk_schedule(req_seq, head=50):
    total_seek = 0
    current_position = head
    req_seq_copy = req_seq.copy()

    print("Sequence:")
    while req_seq_copy:

        close_request = min(req_seq_copy, key=lambda x: abs(x - current_position))

        print(f"{current_position} ==> {close_request}")
        total_seek += abs(close_request - current_position)
        current_position = close_request

        req_seq_copy.remove(close_request)

    print(f"Total num of seek operations: {total_seek}")
    return total_seek


if __name__ == "__main__":
    req_seq = [176, 79, 34, 60, 92, 11, 41, 114]
    sstf_disk_schedule(req_seq, head=50)
