from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from users.managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class User(AbstractBaseUser):
    class UserRoles(models.TextChoices):
        ADMIN = 'admin'
        USER = 'user'

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', "role"]

    phone_regex = RegexValidator(regex=r'^\+\d{8,15}$',
                        message="Phone number format: '+12345678900'. 8 to 15 digits allowed.")

    email = models.EmailField(max_length=254, unique=True)
    phone = models.CharField(validators=[phone_regex], max_length=17, null=True, blank=True)
    role = UserRoles.choices
    first_name = models.CharField(max_length=64, null=True, blank=True)
    last_name = models.CharField(max_length=64, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    objects = UserManager()

    @property
    def is_admin(self):
        return self.role == self.UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == self.UserRoles.USER

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    # def has_perm(self, perm, obj=None):
    #     return self.is_admin
    #
    # def has_module_perms(self, app_label):
    #     return self.is_admin

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['email']

