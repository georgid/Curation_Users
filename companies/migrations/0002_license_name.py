# Generated by Django 2.2.2 on 2019-06-12 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='license',
            name='name',
            field=models.CharField(default='Free Plan', max_length=50),
            preserve_default=False,
        ),
    ]
