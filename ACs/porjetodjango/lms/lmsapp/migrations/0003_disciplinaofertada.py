# Generated by Django 2.1 on 2018-09-11 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmsapp', '0002_disciplina'),
    ]

    operations = [
        migrations.CreateModel(
            name='DisciplinaOfertada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curso', models.TextField(max_length=255)),
                ('turma', models.TextField(max_length=5)),
                ('ano', models.IntegerField()),
                ('semestre', models.IntegerField()),
                ('professor', models.IntegerField()),
                ('disciplina', models.IntegerField()),
            ],
        ),
    ]
