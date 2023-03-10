# Generated by Django 4.1.3 on 2023-01-19 06:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Reccomend', '0004_movie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekends', models.CharField(max_length=100)),
                ('weekdays', models.CharField(max_length=100)),
                ('tired', models.CharField(max_length=100)),
                ('happy', models.CharField(max_length=100)),
                ('sad', models.CharField(max_length=100)),
                ('inspiration', models.CharField(max_length=100)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
