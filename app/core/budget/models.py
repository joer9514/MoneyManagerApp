from django.db import models
from datetime import datetime
from core.user.models import User
from core.category.models import Category


class Budget(models.Model):
    """
    Model of the budget entity
    """
    id_budget = models.AutoField(primary_key=True, auto_created=True, unique=True, null=False, blank=False)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, verbose_name='User')
    id_category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=False,
                                    verbose_name='Category')
    name_budget = models.CharField(max_length=50, null=False, blank=False)
    month_budget = models.DateField(default=datetime.now, null=False, blank=False)
    value_budget = models.DecimalField(default=0.00, null=False, blank=False, max_digits=15, decimal_places=2)

    class Meta:
        """
        Special budget entity attributes
        """
        verbose_name = 'Budget'
        verbose_name_plural = 'Budgets'
        db_table = 'budget'
        ordering = ['id_budget']

    def __str__(self):
        """
        Representation of our budget object
        """
        return '{}'.format(self.name_budget)
