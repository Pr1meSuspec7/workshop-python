# String Concatenation
ip_netmask = "192.168.0.1 " + "255.255.255.0"
print(ip_netmask)

ip = "192.168.0.1"
nm = "255.255.255.0"
print(ip + nm)
print(ip + ' ' + nm)

ip + 5

# String Splitting
ip.split(".")

# Formatting and Templating 
print('The ip address is {} and netmask is {}.'.format(ip, nm))
print(f'The ip address is {ip} and netmask is {nm}.')
print(f'The ip address is {ip} \nand netmask is {nm}.')

