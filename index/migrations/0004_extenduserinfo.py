# Generated by Django 4.0.5 on 2022-06-22 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_pubname_remove_book_public_alter_book_retail_price_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtendUserinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signature', models.CharField(help_text='自建签名', max_length=255, verbose_name='用户签名')),
                ('nickname', models.CharField(help_text='自建昵称', max_length=255, verbose_name='昵称')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='index.userinfo')),
            ],
        ),
    ]
