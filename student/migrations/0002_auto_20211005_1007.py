# Generated by Django 3.2.4 on 2021-10-05 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('address', models.TextField()),
            ],
            options={
                'unique_together': {('name', 'address')},
            },
        ),
        migrations.AddField(
            model_name='student',
            name='phone',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('age', models.IntegerField()),
                ('qualification', models.CharField(max_length=256)),
                ('subjects', models.JSONField(default=list)),
                ('role', models.CharField(choices=[('teacher', 'teacher'), ('head_master', 'head_master')], default='teacher', max_length=256)),
                ('address', models.TextField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=10, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('school', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teachers', to='student.school')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='school',
            field=models.ManyToManyField(related_name='students', to='student.School'),
        ),
    ]
