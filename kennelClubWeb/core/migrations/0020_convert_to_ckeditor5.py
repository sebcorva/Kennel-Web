# Generated manually for CKEditor 5 migration

from django.db import migrations, models
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_preguntasfrecuentes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticias',
            name='texto',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='crianza',
            name='contenido',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='club',
            name='descripcion',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True),
        ),
    ] 