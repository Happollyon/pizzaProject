# Generated by Django 2.0.3 on 2020-06-27 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0018_auto_20200625_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_reg_pizza',
            name='confirm',
            field=models.BooleanField(default=0),
        ),
    ]