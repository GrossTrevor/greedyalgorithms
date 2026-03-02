# Greedy Algorithms
Python implementation of the FIFO (First-In, First-Out), LRU (Least Recently Used), and OPTFF (Belady’s Farthest-in-Future) algorithms for cache access.

## Authors
* Nicholas Farr UFID: 17993779
* Trevor Gross UFID: 11440394

## Project Structure
```
```

## Written Component
### Question 1

| File | k | m | FIFO | LRU | OPTFF |
|------|---|---|------|-----|-------|
| 1 | 10 | 50 | 28 | 24 | 20 |
| 2 | 35 | 250 | 173 | 173 | 110 |
| 3 | 25 | 100 | 78 | 74 | 53 |

Does OPTFF have the fewest misses? Yes, OPTFF proves to be the most effective algorithm of the three tested. This is because it looks ahead on the input data and makes a perfect eviction choice.

How does FIFO compare to LRU? LRU generally does at least equal or fewer misses to the FIFO algorithm. This is because FIFO just evicts the oldest item, rather than the one being the least frequently used - LRU is being smarter about which ID to evict.

### Question 2
### Question 3
$$
\begin{aligned}
&\text{Let OPTFF be Belady’s Farthest-in-Future algorithm.} \\
&\text{Let } A \text{ be any offline algorithm that knows the full request sequence.} \\
&\text{Prove that the number of misses of OPTFF is no larger than that of } A \text{ on any fixed sequence.} \\
& \\
&\text{Let }
\end{aligned}
$$