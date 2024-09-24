import io
import re
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.pagesizes import letter
import streamlit as st


def format_content_for_pdf(content):
    content = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', content)
    content = re.sub(r'\n', '<br />', content)
    return content


@st.cache_data
def generate_pdf(content):
    pdf_buffer = io.BytesIO()
    pdf = SimpleDocTemplate(pdf_buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    normal_style = styles['Normal']
    formatted_content = format_content_for_pdf(content)
    story = [Paragraph(formatted_content, normal_style)]
    pdf.build(story)
    pdf_buffer.seek(0)
    return pdf_buffer