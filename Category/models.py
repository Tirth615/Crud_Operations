from django.db import models

# Create your models here.
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)
    category_description = models.TextField()
    def __str__(self):
        return '{} - {}'.format(self.category_name, self.category_description)

    def __as_dict(self):
        return {'category_id': self.category_id,
                'category_name': self.category_name,
                'category_description': self.category_description}
    class Meta:
       db_table = 'category'
