# Generated by Django 3.1.1 on 2020-09-16 01:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('turmas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('matricula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='turmas.turma')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                              to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='turma',
            name='alunos',
            field=models.ManyToManyField(through='turmas.Matricula', to=settings.AUTH_USER_MODEL),
        ),
    ]
