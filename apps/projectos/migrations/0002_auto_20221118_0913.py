# Generated by Django 3.2.15 on 2022-11-18 09:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0020_itempreco_items_itemsfavoritos'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projectos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projecto',
            name='imagem',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reg.imagem'),
        ),
        migrations.CreateModel(
            name='ProjectoGaleria',
            fields=[
                ('data_actualizacao', models.DateField(auto_created=True, blank=True, null=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('activo', models.BooleanField(default=True)),
                ('data_criacao', models.DateField(auto_now_add=True)),
                ('descricao', models.CharField(blank=True, max_length=500, null=True)),
                ('imagem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reg.imagem')),
                ('projecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectos.projecto')),
                ('usuario_criacao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]