from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

# CUSTOME USER MANAGER:
class UserManager(BaseUserManager):
    def create_user(
        self,
        email,
        name,
        password=None,
        password2=None,
    ):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self,
        email,
        password,
        name,
        **extra_fields,
    ):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            name=name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


# USER MODEL
class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="E-mail",
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    def __str__(self):
        return self.name


def File(instance,filename):
    return "image/{filename}".format(filename=filename)


class ActionUser(models.Model):
    user=models.ManyToManyField("User")
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    in_stock = models.IntegerField()
    price_asked = models.CharField(max_length=255)
    contact = models.BigIntegerField()
    location = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class ResourceUploader(models.Model):
    image = models.ImageField(upload_to=File,blank=True,null=True,)
    profile = models.ImageField(upload_to = File,blank=True)
    banner = models.ImageField(upload_to=File,blank=True)
    bio_description=models.TextField(max_length=500)