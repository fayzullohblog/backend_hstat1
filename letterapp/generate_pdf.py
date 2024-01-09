import pdfkit
from django.core.files.base import ContentFile
from .models import Template
from letterapp.models import LetterInstruction,PdfFilePath
import os
from django.conf import settings


# Define LetterInstructions' pdf file utl
pdf_file_path=PdfFilePath.pdf_instraction_path
media_root=settings.MEDIA_ROOT


def generate_pdf(template_pk1,typeletter_pk,user,file_name):

    template=Template.objects.get(
        user=user,
        id=template_pk1,
        typeletter_id=typeletter_pk,
        )

    template_html=template.body.format(user=template.user)

    # file path for save 
    full_letterinstruction_pdf_path=f'{media_root}{pdf_file_path}'
    pdf_path=f'{full_letterinstruction_pdf_path}{file_name}.pdf'

    pdfkit.from_string(template_html,pdf_path)

    # file url for see 
    pdf_url=f'{pdf_file_path}{file_name}.pdf'


    return  pdf_url


