# Generated by Django 4.0.1 on 2022-01-26 08:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('NewsApp', '0007_alter_news_pub_date_alter_sportnews_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2022, 1, 26, 8, 56, 53, 666730, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='sportnews',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2022, 1, 26, 8, 56, 53, 683840, tzinfo=utc)),
        ),
    ]
