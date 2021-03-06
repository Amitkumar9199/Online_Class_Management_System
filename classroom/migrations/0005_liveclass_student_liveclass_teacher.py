# Generated by Django 4.0 on 2022-03-26 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0004_liveclass_classlink'),
    ]

    operations = [
        migrations.AddField(
            model_name='liveclass',
            name='student',
            field=models.ManyToManyField(related_name='student_liveClass', to='classroom.Student'),
        ),
        migrations.AddField(
            model_name='liveclass',
            name='teacher',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='teacher_liveClass', to='classroom.teacher'),
        ),
    ]
