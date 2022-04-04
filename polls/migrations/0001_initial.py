<<<<<<< HEAD
# Generated by Django 4.0.1 on 2022-04-03 09:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
=======
# Generated by Django 4.0.1 on 2022-03-20 07:46

from django.db import migrations, models
import django.db.models.deletion
>>>>>>> eadf4933b17b4f1e48aa6f604a342fb4573953d9


class Migration(migrations.Migration):

    initial = True

    dependencies = [
<<<<<<< HEAD
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
=======
>>>>>>> eadf4933b17b4f1e48aa6f604a342fb4573953d9
    ]

    operations = [
        migrations.CreateModel(
<<<<<<< HEAD
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
=======
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.question')),
>>>>>>> eadf4933b17b4f1e48aa6f604a342fb4573953d9
            ],
        ),
    ]