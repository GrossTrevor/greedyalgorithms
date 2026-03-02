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
### Question 2
### Question 3
$$
\begin{aligned}
&\text{Let OPTFF be Belady’s Farthest-in-Future algorithm} \\
&\text{Let } A \text{ be any offline algorithm that knows the full request sequence} \\
&\text{Prove that the number of misses of OPTFF is no larger than that of } A \text{ on any fixed sequence} \\
& \\
&\text{Let } m_{\text{OPTFF}} \text{ be the number of misses from the OPTFF algorithm} \\
&\text{Let } m_{A} \text{ be the number of misses from algorithm } A \\
&\text{We must show that } m_{\text{OPTFF}} \leq m_{A} \\
& \\
&\text{Assume the first point of disagreement between the two algorithms is at time } t \\
&\text{Meaning, the algorithms always evict the same page up until time } t-1 \\
& \\
&\text{Let:} \\
&x = \text{the page OPTFF evicts at time } t \\
&y = \text{the page $A$ evicts at time } t \\
&\text{Thus, } x \ne y \\
& \\
&\text{By definition of OPTFF, the next time $x$ is accessed must occur after the next time $y$ is accessed} \\
&\text{Assume we have $A'$ that is the same algorithm as $A$, but evicts $x$ when $A$ evicts $y$, and vice versa} \\
&\text{Let } m_{A'} \text{ be the number of misses from algorithm } A' \\
& \\
&\text{Since we know $y$ is accessed next before $x$, when $y$ is accessed $A$ misses, but $A'$ hits} \\
&\text{So, we know $A$ will have at least one miss} \\
&\text{Going forward, we do not know if $A'$ will miss, since $x$ may or may not be accessed} \\
&\text{We also do not know if $A$ will miss on $x$ later, as it still could be evicted} \\
&\text{This uncertainty means that } m_{A} \geq m_{A'} \\
&\text{This is a contradiction because we created $A'$ under the pretext that it will have no more misses than $A$ and will agree with OPTFF a step further than $A$} \\
&\text{So, no algorithm can be more optimal than OPTFF} \\
\end{aligned}
$$