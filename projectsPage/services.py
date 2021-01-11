import os

from PIL import Image
from io import BytesIO
from resizeimage import resizeimage
from django.core.files.base import ContentFile


def resize_image(self, new_width):
	name, extension = os.path.splitext(self.photo.name)
	extension = extension.lower()

	if extension in ['.jpeg', '.jpg']:
		format_type = 'JPEG'
	elif extension == '.png':
		format_type = 'PNG'

	pil_image_obj = Image.open(self.photo)
	width = pil_image_obj.width
	height = pil_image_obj.height

	if width > new_width:
		try:
			new_big_image = resizeimage.resize_width(pil_image_obj, new_width)
			width = new_width
			height = new_big_image.height
		except:
			return
	else:
		new_big_image = pil_image_obj

	new_big_image_io = BytesIO()
	new_big_image.save(new_big_image_io, format=format_type)
	big_image_name = 'big_'+self.photo.name

	self.photo.delete(save=False)
	self.photo.save(
		big_image_name,
		content=ContentFile(new_big_image_io.getvalue()),
		save=False)

	self.width = width
	self.height = height

	if self.small_photo:
		name, extension = os.path.splitext(self.small_photo.name)
		extension = extension.lower()

		if extension in ['.jpeg', '.jpg']:
			format_type = 'JPEG'
		elif extension == '.png':
			format_type = 'PNG'

		pil_image_obj = Image.open(self.small_photo)
		width = pil_image_obj.width
		height = pil_image_obj.height

	if width > 800:
		try:
			new_small_image = resizeimage.resize_width(pil_image_obj, 800)
		except:
			return
	else:
		new_small_image = pil_image_obj

	new_small_image_io = BytesIO()
	new_small_image.save(new_small_image_io, format=format_type)
	small_image_name = 'small_'+name
	
	self.small_photo.delete(save=False)
	self.small_photo.save(
		small_image_name,
		content=ContentFile(new_small_image_io.getvalue()),
		save=False)
