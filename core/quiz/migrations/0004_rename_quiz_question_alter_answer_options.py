# Generated by Django 5.1.4 on 2024-12-07 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_answer_is_correct'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Quiz',
            new_name='Question',
        ),
        migrations.AlterModelOptions(
            name='answer',
            options={'ordering': ['-created']},
        ),
    ]
