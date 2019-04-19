# Generated by Django 2.1.4 on 2019-04-19 03:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plantjournal', '0005_auto_20190418_2234'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='growthinstance',
            options={'ordering': ['-growth_instance_date', 'plant', 'growth_type']},
        ),
        migrations.AlterModelOptions(
            name='note',
            options={'ordering': ['-note_date', 'note_name']},
        ),
        migrations.AlterUniqueTogether(
            name='growthinstance',
            unique_together={('plant', 'growth_type', 'growth_instance_date')},
        ),
    ]
