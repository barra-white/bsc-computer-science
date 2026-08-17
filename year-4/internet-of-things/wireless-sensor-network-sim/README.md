# Wireless Sensor Network Simulator

CA Assignment 4 — Internet of Things, Year 4, BSc Computer Science.

A simpy-based discrete-event simulation of a wireless sensor network. Sensor nodes self-organise into a rank-based multi-hop routing tree rooted at a sink, report temperature readings up the tree, and the sink maintains a routing table and sends acknowledgements back down. Includes a radio model with range, packet loss and channel selection.

## Usage

```bash
pip install -r requirements.txt
python3 sensor_network_sim.py
```
