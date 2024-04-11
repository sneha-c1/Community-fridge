# Generated by Django 5.0 on 2024-03-21 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communityapp', '0006_requestitem_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestitem',
            name='Status',
            field=models.CharField(choices=[('pending', 'Pending'), ('accept', 'accept'), ('reject', 'reject')], default='pending', max_length=30),
        ),
    ]