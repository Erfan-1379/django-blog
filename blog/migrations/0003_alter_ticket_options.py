# Generated by Django 4.2.2 on 2023-06-14 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_ticket'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ticket',
            options={'verbose_name': 'تیکت', 'verbose_name_plural': 'تیکت ها'},
        ),
    ]
