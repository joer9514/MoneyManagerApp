from django.db import models


class Category(models.Model):
    """
    Model of the category entity
    """
    id_category = models.AutoField(primary_key=True, auto_created=True, unique=True, null=False, blank=False)
    name_category = models.CharField(max_length=50, null=False, blank=False)
    description_category = models.CharField(max_length=250, null=True, blank=True)

    class Meta:
        """
        Special category entity attributes
        """
        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'
        db_table = 'category'
        ordering = ['id_category']

    def __str__(self):
        """
        Representation of our category object
        """
        return '{}'.format(self.name_category)
