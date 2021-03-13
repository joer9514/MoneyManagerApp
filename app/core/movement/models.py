from django.db import models
from datetime import datetime
from core.budget.models import Budget


class Movement(models.Model):
    """
    Model of the movement entity
    """
    id_movement = models.AutoField(primary_key=True, auto_created=True, unique=True, null=False, blank=False)
    id_budget = models.ForeignKey(Budget, on_delete=models.CASCADE, null=False, blank=False,
                                  verbose_name='Budget')
    name_movement = models.CharField(max_length=50, null=False, blank=False)
    month_movement = models.DateField(default=datetime.now, null=False, blank=False)
    value_movement = models.DecimalField(default=0.00, null=False, blank=False, max_digits=15, decimal_places=2)
    description_movement = models.CharField(max_length=250, null=True, blank=True)

    class Meta:
        """
        Special movement entity attributes
        """
        verbose_name = 'Movement'
        verbose_name_plural = 'Movements'
        db_table = 'movement'
        ordering = ['id_movement']

    def __str__(self):
        """
        Representation of our movement object
        """
        return '{}'.format(self.name_movement)
