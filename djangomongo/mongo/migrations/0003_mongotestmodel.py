# Generated by Django 3.0.5 on 2021-02-03 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mongo', '0002_delete_mongotestmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='MongoTestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('image', models.ImageField(upload_to='authors')),
            ],
            options={
                'db_table': 'mongo_table',
            },
        ),
    ]
