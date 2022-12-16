# Generated by Django 3.2.15 on 2022-10-25 06:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reg', '0019_cargo'),
    ]

    operations = [
        migrations.CreateModel(
            name='SobreNos',
            fields=[
                ('data_actualizacao', models.DateField(auto_created=True, blank=True, null=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('activo', models.BooleanField(default=True)),
                ('data_criacao', models.DateField(auto_now_add=True)),
                ('titulo', models.CharField(max_length=255)),
                ('texto', models.CharField(max_length=1000)),
                ('organizacao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reg.organizacao')),
                ('usuario_criacao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Perguntas',
            fields=[
                ('data_actualizacao', models.DateField(auto_created=True, blank=True, null=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('activo', models.BooleanField(default=True)),
                ('data_criacao', models.DateField(auto_now_add=True)),
                ('nome', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('titulo', models.CharField(max_length=255)),
                ('mensagem', models.CharField(max_length=1000)),
                ('resposta', models.CharField(max_length=1000)),
                ('usuario_criacao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'organizacao',
                'verbose_name_plural': 'organizacacoes',
            },
        ),
        migrations.CreateModel(
            name='Equipa',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='reg.pessoa')),
                ('descricao', models.CharField(max_length=500)),
                ('cargo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reg.cargo')),
            ],
            options={
                'abstract': False,
            },
            bases=('reg.pessoa',),
        ),
    ]