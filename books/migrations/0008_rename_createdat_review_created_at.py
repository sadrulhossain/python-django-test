# Generated by Django 4.1.7 on 2023-03-16 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_remove_review_bookid_review_book'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='createdAt',
            new_name='created_at',
        ),
    ]
