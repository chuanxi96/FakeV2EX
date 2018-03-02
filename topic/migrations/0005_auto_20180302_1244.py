# Generated by Django 2.0.2 on 2018-03-02 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0004_topicvote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='dislike_num',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='like_num',
        ),
        migrations.RemoveField(
            model_name='topicvote',
            name='topic',
        ),
        migrations.AlterUniqueTogether(
            name='topiccategory',
            unique_together={('code', 'category_type')},
        ),
    ]
