# Generated by Django 2.2.6 on 2019-10-30 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wine', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(null=True)),
                ('points', models.CharField(max_length=20, null=True)),
                ('price', models.CharField(max_length=20, null=True)),
                ('province', models.CharField(max_length=100, null=True)),
                ('region', models.CharField(max_length=150, null=True)),
                ('taster_name', models.CharField(max_length=120, null=True)),
                ('title', models.CharField(max_length=200, null=True)),
                ('variety', models.CharField(max_length=150, null=True)),
                ('winery', models.CharField(max_length=150, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
