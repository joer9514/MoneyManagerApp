from django.db import models


class User(models.Model):
    """
    Model of the user entity
    """
    id_user = models.AutoField(primary_key=True, auto_created=True, unique=True, null=False, blank=False)
    name_user = models.CharField(max_length=50, null=False, blank=False)
    surname_user = models.CharField(max_length=50, null=False, blank=False)
    email_user = models.CharField(max_length=100, unique=True, null=False, blank=False)
    password_user = models.CharField(max_length=50, null=False, blank=False)

    class Meta:
        """
        Special user entity attributes
        """
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        db_table = 'user'
        ordering = ['id_user']

    def __str__(self):
        """
        Representation of our user object
        """
        return '{} {}'.format(self.name_user, self.surname_user)
