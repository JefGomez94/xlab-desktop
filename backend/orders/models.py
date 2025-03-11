from django.db import models
from django.utils.timezone import now

class Ordenes(models.Model):
    o_id = models.IntegerField()
    o_numero = models.CharField(max_length=12, blank=True, null=True)
    o_fecha = models.DateTimeField(blank=True, null=True)
    o_his_id = models.IntegerField(blank=True, null=True)
    o_fac_id = models.IntegerField(blank=True, null=True)
    o_fecha_toma = models.DateTimeField(blank=True, null=True)
    o_fecha_impresion = models.DateTimeField(blank=True, null=True)
    o_edad = models.IntegerField(blank=True, null=True)
    o_embarazo = models.IntegerField(blank=True, null=True)
    o_estado = models.IntegerField(blank=True, null=True)
    o_cen_id = models.IntegerField(blank=True, null=True)
    o_ser_id = models.IntegerField(blank=True, null=True)#models.ForeignKey('Servicios', models.DO_NOTHING, blank=True, null=True)
    o_med_id = models.IntegerField(blank=True, null=True)
    o_dia_id = models.ForeignKey('Diagnosticos', models.DO_NOTHING, blank=True, null=True)#models.IntegerField(blank=True, null=True)
    o_cama = models.CharField(max_length=15, blank=True, null=True)
    o_nota = models.TextField(blank=True, null=True)
    o_labtot = models.IntegerField(blank=True, null=True)
    o_labnor = models.IntegerField(blank=True, null=True)
    o_labval = models.IntegerField(blank=True, null=True)
    o_labimp = models.IntegerField(blank=True, null=True)
    o_labres = models.IntegerField(blank=True, null=True)
    o_labpen = models.IntegerField(blank=True, null=True)
    o_cem_id = models.IntegerField(blank=True, null=True)
    o_numero_externo = models.CharField(max_length=12, blank=True, null=True)
    o_numero_autoriza = models.CharField(max_length=30, blank=True, null=True)
    o_fecha_autoriza = models.DateTimeField(blank=True, null=True)
    o_export_estado = models.IntegerField(blank=True, null=True)
    o_export_fecha = models.DateTimeField(blank=True, null=True)
    o_dep_codigo = models.CharField(max_length=5, blank=True, null=True)
    o_mun_codigo = models.CharField(max_length=5, blank=True, null=True)
    o_dia_id2 = models.IntegerField(blank=True, null=True)
    o_em_id = models.ForeignKey('Laboratorio', models.DO_NOTHING, blank=True, null=True)#models.CharField(max_length=30, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.pk:  # Si el registro ya existe
            self.accion = 'UPDATE'
        else:  # Si es un nuevo registro
            self.accion = 'CREATE'
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.accion = 'DELETE'
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"Orden {self.o_numero}"

class Ordenesdet(models.Model):
    od_id = models.IntegerField(blank=True, null=True)
    od_ord_id = models.IntegerField(blank=True, null=True)#models.ForeignKey('Ordenes', models.DO_NOTHING, blank=True, null=True)
    od_est_id = models.ForeignKey('Estudios', models.DO_NOTHING, blank=True, null=True)#models.IntegerField(blank=True, null=True)
    od_idxest = models.IntegerField(blank=True, null=True)
    od_ade_id = models.IntegerField(blank=True, null=True)
    od_prog_fecha = models.DateTimeField(blank=True, null=True)
    od_em_id = models.ForeignKey('Laboratorio', models.DO_NOTHING, blank=True, null=True)#models.CharField(max_length=30, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.pk:  # Si el registro ya existe
            self.accion = 'UPDATE'
        else:  # Si es un nuevo registro
            self.accion = 'CREATE'
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.accion = 'DELETE'
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"Orden {self.od_id}"

