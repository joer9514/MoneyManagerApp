from django.db import models
from datetime import datetime
from core.user.models import User
from core.movement.models import Movement


class Saving(models.Model):
    """
    Model of the saving entity
    """
    id_saving = models.AutoField(primary_key=True, auto_created=True, unique=True, null=False, blank=False)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, verbose_name='User')
    id_movement = models.ForeignKey(Movement, on_delete=models.CASCADE, null=False, blank=False,
                                    verbose_name='Movement')
    name_saving = models.CharField(max_length=50, null=False, blank=False)
    month_saving = models.DateField(default=datetime.now, null=False, blank=False)
    account_status = models.BooleanField(default=True, null=False, blank=False)
    account_balance = models.DecimalField(default=0.00, max_digits=15, decimal_places=2)

    class Meta:
        """
        Special saving entity attributes
        """
        verbose_name = 'Saving'
        verbose_name_plural = 'Savings'
        db_table = 'saving'
        ordering = ['id_saving']

    def __str__(self):
        """
        Representation of our saving object
        """
        return '{}'.format(self.name_saving)
