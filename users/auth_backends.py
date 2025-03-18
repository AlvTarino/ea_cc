from django.contrib.auth.backends import ModelBackend
from users.models import CustomUser


class EmailAuthBackend(ModelBackend):
    """Authenticate using email instead of username."""
    
    def authenticate(self, request, username=None, password=None, **kwargs):
        print(f"Authenticating user: {username}")  # Debug log
        try:
            user = CustomUser.objects.get(email=username) 
            print(f"User found: {user}")  # Debug log
            
            if user.check_password(password):
                print("Password is correct")  # Debug log
                return user
            else:
                print("Incorrect password")  # Debug log
                return None
        except CustomUser.DoesNotExist:
            print("User does not exist")  # Debug log
            return None
