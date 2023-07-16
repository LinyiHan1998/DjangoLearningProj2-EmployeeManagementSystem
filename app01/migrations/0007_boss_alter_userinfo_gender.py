# Generated by Django 4.2.2 on 2023-07-15 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0006_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Name')),
                ('age', models.IntegerField(verbose_name='Age')),
                ('image', models.CharField(max_length=128, verbose_name='Avatar')),
            ],
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='gender',
            field=models.SmallIntegerField(choices=[(1, '女'), (2, '男')], verbose_name='性别'),
        ),
    ]
