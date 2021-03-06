# Generated by Django 2.1.4 on 2019-04-19 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantjournal', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fertilizer',
            options={'ordering': ['fertilizer_freq', 'fertilizer_type']},
        ),
        migrations.AlterModelOptions(
            name='humidity',
            options={'ordering': ['humidity_level'], 'verbose_name_plural': 'humidities'},
        ),
        migrations.AlterModelOptions(
            name='light',
            options={'ordering': ['light_type']},
        ),
        migrations.AlterModelOptions(
            name='soil',
            options={'ordering': ['soil_type']},
        ),
        migrations.AlterModelOptions(
            name='toxicity',
            options={'ordering': ['toxicity_type'], 'verbose_name_plural': 'toxicities'},
        ),
        migrations.AlterModelOptions(
            name='water',
            options={'ordering': ['water_freq', 'water_type']},
        ),
        migrations.RemoveField(
            model_name='toxicity',
            name='toxicity_description',
        ),
        migrations.AddField(
            model_name='toxicity',
            name='toxicity_type',
            field=models.CharField(default='', max_length=45, unique=True),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='fertilizer',
            unique_together={('fertilizer_freq', 'fertilizer_type')},
        ),
        migrations.AlterUniqueTogether(
            name='water',
            unique_together={('water_freq', 'water_type')},
        ),
    ]
