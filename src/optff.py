


def find_next_use(r, item, current_index):
    for j in range(current_index + 1, len(r)):
        if r[j] == item:
            return j
        
    return float('inf')  # never used again


def OPT_Test(k, r):
    cache = set()
    misses = 0

    for i in range(len(r)):
        item = r[i]

        if item in cache:
            continue

        misses += 1

        if len(cache) >= k:
            farthest = -1
            evict = None
            for cached_item in cache:
                next_use = find_next_use(r, cached_item, i)
                if next_use == float('inf'):
                    evict = cached_item
                    break
                elif next_use > farthest:
                    farthest = next_use
                    evict = cached_item
            cache.remove(evict)

        cache.add(item)

    return misses