from django.db import models

# comment out model contents to update values, 
# then run "makemigrations" and "migrate", then alter 
# the fields as needed and insert new data with MySQL client

# Create your models here.
# first dataset
class Flux(models.Model):
	reaction_id = models.IntegerField()
	flux_name = models.CharField(max_length=120)
	control_flux = models.DecimalField(max_digits=50, decimal_places=5)
	control_sem = models.DecimalField(max_digits=50, decimal_places=5)
	temp_flux = models.DecimalField(max_digits=50, decimal_places=5)
	temp_sem = models.DecimalField(max_digits=50, decimal_places=5)
	mannitol_flux = models.DecimalField(max_digits=50, decimal_places=5)
	mannitol_sem = models.DecimalField(max_digits=50, decimal_places=5)

	def __str__(self):
		return self.flux_name

	def get_fields(self):
		return [(field, field.value_to_string(self)) for field in Flux._meta.fields]

# second dataset
class Flux2(models.Model):
	flux_name = models.CharField(max_length=120)
	description = models.CharField(max_length=120)
	reaction_type = models.CharField(max_length=120)
	standard_o2_net_flux = models.DecimalField(max_digits=50, decimal_places=5)
	elevated_o2_net_flux = models.DecimalField(max_digits=50, decimal_places=5)
	standard_o2_net_flux_sd = models.DecimalField(max_digits=50, decimal_places=5)
	elevated_o2_net_flux_sd = models.DecimalField(max_digits=50, decimal_places=5)
	standard_o2_exchange_flux = models.DecimalField(max_digits=50, decimal_places=5)
	elevated_o2_exchange_flux = models.DecimalField(max_digits=50, decimal_places=5)
	standard_o2_exchange_flux_lb = models.DecimalField(max_digits=50, decimal_places=5)
	elevated_o2_exchange_flux_lb = models.DecimalField(max_digits=50, decimal_places=5)
	standard_o2_exchange_flux_ub = models.DecimalField(max_digits=50, decimal_places=5)
	elevated_o2_exchange_flux_ub = models.DecimalField(max_digits=50, decimal_places=5)

	def __str__(self):
		return self.flux_name

	def get_fields(self):
		return [(field, field.value_to_string(self)) for field in Flux2._meta.fields]