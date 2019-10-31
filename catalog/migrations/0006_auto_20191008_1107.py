# Generated by Django 2.2.4 on 2019-10-08 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_bookinstance_borrow'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['return_date'], 'verbose_name': 'Экземпляр книги', 'verbose_name_plural': 'Экземпляр книг'},
        ),
        migrations.RenameField(
            model_name='bookinstance',
            old_name='borrow',
            new_name='borrower',
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='return_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата возврата книги'),
        ),
    ]
