class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.vals = set()
        self.miss = 0
        self.res = []  # tracks access order (oldest to newest)

    def get(self, key: int) -> bool:
        if key not in self.vals:
            return False
        
        # Move accessed key to end (most recently used)
        self.res.remove(key)  # O(n) - not ideal but works for small inputs
        self.res.append(key)
        return True

    def put(self, key: int) -> None:
        if key in self.vals:
            # Update existing key
            # Move to most recently used
            self.res.remove(key)
            self.res.append(key)
        else:
            self.miss+=1
            # Add new key
            if len(self.vals) >= self.capacity:
                # Remove least recently used (first in list)

                lru_key = self.res.pop(0)
                self.vals.remove(lru_key)
            
            self.vals.add(key)
            self.res.append(key)



"""You are given:

A cache of capacity ( k )

A sequence of ( m ) requests ( r_1, r_2,.., r_m )

For each request:

If the item is already in the cache, this is a hit.

Otherwise, this is a miss. Insert the item:

If the cache is not full, simply insert it.

If the cache is full, evict one item according to the policy."""


def LRU_Test(k: int, r: list) -> int:

    cache = LRUCache(k) ## initialize cache with size K

    for value in r:
        cache.put(value)


    return cache.miss



        