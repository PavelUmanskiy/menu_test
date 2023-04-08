from django.db import models
"""
ЗАПОЛНИТЬ ДОКСТРИНГ ПОЗЖЕ
"""
class Node(models.Model):
    name = models.CharField(max_length=72, default='')
    children = models.ManyToManyField(to='Node', blank=True)


class Menu(models.Model):
    name = models.CharField(max_length=72, default='Default Menu Name')
    root_node = models.ForeignKey(to='Node', on_delete=models.SET_NULL,
                                  null=True)