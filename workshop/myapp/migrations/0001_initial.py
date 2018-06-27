# Generated by Django 2.0.6 on 2018-06-26 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module_taught', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('institution', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('sex', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workshop_name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('venue', models.CharField(max_length=50)),
                ('workshop_sponsor', models.CharField(max_length=50)),
                ('workshop_logo', models.FileField(upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='instructor',
            name='person_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Person'),
        ),
        migrations.AddField(
            model_name='instructor',
            name='workshop_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Workshop'),
        ),
        migrations.AddField(
            model_name='attendee',
            name='person_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Person'),
        ),
        migrations.AddField(
            model_name='attendee',
            name='workshop_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Workshop'),
        ),
    ]
