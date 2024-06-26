# Generated by Django 4.2.13 on 2024-05-12 18:11

from django.conf import settings
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shareapp', '0004_alter_folder_uid'),
    ]

    operations = [
        migrations.CreateModel(
            name='SignedUrl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField(validators=[django.core.validators.URLValidator()])),
                ('expiry_in', models.IntegerField(default=600, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('allowed_users', models.ManyToManyField(related_name='signed_urls', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
