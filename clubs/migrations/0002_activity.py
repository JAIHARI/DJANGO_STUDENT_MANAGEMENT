# Generated by Django 2.1.7 on 2019-03-19 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '__first__'),
        ('clubs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_no', models.CharField(max_length=4)),
                ('date', models.DateField()),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clubs.Club')),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teachers.Teacher')),
            ],
        ),
    ]