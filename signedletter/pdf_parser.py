import qrcode
from reportlab.pdfgen.canvas import Canvas
from config.settings import MEDIA_ROOT


from reportlab.pdfgen import canvas
from reportlab.lib import styles

class PdfParser:
    
    def create_qrcode_image(self, save_folder_path):
        qr_code = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=2,
        border=2,
            )
        qr_code.add_data(save_folder_path)
        qr_code.make(fit=True)
        qr_code_image = qr_code.make_image(fill_color="black", back_color="white")
        qr_code_image.save(MEDIA_ROOT / "data.png")
        return MEDIA_ROOT / "data.png"


    def create_qrcode_pdf(self,  qr_code_image, watermark_file:str='watermark.pdf', **kwargs):
        """
            Create pdf file with qrcode image
        """
        # if watermark_file doesn't exist, create it
        watermark_file = MEDIA_ROOT / watermark_file
        if not watermark_file.exists():
            watermark_file.touch()

        doc = Canvas(str(MEDIA_ROOT / watermark_file))
        regular_font = "Times-Bold"
        font_size=12

        doc.setFont(regular_font,font_size)
        
        # draw the QR code at the specified coordinates
        doc.drawImage(qr_code_image, 270, 80)
     
        if kwargs:
            #data
            data_1 = kwargs.get('data_1', '')
            data_2 = kwargs.get('data_2', '')

            # data = kwargs.get('data_2', '').split(' ')
            # data.insert(2,'\n')
          
            # data_2=' '.join(data)
            # print(data_2)
            
            #coordinates
            x_path_1 = kwargs.get('x_path_1', 0)
            y_path_1 = kwargs.get('y_path_1', 0)

            x_path_2 = kwargs.get('x_path_2', 0)
            y_path_2 = kwargs.get('y_path_2', 0)
            #draw data
            doc.drawString(x_path_1, y_path_1, data_1)
            doc.drawString(x_path_2, y_path_2, 'Boshqarma boshlig\'ining')
            doc.drawString(88, 115, data_2)
            
            #TODO: add more data to pdf file
        doc.save()
        return watermark_file