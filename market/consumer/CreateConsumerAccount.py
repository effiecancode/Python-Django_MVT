from django.http import HttpResponse
import json
from .models import ConsumerUser


class CreateConsumerAccount:
  def __init__(self):
    pass

  def save_client_account(self, username, email, password1):
    try:
      email = email.strip()
      email = email.replace(' ', '')
      username = username.strip()
      username = username.replace(' ', '')
      user_exists = ConsumerUser.objects.filter(email=email).exists()
      if user_exists:
        data = {"status": "fail", "data": {"message": "User already exists"}}
        return HttpResponse(json.dumps(data), content_type='text/json')
      user = ConsumerUser(
        username=username,
        email=email,
      )
      print(user)
      user.set_password(password1)
      user.save()
      return HttpResponse(json.dumps({'status': 'success', 'data': {'message': str(email)}, 'user': str(user)}))
    except Exception as e:
      return HttpResponse(json.dumps({'status': 'failed', 'data': {'message': str(e)}}))