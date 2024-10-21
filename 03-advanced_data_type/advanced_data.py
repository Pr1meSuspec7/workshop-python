
# list
switches = ["sw1", "sw2", "sw3"]
routers = ["r1", "r2", "r3", "r4"]

print(switches[0])
print(routers[0])

switches.append("sw4")
print(switches)

routers.pop(3)
print(routers)

# dictionary
routers = {"r1": {"ip":"192.168.1.1", "mask":"255.255.255.0", "admin":True},
           "r2": {"ip":"192.168.2.1", "mask":"255.255.255.0", "admin":False}}

routers["r1"]
routers["r1"]["ip"]
print(f'r1: {routers["r1"]["ip"]} {routers["r1"]["mask"]}')

# nested data
devices = {"r1": {"interfaces": 
                  [{"Gi0/0/0": {"ip": "192.168.0.1","mask": "255.255.255.0"}},
                   {"Gi0/0/1": {"ip": "192.168.1.1","mask": "255.255.255.0"}},
                   {"Gi0/0/2": {"ip": "192.168.2.1","mask": "255.255.255.0"}}]},
           "r2": {"interfaces": 
                  [{"Gi0/0/0": {"ip": "172.16.0.1","mask": "255.255.255.0"}},
                   {"Gi0/0/1": {"ip": "172.16.1.1","mask": "255.255.255.0"}},
                   {"Gi0/0/2": {"ip": "172.16.2.1","mask": "255.255.255.0"}}]}}

print(devices["r1"]["interfaces"])
print(devices["r2"]["interfaces"])

for interface in devices["r1"]["interfaces"]:
    print(interface)

