from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin, UserManager
from simple_history.models import HistoricalRecords


class UserManager(BaseUserManager):

	def _create_user(self, username, email, name,last_name, password, is_staff, is_superuser, **extra_fields):
		user = self.model(
			username = username,
			email = email,
			name = name, 
            last_name = last_name,
			is_staff = is_staff,
			is_superuser = is_superuser,
			**extra_fields
		)
		user.set_password(password)
		user.save(using=self.db)
		return user

	def create_user(self, username, email, name,last_name, password=None, **extra_fields): 
		return self._create_user(username, email, name, last_name, password, False, False, **extra_fields)


	def create_superuser(self, username, email, name,last_name, password=None, **extra_fields):
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)

		if extra_fields.get('is_superuser') is not True:
			raise ValueError('El superusuario debe tener is_superuser=True .')
		if extra_fields.get('is_staff') is not True:
			raise ValueError('El superusuario debe tener is_staff=True')
		
		return self._create_user(username, email, name,last_name, password, **extra_fields)

#MODELO USUARIO CREACION BD
#AGREGAR CAMPO NULO O BLACK DIFERENCIAS Y PORQUE?
class User(AbstractBaseUser, PermissionsMixin):
     
	username = models.CharField(max_length=50, unique = True, blank=False, null=False)
	email = models.EmailField('Correo Electrónico', max_length=50, unique = True,) 
	name = models.CharField('Nombres', max_length = 100, blank = False, null = False)
	last_name = models.CharField('Apellidos', max_length= 100, blank=True, null = True)
	document_id = models.CharField("N° de documento", max_length=50, unique= True, blank=True, null=True)
	Position_company = models.CharField("Puesto en compañia", max_length=25, blank=True, null=True)#  <------ ANALIZAR ESTE CAMPO
	is_active = models.BooleanField(default = True)
	is_staff = models.BooleanField(default = False)
	historical = HistoricalRecords() 
	objects = UserManager() #WHAT USER MANAGER USOS

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email', 'name', 'last_name','password']

	class Meta:
		verbose_name = 'Usuario'
		verbose_name_plural = 'Usuarios'

	#FUNCTIONS
	def natural_key(self):
		return (self.username)

	def __str__(self):
		""" VISUALIZACION DE UN MODELO POR DEFECTO
		SE visualiza en navegador o movil donde se solicite """
		return f'{self.name} {self.last_name}'
	
