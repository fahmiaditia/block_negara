from django.db import models
import uuid

# Create your models here.

class Data_Negara(models.Model):
	class Meta:
		verbose_name_plural = "Data Negara"

	uuid_negara = models.CharField(max_length=130, verbose_name="UUID Negara")
	nama_negara = models.CharField(max_length=30, verbose_name="Negara")
	izin_negara = models.BooleanField(default=True, verbose_name="Status")

	def __str__(self):
		return f"{self.nama_negara} - {self.uuid_negara}"

