# Generated by Django 5.0.4 on 2024-04-24 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0004_post_descipcion'),
        ('news', '0003_delete_category_alter_post_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(related_name='news_posts', to='history.category', verbose_name='Categorías'),
        ),
    ]