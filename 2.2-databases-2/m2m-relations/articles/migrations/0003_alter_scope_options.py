# Generated by Django 4.0.4 on 2022-05-31 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_tag_alter_article_options_scope_article_tags'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scope',
            options={'ordering': ['is_main', 'tag'], 'verbose_name': 'Тематика статьи', 'verbose_name_plural': 'Тематики статей'},
        ),
    ]