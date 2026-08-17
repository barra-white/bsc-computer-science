# Memory Management

CA Assignment 2 — Operating Systems 2 (CS2506), Year 2, BSc Computer Science.

Two memory management components: a buddy-system allocator that splits and merges power-of-two blocks to satisfy allocation requests, and a FIFO page-replacement queue with page-fault detection and main-memory load/unload.

## Files

| File | Description |
|------|-------------|
| `buddy_system.py` | Buddy system allocator — `Block`, `Request` and `BuddySystem` classes |
| `fifo.py` | FIFO replacement queue and `Page` class |
| `main.py` | Test driver for both components |

## Usage

```bash
python3 main.py
```

Standard library only.
