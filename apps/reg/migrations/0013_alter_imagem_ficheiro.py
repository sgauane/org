# Generated by Django 3.2.15 on 2022-08-30 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0012_auto_20220829_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagem',
            name='ficheiro',
            field=models.ImageField(null=True, upload_to='imagens'),
        ),
    ]
