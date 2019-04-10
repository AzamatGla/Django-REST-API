# Generated by Django 2.2 on 2019-04-09 04:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_remove_comment_company_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='company_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.Company'),
        ),
    ]