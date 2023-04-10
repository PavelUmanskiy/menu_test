# Generated by Django 4.1.5 on 2023-04-10 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tree_menu', '0003_node_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='related_menu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='menu', to='tree_menu.node'),
        ),
    ]