from django.db import models

# Create your models here.

class Document(models.Model):
    course_code = models.CharField(max_length=20)
    course_title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="doc_images", default="nounicon4.jpg")
    is_paid = models.BooleanField(default=False)
    document = models.FileField(upload_to="documents", validators=[FileExtensionValidator(['pdf'])])
    exam_year = models.PositiveSmallIntegerField()
    file_format = models.CharField(max_length=50)