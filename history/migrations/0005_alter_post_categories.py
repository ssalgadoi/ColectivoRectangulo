# Generated by Django 5.0.4 on 2024-04-24 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0004_post_descipcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(related_name='history_posts', to='history.category', verbose_name='Categorías'),
        ),
    ]