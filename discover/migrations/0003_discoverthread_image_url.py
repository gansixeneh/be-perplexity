# Generated by Django 4.2.9 on 2024-01-31 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discover', '0002_source_discoverthread_sources'),
    ]

    operations = [
        migrations.AddField(
            model_name='discoverthread',
            name='image_url',
            field=models.URLField(default='https://www.perplexity.ai/_next/image?url=https%3A%2F%2Fpplx-res.cloudinary.com%2Fimage%2Ffetch%2Fs--7rBGk--z--%2Ft_thumbnail%2Fhttps%3A%2F%2Fwww.creativeboom.com%2Fupload%2Farticles%2Fcd%2Fcd1b08cd59d26ad43924fa2df8ed000840ce2136_1280.jpg&w=640&q=75'),
            preserve_default=False,
        ),
    ]
