# Generated by Django 4.2.2 on 2023-07-08 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_admin_alter_prettynum_status_alter_userinfo_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='gender',
            field=models.SmallIntegerField(choices=[(2, '男'), (1, '女')], verbose_name='性别'),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.SmallIntegerField(choices=[(1, 'urgent'), (2, 'important'), (3, 'temporary')], default=3, verbose_name='level')),
                ('title', models.CharField(max_length=64, verbose_name='title')),
                ('detail', models.TextField(verbose_name='detail')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.admin', verbose_name='person in charge')),
            ],
        ),
    ]
