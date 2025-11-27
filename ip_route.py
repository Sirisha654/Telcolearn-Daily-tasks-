import subprocess
import json

output = subprocess.check_output(["ip", "route"]).decode().strip().split("\n")

routes = []
for line in output:
    parts = line.split()
    route = {
        "destination": parts[0],
        "via": parts[parts.index("via") + 1] if "via" in parts else None,
        "dev": parts[parts.index("dev") + 1] if "dev" in parts else None,
        "src": parts[parts.index("src") + 1] if "src" in parts else None
    }
    routes.append(route)

with open("routing_table.json", "w") as f:
    json.dump(routes, f, indent=4)

print("Routing table saved to routing_table.json")
