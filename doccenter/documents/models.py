"""Document models."""
import uuid

from django.db import models
from django.core.validators import FileExtensionValidator

from taggit.managers import TaggableManager


def uuid_directory_path(instance, filename):
    """Upload file to MEDIA_ROOT/documents/<instance.uuid>/<filename>."""
    return f"documents/{uuid.uuid4()}/{filename}"


class Document(models.Model):
    """Document in docx or pdf format."""

    title = models.CharField(max_length=255, blank=True)
    file_upload = models.FileField(
        upload_to=uuid_directory_path,
        validators=[FileExtensionValidator(allowed_extensions=["pdf", "docx"])],
    )
    tags = TaggableManager(blank=True)

    def __str__(self) -> str:
        return f"Document {self.title}"
