# Generated by Django 3.2.15 on 2022-10-26 12:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0019_cargo'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0002_auto_20221025_1022'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sobrenos',
            old_name='texto',
            new_name='descricao',
        ),
        migrations.RenameField(
            model_name='sobrenos',
            old_name='titulo',
            new_name='missao',
        ),
        migrations.AddField(
            model_name='sobrenos',
            name='visao',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sobrenos',
            name='organizacao',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reg.organizacao'),
        ),
        migrations.CreateModel(
            name='Valores',
            fields=[
                ('data_actualizacao', models.DateField(auto_created=True, blank=True, null=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('activo', models.BooleanField(default=True)),
                ('data_criacao', models.DateField(auto_now_add=True)),
                ('designacao', models.CharField(max_length=255)),
                ('organizacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reg.organizacao')),
                ('usuario_criacao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]