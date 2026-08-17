# Process Scheduler

CA Assignment 1 — Operating Systems 2 (CS2506), Year 2, BSc Computer Science.

A priority-based process scheduler for a parking-sensor system. Manages processes through initialising, ready and blocked queues, allocates PIDs (0 and 1 reserved for the kernel), preempts on interrupts, and drops to an idle state that polls the parking-sensor process. Shuts down when the car exceeds 20 km/h.

## Usage

```bash
python3 scheduler.py
```

Standard library only.
