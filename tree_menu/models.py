from django.db import models
"""
ЗАПОЛНИТЬ ДОКСТРИНГ ПОЗЖЕ
"""


class Node(models.Model):
    symbols = (
        ('└', '└'),
        ('├', '├'),
        ('─', '─'),
        ('│', '│'),
    )
    
    name = models.CharField(max_length=72, default='')
    parent = models.ForeignKey(to='Node', blank=True, on_delete=models.CASCADE,
                               null=True)
    url = models.URLField(default='/')
    related_menu = models.ForeignKey(to='Node', blank=True, on_delete=models.CASCADE,
                                     null=True, related_name='menu')
    symbol = models.CharField(choices=symbols, default='└', max_length=1)

    def __str__(self) -> str:
        return self.name