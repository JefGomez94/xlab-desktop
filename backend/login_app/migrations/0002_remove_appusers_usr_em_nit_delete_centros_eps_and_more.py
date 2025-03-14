# Generated by Django 4.2.20 on 2025-03-07 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appusers',
            name='usr_em_nit',
        ),
        migrations.DeleteModel(
            name='Centros_eps',
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
        migrations.RemoveField(
            model_name='estudios',
            name='e_gru_id',
        ),
        migrations.DeleteModel(
            name='Estudiosdet',
        ),
        migrations.RemoveField(
            model_name='eventos',
            name='ev_em_nit',
        ),
        migrations.RemoveField(
            model_name='historias',
            name='h_em_id',
        ),
        migrations.RemoveField(
            model_name='laboratorios',
            name='l_em_id',
        ),
        migrations.RemoveField(
            model_name='laboratorios',
            name='l_pru_id',
        ),
        migrations.DeleteModel(
            name='LaboratoriosRem',
        ),
        migrations.RemoveField(
            model_name='medicos',
            name='m_em_nit',
        ),
        migrations.RemoveField(
            model_name='ordenes',
            name='o_dia_id',
        ),
        migrations.RemoveField(
            model_name='ordenes',
            name='o_em_id',
        ),
        migrations.RemoveField(
            model_name='ordenesdet',
            name='od_em_id',
        ),
        migrations.RemoveField(
            model_name='ordenesdet',
            name='od_est_id',
        ),
        migrations.RemoveField(
            model_name='pruebas',
            name='p_gru_id',
        ),
        migrations.DeleteModel(
            name='Servicios',
        ),
        migrations.DeleteModel(
            name='Tecnicasprueba',
        ),
        migrations.DeleteModel(
            name='Appusers',
        ),
        migrations.DeleteModel(
            name='Diagnosticos',
        ),
        migrations.DeleteModel(
            name='Estudios',
        ),
        migrations.DeleteModel(
            name='Eventos',
        ),
        migrations.DeleteModel(
            name='Grupostrabajo',
        ),
        migrations.DeleteModel(
            name='Historias',
        ),
        migrations.DeleteModel(
            name='Laboratorio',
        ),
        migrations.DeleteModel(
            name='Laboratorios',
        ),
        migrations.DeleteModel(
            name='Medicos',
        ),
        migrations.DeleteModel(
            name='Ordenes',
        ),
        migrations.DeleteModel(
            name='Ordenesdet',
        ),
        migrations.DeleteModel(
            name='Pruebas',
        ),
    ]
