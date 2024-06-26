# Generated by Django 5.0.6 on 2024-05-12 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articlemodel',
            options={'ordering': ('-created',)},
        ),
        migrations.RenameField(
            model_name='articlemodel',
            old_name='Date',
            new_name='created',
        ),
        migrations.AddField(
            model_name='articlemodel',
            name='edited',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='articlemodel',
            name='status',
            field=models.CharField(choices=[('checking', 'Checking'), ('rejected', 'Rejected'), ('published', 'Published')], default='checking', max_length=15),
        ),
        migrations.AlterField(
            model_name='articlemodel',
            name='Body',
            field=models.TextField(max_length=10000),
        ),
    ]
