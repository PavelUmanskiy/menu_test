from django.db import models
"""
ЗАПОЛНИТЬ ДОКСТРИНГ ПОЗЖЕ
"""
class Node(models.Model):
    name = models.CharField(max_length=72, default='')
    parent = models.ForeignKey(to='Node', blank=True, on_delete=models.CASCADE, null=True)
    url = models.URLField(default='/')

    def __str__(self) -> str:
        return self.name