class Historias(models.Model):
    h_id = models.IntegerField()
    h_numero = models.CharField(max_length=16, blank=True, null=True)
    h_identificacion = models.CharField(max_length=16, blank=True, null=True)
    h_fecha = models.DateTimeField(blank=True, null=True)
    h_nombres = models.CharField(max_length=40, blank=True, null=True)
    h_apellido1 = models.CharField(max_length=20, blank=True, null=True)
    h_apellido2 = models.CharField(max_length=20, blank=True, null=True)
    h_fecha_nacimiento = models.DateTimeField(blank=True, null=True)
    h_sexo = models.CharField(max_length=2, blank=True, null=True)
    h_foto = models.CharField(max_length=255, blank=True, null=True)
    h_email = models.CharField(max_length=40, blank=True, null=True)
    h_nota = models.TextField(blank=True, null=True)
    h_telefonos = models.CharField(max_length=30, blank=True, null=True)
    h_tipoident = models.CharField(max_length=3, blank=True, null=True)
    h_ips_cod = models.IntegerField(blank=True, null=True)
    h_direccion = models.CharField(max_length=80, blank=True, null=True)
    h_zona = models.CharField(max_length=1, blank=True, null=True)
    h_em_id = models.ForeignKey('Laboratorio', models.DO_NOTHING, blank=True, null=True)#models.CharField(max_length=30, blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if self.pk:  # Si el registro ya existe
            self.accion = 'UPDATE'
        else:  # Si es un nuevo registro
            self.accion = 'CREATE'
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.accion = 'DELETE'
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"Historia {self.h_id} - Acción: {self.accion}"
    
class Laboratorios(models.Model):
    l_id = models.IntegerField()
    l_ord_id = models.IntegerField(blank=True, null=True)
    l_est_id = models.IntegerField(blank=True, null=True)#models.ForeignKey('Estudios', models.DO_NOTHING, blank=True, null=True)
    l_pru_id = models.ForeignKey('Pruebas', models.DO_NOTHING, blank=True, null=True)#models.IntegerField(blank=True, null=True)
    l_fecha = models.DateTimeField(blank=True, null=True)
    l_fecha_crea = models.DateTimeField(blank=True, null=True)
    l_fecha_mod = models.DateTimeField(blank=True, null=True)
    l_fecha_val = models.DateTimeField(blank=True, null=True)
    l_fecha_imp = models.DateTimeField(blank=True, null=True)
    l_resultado = models.CharField(max_length=15, blank=True, null=True)
    l_resultnum = models.FloatField(blank=True, null=True)
    l_resultcomp = models.TextField(blank=True, null=True)
    l_resultgraf = models.CharField(max_length=255, blank=True, null=True)  # Cambiado de BinaryField a CharField
    l_ref_inf = models.FloatField(blank=True, null=True)
    l_ref_sup = models.FloatField(blank=True, null=True)
    l_estado = models.IntegerField(blank=True, null=True)
    l_orden_imp = models.IntegerField(blank=True, null=True)
    l_gru_id = models.IntegerField(blank=True, null=True)
    l_estado_rango = models.IntegerField(blank=True, null=True)
    l_idxest = models.IntegerField(blank=True, null=True)
    l_usr_val = models.IntegerField(blank=True, null=True)
    l_confirmado = models.IntegerField(blank=True, null=True)
    l_txorigen = models.IntegerField(blank=True, null=True)
    l_tpr_id = models.IntegerField(blank=True, null=True)
    l_nota = models.TextField(blank=True, null=True)
    l_exp_id = models.IntegerField(blank=True, null=True)
    l_datacheck = models.IntegerField(blank=True, null=True)
    qc_excluir = models.CharField(max_length=1, blank=True, null=True)
    qc_dato_grupo = models.IntegerField(blank=True, null=True)
    qc_imagen = models.BinaryField(blank=True, null=True)
    l_nota_aud = models.TextField(blank=True, null=True)
    l_origen_infosalud = models.IntegerField(blank=True, null=True)
    l_cod_prueba = models.CharField(max_length=255, blank=True, null=True)
    l_gru_visual = models.CharField(max_length=255, blank=True, null=True)
    l_o_numero_externo = models.CharField(max_length=255, blank=True, null=True)
    l_ord_visual = models.CharField(max_length=255, blank=True, null=True)
    l_pru_unidad = models.CharField(max_length=255, blank=True, null=True)
    l_tpr_rango_ref = models.CharField(max_length=255, blank=True, null=True)
    l_em_id = models.ForeignKey('Laboratorio', models.DO_NOTHING, blank=True, null=True)#models.CharField(max_length=30, blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if self.pk:  # Si el registro ya existe
            self.accion = 'UPDATE'
        else:  # Si es un nuevo registro
            self.accion = 'CREATE'
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.accion = 'DELETE'
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"Laboratorio {self.l_id}"

