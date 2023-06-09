# Generated by Django 3.2.15 on 2022-11-07 12:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reg', '0020_itempreco_items_itemsfavoritos'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Debito',
            fields=[
                ('data_actualizacao', models.DateField(auto_created=True, blank=True, null=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('activo', models.BooleanField(default=True)),
                ('data_criacao', models.DateField(auto_now_add=True)),
                ('referencia', models.CharField(max_length=11)),
                ('data_limite', models.DateField()),
                ('usuario_criacao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('valor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reg.itempreco')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Desconto',
            fields=[
                ('data_actualizacao', models.DateField(auto_created=True, blank=True, null=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('activo', models.BooleanField(default=True)),
                ('data_criacao', models.DateField(auto_now_add=True)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=7)),
                ('usuario_criacao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('data_actualizacao', models.DateField(auto_created=True, blank=True, null=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('activo', models.BooleanField(default=True)),
                ('data_criacao', models.DateField(auto_now_add=True)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=7)),
                ('debito', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='financas.debito')),
                ('desconto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='financas.desconto')),
                ('usuario_criacao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
