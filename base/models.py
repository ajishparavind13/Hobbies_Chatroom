from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.contrib.auth.models import PermissionsMixin


    
class UserManager(BaseUserManager):
    def create_user(self,  email, password=None):
        if not email:
            raise ValueError('Users must have a username')

        user = self.model(
            email=email,
        )

        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password=None):

        if password is None:
            raise TypeError("Password should not be none")

        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user
    

class User(AbstractBaseUser,PermissionsMixin):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)
    username = models.CharField(max_length=12,unique=True,null=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    avatar = models.ImageField(null=True, default="avatar.svg")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()
    def __str__(self):
        return self.email
    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(
        User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]
