#################### For loop ####################

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

#################### While loop ####################

while True:
    long_password = input('Insert a long password: ')
    if len(long_password) >= 10:
        print('Great!!!')
        break
    else:
        print('Must be longer than 10 characters.')
