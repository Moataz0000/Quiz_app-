# Generated by Django 5.1.4 on 2024-12-07 13:42

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('question', models.CharField(help_text="be sure the question don'n has over 1000 charachter", max_length=1000, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('answer', models.TextField(max_length=2000)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('quesiton', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='quiz.quiz')),
            ],
        ),
    ]