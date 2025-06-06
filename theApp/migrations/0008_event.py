# Generated by Django 5.2 on 2025-05-08 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theApp', '0007_alter_book_publication_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=255)),
                ('start_datetime', models.DateTimeField()),
                ('end_datetime', models.DateTimeField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='event_images/')),
                ('nbr_reservations', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('event_type', models.CharField(choices=[('BOOK_READING', 'Book Reading'), ('WORKSHOP', 'Workshop'), ('AUTHOR_VISIT', 'Author Visit'), ('EXHIBITION', 'Exhibition'), ('OTHER', 'Other')], default='OTHER', max_length=20)),
                ('is_public', models.BooleanField(default=True)),
            ],
        ),
    ]
