# Shortest Path — Dijkstra

CA Assignment 2 — Algorithms & Data Structures 2 (CS2516), Year 2, BSc Computer Science.

Implements Dijkstra's shortest-path algorithm over a graph ADT, comparing two adaptable priority queue implementations — an unsorted list and a binary heap. Includes a route-map variant that reads GPS-coordinate graphs.

## Files

| File | Description |
|------|-------------|
| `graph.py` | Graph ADT (vertices, edges, DFS/BFS) + Dijkstra over a plain weighted graph |
| `route_map.py` | Route-map variant — vertices carry GPS coordinates, edges carry travel times |
| `apq.py` | Adaptable priority queues: `UnsortedAPQ` (list) and `HeapAPQ` (binary heap) |
| `route_apq.py` | APQ variant for the route map |
| `stacks.py` | Array-based stack used by the DFS traversal |
| `simplegraph1.txt` / `simplegraph2.txt` / `simpleroute.txt` | Test graphs |

## Usage

```bash
python3 graph.py      # runs Dijkstra on simplegraph2.txt
python3 route_map.py  # runs Dijkstra on simpleroute.txt
```
