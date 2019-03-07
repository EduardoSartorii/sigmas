# Generated by Django 2.1.7 on 2019-03-07 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20190306_1838'),
    ]

    operations = [
        migrations.CreateModel(
            name='comanda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_cliente', models.CharField(help_text='Informe o nome do cliente', max_length=300, verbose_name='Nome do cliente')),
                ('cpf', models.CharField(help_text='Informe a marca do produto', max_length=14, unique=True, verbose_name='Marca do produto')),
                ('comanda', models.CharField(help_text='Informe o número da comanda', max_length=8, verbose_name='Comanda')),
                ('mesas', models.CharField(help_text='Informe a mesa do cliente', max_length=3, verbose_name='Mesa')),
                ('narguiles', models.CharField(help_text='Informe a marca do produto', max_length=5, verbose_name='Narguile')),
                ('rua', models.CharField(help_text='Endereço do cliente', max_length=300, verbose_name='Endereço do cliente')),
                ('cidade', models.CharField(help_text='Informe a cidade do cliente', max_length=300, verbose_name='Cidade do Cliente')),
                ('estado', models.CharField(help_text='Informe a marca do produto', max_length=300, verbose_name='Marca do produto')),
                ('celular', models.CharField(help_text='Informe a marca do produto', max_length=300, verbose_name='Marca do produto')),
                ('email', models.CharField(help_text='Informe a marca do produto', max_length=300, verbose_name='Marca do produto')),
            ],
        ),
    ]