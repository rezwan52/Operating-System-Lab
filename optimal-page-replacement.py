def optimal_page_replacement(reference_string, frame_size):
    frames = []
    miss = 0

    for i in range(len(reference_string)):
        page = reference_string[i]

        if page in frames:
            continue

        if len(frames) < frame_size:
            frames.append(page)
            miss += 1
        else:

            next_use = []
            for f in frames:
                if f not in reference_string[i + 1 :]:
                    next_use.append((f, float("inf")))
                else:
                    next_use.append((f, reference_string[i + 1 :].index(f)))

            page_to_replace = max(next_use, key=lambda x: x[1])[0]
            frames[frames.index(page_to_replace)] = page
            miss += 1

    return miss


reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 3]
frame_size = 4

page_miss = optimal_page_replacement(reference_string, frame_size)
print(f"Number of Missed page: {page_miss}")
