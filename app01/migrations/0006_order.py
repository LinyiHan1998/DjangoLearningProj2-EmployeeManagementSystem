# Generated by Django 4.2.2 on 2023-07-09 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_alter_userinfo_gender_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Oid', models.CharField(max_length=64, verbose_name='order No.')),
                ('title', models.CharField(max_length=32, verbose_name='title')),
                ('price', models.IntegerField(verbose_name='price')),
                ('status', models.SmallIntegerField(choices=[(1, 'unpaid'), (2, 'paid')], default=1, verbose_name='status')),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.admin', verbose_name='Administrator')),
            ],
        ),
    ]
