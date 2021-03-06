# Generated by Django 3.1.7 on 2021-03-28 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiledesa', '0003_auto_20210325_0841'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kepaladesa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('slug', models.CharField(max_length=225)),
                ('reign', models.CharField(max_length=225)),
                ('address', models.CharField(max_length=1024)),
                ('biography', models.TextField()),
                ('is_featured', models.BooleanField(default=False)),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kepaladesas', to='profiledesa.aparatur')),
            ],
        ),
        migrations.DeleteModel(
            name='employee',
        ),
    ]
