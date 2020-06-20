# Generated by Django 2.0.3 on 2020-06-18 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20200618_1117'),
    ]

    operations = [
        migrations.CreateModel(
            name='Salad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='teste', max_length=64)),
                ('print', models.FloatField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='pasta',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]
