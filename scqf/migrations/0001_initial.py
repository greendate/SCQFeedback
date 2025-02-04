# Generated by Django 2.1.2 on 2020-02-09 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('desctiption', models.TextField()),
                ('image_url', models.CharField(default='https://i.imgur.com/FChk3bD.jpg', max_length=500)),
                ('grade', models.DecimalField(decimal_places=1, default=0.0, max_digits=1)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_id', models.IntegerField()),
                ('author', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('grade', models.DecimalField(decimal_places=1, default=0.0, max_digits=1)),
            ],
        ),
    ]
