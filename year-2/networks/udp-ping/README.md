# UDP Ping

Networks (CS2505), Year 2, BSc Computer Science — UDP ping client/server lab.

A UDP client pings a server 10 times and measures round-trip time; the server randomly drops ~30% of packets to simulate loss and echoes the rest back.

## Usage

Run the server first, then the client, and enter the same port for both:

```bash
python3 udp_ping_server.py   # enter a port when prompted
python3 udp_ping_client.py   # enter the same port
```

Both scripts use only the Python standard library.
