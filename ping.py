import socket, time

host = "apple.com"
port = 80

times = []
for i in range(4):
    try:
        start = time.time()
        socket.create_connection((host, port)).close()
        rtt = (time.time() - start) * 1000
        times.append(rtt)
        print(f"Reply from {host}: time={rtt:.2f} ms")
    except:
        print("Request timed out")

if times:
    print("\nMin =", min(times), "ms")
    print("Max =", max(times), "ms")
    print("Avg =", sum(times) / len(times), "ms")