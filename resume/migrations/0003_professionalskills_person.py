# Generated by Django 3.1.2 on 2020-10-30 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_remove_professionalskills_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='professionalskills',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='resume.person'),
        ),
    ]
