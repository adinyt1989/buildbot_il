from reportlab.pdfgen import canvas
from io import BytesIO

async def generate_contract(user_id: str) -> BytesIO:
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer)
    pdf.drawString(100, 800, f"Договор для пользователя {user_id}")
    pdf.save()
    buffer.seek(0)
    return buffer
