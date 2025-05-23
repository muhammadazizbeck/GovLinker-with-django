# Generated by Django 5.2 on 2025-04-14 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suggestion', '0002_alter_complaintsuggestion_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default=1, upload_to='category_images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='text',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
