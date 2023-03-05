# Generated by Django 3.2.6 on 2023-03-01 13:00

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=200)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('role', models.CharField(choices=[('USR', 'user'), ('ADM', 'Admin')], default='USR', max_length=3)),
                ('image', models.ImageField(blank=True, null=True, upload_to='avatars')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
