# Generated by Django 5.0.6 on 2024-05-31 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('UserId', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('FirstName', models.CharField(max_length=50)),
                ('LastName', models.CharField(max_length=50)),
                ('Phone', models.CharField(max_length=10)),
                ('Email', models.EmailField(max_length=100)),
            ],
        ),
    ]
