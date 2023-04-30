from django.http import JsonResponse
import re
from .models import User
from django.core.mail import send_mail


def register(self, request):
    username = request.POST['username']
    name = request.POST['name']
    password = request.POST['password']
    mobile = request.POST['mobile']
    email = request.POST['email']
    address = request.POST['address']

    if not re.match("^[a-zA-Z]*$", username):
        return JsonResponse({"message": "Username should consist of only alphabets."}, status=400)

    if not re.match("^[a-zA-Z]*$", name):
        return JsonResponse({"message": "Name should consist of only alphabets."}, status=400)

    if not str(mobile).isdigit() or len(str(mobile)) != 10:
        return JsonResponse({"message": "Mobile number should be an integer with length 10."}, status=400)

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return JsonResponse({"message": "Email is not valid."}, status=400)

    if not re.match(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$", password):
        return JsonResponse({"message": "Password should contain at least 8 characters, including alphanumeric and special characters."}, status=400)

    user = User(
        username=username,
        password=password,
        email=email,
        name=name,
        mobile=mobile,
        address=address
    )
    user.save()

    user_id = User.objects.count() + 1

    subject = 'Welcome to our website'
    message = f'Hi {user.name}, thank you for joining our website!\n Username: {user.username} Password: {user.password}'
    from_email = 'admin@example.com'
    recipient_list = [user.email]
    send_mail(subject, message, from_email, recipient_list)

    return JsonResponse({'message': f'New user created with id {user_id}'})


def login(self, request):
    user = User.objects.get(
        username=request.POST['username'], password=request.POST['password'])
    return JsonResponse({'authenticated': False if user.DoesNotExist else True})


def getUsers(self, request):
    return JsonResponse({'users': User.objects.all()})
