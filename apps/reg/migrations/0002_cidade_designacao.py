# Generated by Django 3.2.15 on 2022-08-23 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cidade',
            name='designacao',
            field=models.CharField(default='', max_length=255),
        ),
    ]
