# Generated by Django 4.1.5 on 2023-01-30 00:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0002_rename_project_polls"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Polls",
            new_name="Poll",
        ),
    ]