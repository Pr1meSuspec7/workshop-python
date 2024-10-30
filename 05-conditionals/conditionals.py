response = 200

if response == 200:
    print("OK")
elif response == 300:
    print("Redirection")
elif response == 400:
    print("Client Error")
elif response == 500:
    print("Server Error")
else:
    print("Unknown Error")


if response >= 200 and response <= 299:
    print("OK")
elif response >= 300 and response <= 399:
    print("Redirection")
elif response >= 400 and response <= 499:
    print("Client Error")
elif response >= 500 and response <= 599:
    print("Server Error")
else:
    print("Unknown Error")

# Identity Operators
# questi due oggetti si trovano in posizioni di memoria differenti
x = ["router1", "router2"]
y = ["router1", "router2"]
# z punta alla posizione di memoria dove si trova x
z = x

z is x
x is y

# Membership Operators
x = ["router1", "router2"]
"router1" in x
"router3" in x
"router3" not in x
