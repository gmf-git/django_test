def jwt_response_payload_handler(token, user, request):
    data = {
        'name': user.name,
        'username': user.username,
        'token': token
    }
    return data
