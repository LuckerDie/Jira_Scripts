import base64


def create_token(login, password):
    encoded = base64.b64encode(f"{login}:{password}".encode('utf-8'))
    list_s = ["b'", "'"]
    token = str(encoded)
    for word in list_s:
        token = token.replace(word, "")

    return token
