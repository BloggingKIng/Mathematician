# Generated by Django 4.0.5 on 2022-08-06 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('is_correct', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choices', models.ManyToManyField(to='Quiz.answer')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(default='What is the ans of 2 + 2', max_length=1000)),
                ('question_mark', models.IntegerField(default=2)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Quiz.test')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='choice_qs',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Quiz.question'),
        ),
    ]