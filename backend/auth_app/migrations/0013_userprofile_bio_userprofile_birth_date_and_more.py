# Generated by Django 5.1.1 on 2024-09-22 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0012_remove_userprofile_email_remove_userprofile_password_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='location',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
