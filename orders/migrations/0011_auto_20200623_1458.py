# Generated by Django 2.0.3 on 2020-06-23 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_user_reg_pizza_user_sici_pizza'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_reg_pizza',
            name='item_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user_reg_pizza',
            name='option_1',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user_reg_pizza',
            name='option_2',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user_reg_pizza',
            name='option_3',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user_reg_pizza',
            name='option_4',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user_reg_pizza',
            name='option_5',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user_reg_pizza',
            name='user_id',
            field=models.IntegerField(default=0),
        ),
    ]