# Generated by Django 3.1.2 on 2020-10-31 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_auto_20201030_2314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='areaofinterest',
            name='person',
        ),
        migrations.RemoveField(
            model_name='professionalskills',
            name='person',
        ),
        migrations.AddField(
            model_name='person',
            name='academic_detail',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='person',
            name='area_of_interest_detail',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='person',
            name='skillDetail',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='education',
            name='degree',
            field=models.CharField(choices=[('Phd', 'Phd'), ('Mtech/MA/MSc/MCom/MBA', 'Masters'), ('BE/Btech/BA/BSc/BCom', 'Masters'), ('12th', 'High School')], max_length=50),
        ),
        migrations.DeleteModel(
            name='Academics',
        ),
        migrations.DeleteModel(
            name='AreaOfInterest',
        ),
        migrations.DeleteModel(
            name='ProfessionalSkills',
        ),
    ]
