# Generated by Django 3.2.15 on 2022-08-29 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0011_alter_endereco_data_fim'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imagem',
            options={'verbose_name': 'Foto', 'verbose_name_plural': 'Fotos'},
        ),
        migrations.AlterField(
            model_name='imagem',
            name='descricao',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]