from requests import Session

def get_user_name(user):
    """Given a Github user, gets it name"""
    session = Session()
    url = f"https://api.github.com/users/{user}"
    response = session.get(url)
    json_response = response.json()
    return json_response["name"]
