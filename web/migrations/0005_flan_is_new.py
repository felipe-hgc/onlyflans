# Generated by Django 3.2.4 on 2022-06-30 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_contactform'),
    ]

    operations = [
        migrations.AddField(
            model_name='flan',
            name='is_new',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]