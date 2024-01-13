import pdfkit
from django.core.files.base import ContentFile
from .models import Template
from letterapp.models import LetterInstruction,PdfFilePath
import os
from django.conf import settings
from django.utils import timezone
from datetime import timedelta

# Define LetterInstructions' pdf file utl
pdf_file_path=PdfFilePath.pdf_instraction_path
media_root=settings.MEDIA_ROOT


def generate_pdf(
        template_pk1,
        typeletter_pk,
        request,
        file_name,

        adress,
        street,
        company_name,
        inn_number,
        phone_number,
    
        
        ):

 
    template=Template.objects.get(
        user=request.user,
        id=template_pk1,
        typeletter_id=typeletter_pk,

        )
 
    print('------------>',file_name)
    template_html=template.body.format(
                            created_date=timezone.now().strftime('%Y-%m-%d'),
                            letter_date=template.report_date,

                            adress=adress,
                            street=street,
                            company_name=company_name,
                            inn_number=inn_number,
                            phone_number=phone_number,
                            letter_title=template.title,
                            admin_number=request.user.user_number_litter,
                            letter_number=file_name,
                            
            )

    # file path for save 
    full_letterinstruction_pdf_path=f'{media_root}{pdf_file_path}'
    pdf_path=f'{full_letterinstruction_pdf_path}{file_name}.pdf'

    pdfkit.from_string(template_html,pdf_path)

    # file url for see 
    pdf_url=f'{pdf_file_path}{file_name}.pdf'


    return  pdf_url


