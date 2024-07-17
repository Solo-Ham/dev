from django.core.mail import send_mail
from django.contrib.auth.models import User
import random
from .models import StoreOTP


def generateOtp():
    otp=""

    for x in range(6):
        otp = otp + str(random.randint(0, 9))
    return otp

    
def verify_user(email):
    user = User.objects.get(email=email)
    code = generateOtp()
    send_mail("Email Verification",
    (f'Dear {user.username} \n' 
    f'Your verification code is {code}. \n'
    'Thank you for signing up with us. '), 
    'The Question System <no-reply@yourorganization.com>',
    [user.email])
    newOtp = StoreOTP.objects.create(owner=user, code=code)
    newOtp.save()
    