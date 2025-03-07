def disk_schedule(req_seq, head=50):
    total_seek = 0
    current_position = head

    print("Sequence:")
    for request in req_seq:
        print(f"{current_position} => {request}")
        total_seek += abs(request - current_position)
        current_position = request

    print(f"Total num of seek operations: {total_seek}")
    return total_seek


if __name__ == "__main__":
    req_seq = [176, 79, 34, 60, 92, 11, 41, 114]
    disk_schedule(req_seq, head=50)