class LaboratoriosRem(models.Model):
    lR_id = models.IntegerField(blank=True, null=True)
    lR_resultado = models.CharField(max_length=255, blank=True, null=True)
    lR_fecha = models.DateTimeField(default=now, editable=False)  # Fecha y hora al momento del registro
    lR_ord_id = models.IntegerField(blank=True, null=True)
    lR_em_id = models.CharField(max_length=25, blank=True, null=True)
    lR_disponible = models.BooleanField(default=True, editable=True)

    def save(self, *args, **kwargs):
        if self.pk:  # Si el registro ya existe
            self.accion = 'UPDATE'
        else:  # Si es un nuevo registro
            self.accion = 'CREATE'
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.accion = 'DELETE'
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"Orden {self.lR_ord_id} - Nit: {self.lR_em_id}"

class Estudios(models.Model):
    e_id = models.IntegerField(primary_key=True)
    e_codigo = models.CharField(max_length=15, blank=True, null=True)
    e_nombre = models.CharField(max_length=200, blank=True, null=True)
    e_cod_alterno = models.CharField(max_length=30, blank=True, null=True)
    e_nom_alterno = models.CharField(max_length=200, blank=True, null=True)
    e_gru_id = models.ForeignKey('Grupostrabajo', models.DO_NOTHING, blank=True, null=True)
    e_orden_imp = models.IntegerField(blank=True, null=True)
    e_valor_base = models.FloatField(blank=True, null=True)
    e_remision = models.IntegerField(blank=True, null=True)
    e_activo = models.IntegerField(blank=True, null=True)
    e_conjunto = models.IntegerField(blank=True, null=True)
    e_notas = models.TextField(blank=True, null=True)
    e_newpage = models.IntegerField(blank=True, null=True)
    e_codabrev = models.CharField(max_length=8, blank=True, null=True)
    e_bclblnum = models.IntegerField(blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if self.pk:  # Si el registro ya existe
            self.accion = 'UPDATE'
        else:  # Si es un nuevo registro
            self.accion = 'CREATE'
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.accion = 'DELETE'
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"Estudio {self.e_id} - Acción: {self.accion}"

class Estudiosdet(models.Model):
    ed_id = models.IntegerField(primary_key=True)
    ed_est_id = models.IntegerField(blank=True, null=True)
    ed_pru_id = models.IntegerField(blank=True, null=True)
    ed_pru_codigo = models.CharField(max_length=20, blank=True, null=True)
    ed_orden_imp = models.IntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.pk:  # Si el registro ya existe
            self.accion = 'UPDATE'
        else:  # Si es un nuevo registro
            self.accion = 'CREATE'
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.accion = 'DELETE'
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"Estudiosdet {self.ed_id} - Acción: {self.accion}"

class Pruebas(models.Model):
    p_id = models.IntegerField(primary_key=True)
    p_codigo = models.CharField(max_length=10, blank=True, null=True)
    p_cod_alterno = models.CharField(max_length=10, blank=True, null=True)
    p_nombre = models.CharField(max_length=70, blank=True, null=True)
    p_unidades = models.CharField(max_length=15, blank=True, null=True)
    p_gru_id = models.ForeignKey('Grupostrabajo', models.DO_NOTHING, blank=True, null=True)
    p_tipo_resultado = models.CharField(max_length=1, blank=True, null=True)
    p_formula = models.CharField(max_length=100, blank=True, null=True)
    p_comp_formato = models.TextField(blank=True, null=True)
    p_min_alarma = models.FloatField(blank=True, null=True)
    p_max_alarma = models.FloatField(blank=True, null=True)
    p_valor_inferior1 = models.FloatField(blank=True, null=True)
    p_valor_inferior2 = models.FloatField(blank=True, null=True)
    p_valor_inferior3 = models.FloatField(blank=True, null=True)
    p_valor_inferior4 = models.FloatField(blank=True, null=True)
    p_valor_superior1 = models.FloatField(blank=True, null=True)
    p_valor_superior2 = models.FloatField(blank=True, null=True)
    p_valor_superior3 = models.FloatField(blank=True, null=True)
    p_valor_superior4 = models.FloatField(blank=True, null=True)
    p_rangos_ext = models.TextField(blank=True, null=True)
    p_numdec_res = models.IntegerField(blank=True, null=True)
    p_tecnica = models.CharField(max_length=80, blank=True, null=True)
    p_rangos_ref = models.CharField(blank=True, null=True)
    p_tpr_id = models.IntegerField(blank=True, null=True)
    p_tiporef = models.IntegerField(blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if self.pk:  # Si el registro ya existe
            self.accion = 'UPDATE'
        else:  # Si es un nuevo registro
            self.accion = 'CREATE'
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.accion = 'DELETE'
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"Prueba {self.p_id} - Acción: {self.accion}"

class Grupostrabajo(models.Model):
    g_id = models.IntegerField(primary_key=True)
    g_codigo = models.CharField(max_length=5, blank=True, null=True)
    g_nombre = models.CharField(max_length=70, blank=True, null=True)
    g_orden_imp = models.IntegerField(blank=True, null=True)
    g_activo = models.IntegerField(blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if self.pk:  # Si el registro ya existe
            self.accion = 'UPDATE'
        else:  # Si es un nuevo registro
            self.accion = 'CREATE'
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.accion = 'DELETE'
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"Grupostrabajo {self.g_id} - Acción: {self.accion}"

class Servicios(models.Model):
    s_id = models.IntegerField(primary_key=True)
    s_codigo = models.CharField(max_length=15, blank=True, null=True)
    s_nombre = models.CharField(max_length=100, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.pk:  # Si el registro ya existe
            self.accion = 'UPDATE'
        else:  # Si es un nuevo registro
            self.accion = 'CREATE'
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.accion = 'DELETE'
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"Servicio {self.s_id} - Acción: {self.accion}"

class Medicos(models.Model):
    m_id = models.IntegerField()
    m_codigo = models.CharField(max_length=15, blank=True, null=True)
    m_nombre = models.CharField(max_length=40, blank=True, null=True)
    m_email = models.CharField(max_length=40, blank=True, null=True)
    m_tcod = models.CharField(max_length=2, blank=True, null=True)
    m_regprof = models.CharField(max_length=10, blank=True, null=True)
    m_especialidad = models.CharField(max_length=30, blank=True, null=True)
    m_em_nit = models.ForeignKey('Laboratorio', models.DO_NOTHING, blank=True, null=True)#models.CharField(max_length=30, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.pk:  # Si el registro ya existe
            self.accion = 'UPDATE'
        else:  # Si es un nuevo registro
            self.accion = 'CREATE'
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.accion = 'DELETE'
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"Medico {self.m_id} - Acción: {self.accion}"

class Diagnosticos(models.Model):
    d_id = models.IntegerField(primary_key=True)
    d_codigo = models.CharField(max_length=4, blank=True, null=True)
    d_descripcion = models.CharField(max_length=254, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.pk:  # Si el registro ya existe
            self.accion = 'UPDATE'
        else:  # Si es un nuevo registro
            self.accion = 'CREATE'
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.accion = 'DELETE'
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"Diagnostico {self.d_id} - Acción: {self.accion}"

class Centros_eps(models.Model):
    c_id = models.IntegerField(primary_key=True)
    c_codigo = models.CharField(max_length=15, blank=True, null=True)
    c_nombre = models.CharField(max_length=100, blank=True, null=True)
    c_tar_id = models.IntegerField(blank=True, null=True)
    c_email = models.CharField(max_length=100, blank=True, null=True)
    c_nit = models.CharField(max_length=15, blank=True, null=True)
    c_direccion = models.CharField(max_length=60, blank=True, null=True)
    c_dpto = models.CharField(max_length=2, blank=True, null=True)
    c_muni = models.CharField(max_length=3, blank=True, null=True)
    c_contributivo = models.CharField(max_length=1, blank=True, null=True)
    c_subsidiado = models.CharField(max_length=1, blank=True, null=True)
    c_descuento = models.IntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.pk:  # Si el registro ya existe
            self.accion = 'UPDATE'
        else:  # Si es un nuevo registro
            self.accion = 'CREATE'
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.accion = 'DELETE'
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"Centro_eps {self.c_id} - Acción: {self.accion}"
    
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone
from .managers import AppusersManager

class CustomUser(AbstractBaseUser):
    usr_identification = models.CharField(max_length=50, unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    

    objects = AppusersManager()

    USERNAME_FIELD = 'usr_identification'

class Appusers(AbstractBaseUser):
    usr_id = models.IntegerField()
    usr_name = models.CharField(max_length=30, blank=True, null=True)
    usr_description = models.CharField(max_length=50, blank=True, null=True)
    usr_signature = models.CharField(max_length=255, blank=True, null=True)
    usr_identification = models.CharField(max_length=16, blank=True, null=True, unique=True)
    usr_em_nit = models.ForeignKey('Laboratorio', models.DO_NOTHING, blank=True, null=True)
    usr_email = models.EmailField(null=True, unique=True)
    usr_password = models.CharField(null=True, max_length=128)
    password = models.CharField(max_length=128, null=True, blank=True)
    accion = models.CharField(max_length=10, default='CREATE')
    last_login = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=False)
    load_resRem = models.BooleanField(default=False)

    objects = AppusersManager()

    USERNAME_FIELD = 'usr_identification'
    REQUIRED_FIELDS = ['usr_id']

    def save(self, *args, **kwargs):
        if not self.pk or 'usr_password' in kwargs:
            self.usr_password = make_password(self.usr_identification)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.accion = 'DELETE'
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"Appuser {self.usr_id} - Acción: {self.accion}"

    # Métodos requeridos para la autenticación
    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_username(self):
        return self.usr_identification
    
    # Propiedades adicionales que Django puede necesitar
    @property
    def is_staff(self):
        return False

    @property
    def is_superuser(self):
        return False

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

class Laboratorio(models.Model):
    lab_nit = models.IntegerField(primary_key=True, null=False, blank=False)
    lab_nombre = models.CharField(max_length=100, null=True, blank=True)
    lab_datos = models.CharField(max_length=250, null=True, blank=True)
    lab_email = models.CharField(max_length=50, null=True, blank=True)
    lab_isActive = models.BooleanField(default=True)
    lab_dateExpired = models.DateField(null=True, blank=True)
    lab_logo = models.CharField(max_length=250, null=True, blank=True)  # Asegúrate de que editable=True
    lab_nit_num = models.CharField(max_length=20, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.pk:
            self.accion = 'UPDATE'
        else:
            self.accion = 'CREATE'
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.accion = 'DELETE'
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"Lab_emp {self.lab_nit} - Acción: {self.accion}"

class Tecnicasprueba(models.Model):
    tpr_id = models.IntegerField(primary_key=True)
    tpr_pru_id = models.IntegerField(blank=True, null=True)
    tpr_tecnica = models.CharField(max_length=90, blank=True, null=True)
    tpr_min_alarma = models.FloatField(blank=True, null=True)
    tpr_max_alarma = models.FloatField(blank=True, null=True)
    tpr_min_masculino = models.FloatField(blank=True, null=True)
    tpr_max_masculino = models.FloatField(blank=True, null=True)
    tpr_min_femenino = models.FloatField(blank=True, null=True)
    tpr_max_femenino = models.FloatField(blank=True, null=True)
    tpr_min_menor = models.FloatField(blank=True, null=True)
    tpr_max_menor = models.FloatField(blank=True, null=True)
    tpr_min_embarazo = models.FloatField(blank=True, null=True)
    tpr_max_embarazo = models.FloatField(blank=True, null=True)
    tpr_rango_ext = models.TextField(blank=True, null=True)
    tpr_rango_ref = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.pk:  # Si el registro ya existe
            self.accion = 'UPDATE'
        else:  # Si es un nuevo registro
            self.accion = 'CREATE'
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.accion = 'DELETE'
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"tpr_id {self.tpr_id} - Acción: {self.accion}"

class Eventos(models.Model):
    ev_id = models.AutoField(primary_key=True)
    ev_name = models.CharField(blank=True, null=True, max_length=50)
    ev_description = models.TextField(blank=True, null=True, max_length=255)
    ev_result = models.BooleanField(blank=True, null=True)
    ev_date = models.DateTimeField(default=timezone.now)
    ev_user_login = models.CharField(blank=True, null=True, max_length=100)
    ev_input_search = models.CharField(blank=True, null=True, max_length=255)
    ev_user_table = models.CharField(blank=True, null=True, max_length=50)
    ev_ip_origen = models.CharField(blank=True, null=True, max_length=50)
    ev_archivo = models.CharField(blank=True, null=True, max_length=255)
    ev_browser = models.CharField(blank=True, null=True, max_length=100)
    ev_os = models.CharField(blank=True, null=True, max_length=100)
    ev_em_nit = models.ForeignKey('Laboratorio', models.DO_NOTHING, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.pk:  # Si el registro ya existe
            self.accion = 'UPDATE'
        else:  # Si es un nuevo registro
            self.accion = 'CREATE'
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.accion = 'DELETE'
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"tpr_id {self.ev_id}"
