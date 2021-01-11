import os
import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.dispatch import receiver

from .choices import SPACE_CHOICES
from .services import resize_image


class Project(models.Model):
	space = models.CharField(_('Ambiente'), max_length=15, blank=True, choices=SPACE_CHOICES)
	photo = models.ImageField(
		_("Foto")
	)
	small_photo = models.ImageField(
		_("Foto Pequena"),
		help_text='Caso nenhuma img seja selecionada, o sistema irá gerar uma miniatura automaticamente.',
		null=True,
		blank=True
	)
	position = models.PositiveSmallIntegerField(
		_("Posição"),
		null=True
	)
	description = models.CharField(
		_('Descrição'), max_length=150, blank=True, null=True
	)
	width = models.PositiveSmallIntegerField(
		_("Largura"),
		default=0
	)
	height = models.PositiveSmallIntegerField(
		_("Altura"),
		default=0
	)
	create_at = models.DateTimeField(_('Criado em'), auto_now_add=True)


	__original_photo = None
	__original_small_photo = None

	def __init__(self, *args, **kwargs):
		super(Project, self).__init__(*args, **kwargs)
		self.__original_photo = self.photo
		self.__original_small_photo = self.small_photo

	def save(self, *args, **kwargs):
		if self.photo != self.__original_photo or self.small_photo != self.__original_small_photo :
			if self.space == '360':
				resize_image(self, 5000)
			else:
				resize_image(self, 1920)
		super(Project, self).save(*args, **kwargs)
		self.__original_photo = self.photo
		self.__original_small_photo = self.small_photo

	class Meta:
		ordering = ['-position']
		verbose_name = _('um Projeto')
		verbose_name_plural = _('Imagens dos Projetos')


@receiver(models.signals.post_delete, sender=Project)
def remove_file_from_s3(sender, instance, using, **kwargs):
	instance.photo.delete(save=False)
	instance.small_photo.delete(save=False)

