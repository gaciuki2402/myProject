# Generated by Django 4.0.1 on 2022-03-24 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_manufacturer_car'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('shirt_size', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=1)),
            ],
        ),
        migrations.RemoveField(
            model_name='person',
            name='shirt_size',
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=120),
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField()),
                ('invite_reason', models.CharField(max_length=86)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.group')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.person')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='members',
            field=models.ManyToManyField(through='polls.Membership', to='polls.Person'),
        ),
    ]
