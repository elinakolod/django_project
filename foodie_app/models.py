from django.db import models

class Category(models.Model):
    # !!! enforces validation at the form and model validation level, but not automatically on .save().
    name = models.CharField(max_length=100, blank=False, null=False, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-name']
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

