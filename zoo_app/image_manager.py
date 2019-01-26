import base64
import io

def createBase64Image(img_obj):
     buffer = io.BytesIO()
     img_obj.save(buffer, format="jpeg")
     return base64.b64encode(buffer.getvalue()).decode()
