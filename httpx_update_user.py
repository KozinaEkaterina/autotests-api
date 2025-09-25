import httpx

from tools.fakers import fake


create_user_payload = {
    "email": fake.email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
}
response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)
response.raise_for_status()
created_user_data = response.json()
print('Create user data:', created_user_data)


login_payload = {
    "email": create_user_payload['email'],
    "password": create_user_payload['password'],
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response.raise_for_status()
login_response_data = login_response.json()
print('Login data:', login_response_data)


update_user_payload = {
    "email": fake.email(),
    "lastName": fake.last_name(),
    "firstName": fake.first_name(),
    "middleName": fake.middle_name(),
}
authorization_headers = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}
response = httpx.patch(
    f"http://localhost:8000/api/v1/users/{created_user_data['user']['id']}",
    json=update_user_payload,
    headers=authorization_headers,
)
response.raise_for_status()
updated_user_data = response.json()
print('Update user data:', updated_user_data)