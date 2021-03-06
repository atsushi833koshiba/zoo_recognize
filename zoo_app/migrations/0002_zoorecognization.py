# Generated by Django 2.0.10 on 2019-01-24 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zoo_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZooRecognization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='unknown', max_length=128, null=True)),
                ('animal_id', models.IntegerField(default=0)),
                ('score', models.FloatField(default=0.0, null=True, verbose_name='score of the classification')),
            ],
        ),
    ]
