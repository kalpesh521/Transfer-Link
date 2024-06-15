# Generated by Django 4.2.13 on 2024-05-12 15:12

from django.db import migrations, models
import shareapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('shareapp', '0003_alter_folder_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='uid',
            field=models.UUIDField(default=shareapp.models.unique_id, editable=False, primary_key=True, serialize=False),
        ),
    ]
