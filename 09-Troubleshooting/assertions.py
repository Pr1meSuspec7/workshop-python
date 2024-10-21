
response = {"status_code": 200, "response_reason": "OK", "response_text": "Testo ricevuto dalla prima chiama API"}

assertion_message = f'{response["status_code"]} -> {response["response_reason"]}'
assert response["status_code"] == 200, assertion_message
print('')
print(response["response_text"])
print('')


response2 = {"status_code": 401, "response_reason": "Unauthorized", "response_text": "Testo ricevuto dalla seconda chiama API"}
assert response2["status_code"] == 200, assertion_message
print('')
print(response2["response_text"])
print('')
