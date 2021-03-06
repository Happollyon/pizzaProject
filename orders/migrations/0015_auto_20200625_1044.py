# Generated by Django 2.0.3 on 2020-06-25 09:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_auto_20200624_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_pasta',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pasta_client', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user_salad',
            name='item_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item', to='orders.Salad'),
        ),
        migrations.AlterField(
            model_name='user_salad',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salad_client', to=settings.AUTH_USER_MODEL),
        ),
    ]
