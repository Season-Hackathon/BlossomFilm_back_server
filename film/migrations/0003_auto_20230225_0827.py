# Generated by Django 3.2.18 on 2023-02-24 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0002_auto_20230224_2244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='frame',
            name='film',
        ),
        migrations.AddField(
            model_name='frame',
            name='height',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='frame',
            name='width',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='myphotoframe',
            name='title',
            field=models.CharField(blank=True, default='', max_length=512),
        ),
        migrations.DeleteModel(
            name='Film',
        ),
    ]
