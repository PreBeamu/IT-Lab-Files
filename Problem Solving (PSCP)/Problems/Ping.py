"""Docstring"""
def main():
    """Ping... Pong... Ping.. Damn.. My WiFi is so slow!?"""
    input()
    input()
    ping = input()
    replies = {}
    for i in range(4):
        replies[i] = input() + " "
    # Useful Data
    var = {
        "ping_address": "", "dots": 0,
        "lost": 0, "received": 0,
        "min_time": float('inf'), "max_time": 0, "avg_time": 0
    }
    # Find target Address :3
    if "[" in ping and "]" in ping:
        var["ping_address"] = ping.split("[")[1].split("]")[0]
    else:
        ping_length = len(ping)
        for i in range(ping_length):
            if ping[i] == "]":
                break
            if ping[i] == " " and var["dots"] >= 3:
                break
            if ping[i].isdigit() \
                and (ping[i-1].isnumeric() or ping[i-1] in ":[]. ") \
                and (ping[i+1].isnumeric() or ping[i+1] in ":[]. "):
                var["ping_address"] += ping[i]
            elif (ping[i] in ":[]. " and var["ping_address"]):
                var["dots"] += ping[i] == "."
                var["ping_address"] += ping[i]

    # Find Lost and Received ( UwU )
    def find_packet():
        sum_time = 0
        count_time = 0
        for _, i in replies.items():
            if "Reply" in i:
                var["received"] += 1
            else:
                var["lost"] += 1
            if "time=" in i:
                for part in i.split():
                    if "time=" in part:
                        timeu = int(part.replace("time=", "").replace("ms", ""))
                        var["min_time"] = min(var["min_time"], timeu)
                        var["max_time"] = max(var["max_time"], timeu)
                        sum_time += timeu
                        count_time += 1
        if count_time > 0:
            var["avg_time"] = sum_time / count_time
        else:
            var["min_time"] = var["max_time"] = var["avg_time"] = 0
    find_packet()

    print("Ping statistics for", var["ping_address"] + ":")
    print(f"    Packets: Sent = 4, Received = {var['received']},"
          + f" Lost = {var['lost']} ({int((var['lost']/4)*100)}% loss),")
    if var["lost"] != 4:
        print("Approximate round trip times in milli-seconds:")
        print(f"    Minimum = {var['min_time']}ms, Maximum = {var['max_time']}ms,"
              + f" Average = {int(var['avg_time'])}ms")
main()
