
response = {"status_code": 200, "response_reason": "OK", "response_text": "Testo ricevuto dalla prima chiamata API"}

assertion_message = f'{response["status_code"]} -> {response["response_reason"]}'
assert response["status_code"] == 200, assertion_message
print('')
print(response["response_text"])
print('')

print('##############################\n')

response2 = {"status_code": 401, "response_reason": "Unauthorized", "response_text": "Testo ricevuto dalla seconda chiamata API"}

assertion_message2 = f'{response2["status_code"]} -> {response2["response_reason"]}'
assert response2["status_code"] == 200, assertion_message2
print('')
print(response2["response_text"])
print('')
