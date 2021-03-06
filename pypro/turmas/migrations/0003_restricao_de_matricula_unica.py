# Generated by Django 3.1.1 on 2020-09-16 01:15

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('turmas', '0002_criacao_matricula'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='matricula',
            options={'ordering': ['turma', 'data']},
        ),
        migrations.RenameField(
            model_name='matricula',
            old_name='matricula',
            new_name='turma',
        ),
        migrations.AlterUniqueTogether(
            name='matricula',
            unique_together={('usuario', 'turma')},
        ),
    ]
