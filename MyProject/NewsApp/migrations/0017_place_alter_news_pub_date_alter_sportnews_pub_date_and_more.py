# Generated by Django 4.0.1 on 2022-02-11 09:15

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('NewsApp', '0016_remove_restaurant_place_alter_news_pub_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='news',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2022, 2, 11, 9, 15, 57, 257982, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='sportnews',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2022, 2, 11, 9, 15, 57, 275793, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('place', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='NewsApp.place')),
                ('serves_hot_dogs', models.BooleanField(default=False)),
                ('serves_pizza', models.BooleanField(default=False)),
            ],
        ),
    ]