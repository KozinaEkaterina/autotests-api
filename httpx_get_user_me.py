import httpx

EMAIL = ""
PASSWORD = ""

def login(email: str, password: str) -> dict[str, dict[str, str]]:
    payload = {
        "email": email,
        "password": password,
    }
    response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=payload)
    response.raise_for_status()
    response_data = response.json()
    return response_data

def get_user_data(bearer_token: str) -> dict[str, dict[str, dict[str, str]]]:
    headers = {"Authorization": f"Bearer {bearer_token}"}
    response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)
    response.raise_for_status()
    user_data = response.json()
    print(f"User data: {user_data}")
    print(f"Status code: {response.status_code}")
    return user_data

with httpx.Client() as client:
    token = login(EMAIL, PASSWORD)["token"]["accessToken"]
    get_user_data(token)


