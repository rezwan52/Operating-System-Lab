from collections import deque


def fifo_page_replacement(pages, capacity):
    memory = deque()
    miss = 0

    for page in pages:
        if page not in memory:
            miss += 1
            if len(memory) == capacity:
                memory.popleft()
            memory.append(page)

    return miss


pages = [1, 3, 0, 3, 5, 6, 3]
capacity = 3
page_miss = fifo_page_replacement(pages, capacity)

print(f"Number of Missed page: {page_miss}")
