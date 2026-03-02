"""
FIFO Algorithm

Input:
k = cache capacity
r[] = sequence of integer ids (index 0 to m-1) of the requests,
    where m is the total number of requests

Output:
number of cache misses
"""
def fifo(k, r):
    cache = set()
    queue = []
    cache_misses = 0

    for req in r:
        if req not in cache:
            cache_misses += 1
            if len(cache) < k:
                cache.add(req)
                queue.append(req)
            else:
                evict = queue.pop(0)
                cache.remove(evict)
                cache.add(req)
                queue.append(req)

    return cache_misses