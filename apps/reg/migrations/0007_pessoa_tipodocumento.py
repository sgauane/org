# Generated by Django 3.2.15 on 2022-08-23 20:43

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0006_auto_20220823_2029'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoDocumento',
            fields=[
                ('data_actualizacao', models.DateField(auto_created=True, blank=True, null=True)),
                ('data_criacao', models.DateField(auto_created=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('activo', models.BooleanField(default=True)),
                ('designacao', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'Tipo de Documento',
                'verbose_name_plural': 'Tipos de Documento',
            },
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('data_actualizacao', models.DateField(auto_created=True, blank=True, null=True)),
                ('data_criacao', models.DateField(auto_created=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('activo', models.BooleanField(default=True)),
                ('nuit', models.CharField(max_length=9, null=True)),
                ('nome', models.CharField(max_length=500)),
                ('apelido', models.CharField(max_length=255, null=True)),
                ('nacionalidade', django_countries.fields.CountryField(max_length=2)),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1)),
                ('data_nascimento', models.DateField()),
                ('numero_documento', models.CharField(max_length=25)),
                ('foto', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='reg.imagem')),
                ('tipo_documento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reg.tipodocumento')),
            ],
            options={
                'verbose_name': 'Pessoa',
                'verbose_name_plural': 'Pessoas',
            },
        ),
    ]