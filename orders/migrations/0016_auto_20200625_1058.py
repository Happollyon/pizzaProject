# Generated by Django 2.0.3 on 2020-06-25 09:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0015_auto_20200625_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_plater',
            name='item_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item', to='orders.Plater'),
        ),
        migrations.AlterField(
            model_name='user_plater',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plater_client', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user_sub',
            name='item_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item', to='orders.Subs'),
        ),
        migrations.AlterField(
            model_name='user_sub',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_client', to=settings.AUTH_USER_MODEL),
        ),
    ]