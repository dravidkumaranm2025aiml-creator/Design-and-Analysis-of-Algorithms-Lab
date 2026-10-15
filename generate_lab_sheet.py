import os
import pymupdf
import qrcode
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image as RLImage, PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas

# 1. Generate QR codes for all 5 weeks
weeks_info = [
    {
        'week': 'WEEK 1',
        'title': 'Complexity Analysis (Counter Method)',
        'topics': 'Finding Complexity using Counter Method & Loop Analysis (Problems 1 to 5)',
        'url': 'https://github.com/dravidkumaranm2025aiml-creator/Design-and-Analysis-of-Algorithms-Lab/blob/main/Week_1.pdf',
        'qr_file': 'qr_week_1.png'
    },
    {
        'week': 'WEEK 2',
        'title': 'Greedy Algorithms',
        'topics': 'Coin Problem, Cookies Problem, Burger Problem, Max Array Sum, Min Product',
        'url': 'https://github.com/dravidkumaranm2025aiml-creator/Design-and-Analysis-of-Algorithms-Lab/blob/main/Week_2.pdf',
        'qr_file': 'qr_week_2.png'
    },
    {
        'week': 'WEEK 3',
        'title': 'Divide & Conquer Algorithms',
        'topics': 'Count Zeros in Array, Majority Element, Floor Value, Pair Sum, Quick Sort',
        'url': 'https://github.com/dravidkumaranm2025aiml-creator/Design-and-Analysis-of-Algorithms-Lab/blob/main/Week_3.pdf',
        'qr_file': 'qr_week_3.png'
    },
    {
        'week': 'WEEK 4',
        'title': 'Dynamic Programming',
        'topics': 'Playing with Numbers, Chessboard Problem, Longest Common Subsequence, LIS',
        'url': 'https://github.com/dravidkumaranm2025aiml-creator/Design-and-Analysis-of-Algorithms-Lab/blob/main/Week_4.pdf',
        'qr_file': 'qr_week_4.png'
    },
    {
        'week': 'WEEK 5',
        'title': 'Search & Array Optimization',
        'topics': 'Finding Duplicates (O(n²) & O(n)), Array Intersection, Pairs with Difference K',
        'url': 'https://github.com/dravidkumaranm2025aiml-creator/Design-and-Analysis-of-Algorithms-Lab/blob/main/Week_5.pdf',
        'qr_file': 'qr_week_5.png'
    }
]

for w in weeks_info:
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=2,
    )
    qr.add_data(w['url'])
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')
    img.save(w['qr_file'])

# 2. Build Page 2 (The 3-column table) as a standalone PDF first
temp_p2 = 'temp_page2.pdf'
a4_w, a4_h = A4

styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    'DocTitle',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=13,
    leading=16,
    alignment=1,
    textColor=colors.HexColor('#0F172A')
)
sub_style = ParagraphStyle(
    'DocSub',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=9.5,
    leading=13,
    alignment=1,
    textColor=colors.HexColor('#1E3A8A')
)
course_style = ParagraphStyle(
    'DocCourse',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=10.5,
    leading=14,
    alignment=1,
    textColor=colors.HexColor('#0284C7')
)
sheet_title_style = ParagraphStyle(
    'SheetTitle',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=10,
    leading=13,
    alignment=1,
    textColor=colors.HexColor('#334155')
)
info_style = ParagraphStyle(
    'InfoBar',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=8.5,
    leading=12,
    alignment=0,
    textColor=colors.HexColor('#1E293B')
)

th_style = ParagraphStyle(
    'TH',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=10,
    leading=12,
    alignment=1,
    textColor=colors.white
)

week_title_style = ParagraphStyle(
    'WeekTitle',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=11,
    leading=13,
    textColor=colors.HexColor('#0F172A')
)
week_desc_style = ParagraphStyle(
    'WeekDesc',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=8.5,
    leading=11,
    textColor=colors.HexColor('#1E3A8A')
)
week_topics_style = ParagraphStyle(
    'WeekTopics',
    parent=styles['Normal'],
    fontName='Helvetica-Oblique',
    fontSize=7.5,
    leading=9.5,
    textColor=colors.HexColor('#64748B')
)

qr_caption_style = ParagraphStyle(
    'QRCaption',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=7.5,
    leading=9,
    alignment=1,
    textColor=colors.HexColor('#1E3A8A')
)

sign_label_style = ParagraphStyle(
    'SignLabel',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=8.5,
    leading=14,
    textColor=colors.HexColor('#1E293B')
)

story = []
story.append(Paragraph('RAJALAKSHMI ENGINEERING COLLEGE (AUTONOMOUS)', title_style))
story.append(Paragraph('DEPARTMENT OF ARTIFICIAL INTELLIGENCE &amp; MACHINE LEARNING', sub_style))
story.append(Paragraph('CS23331 &mdash; DESIGN AND ANALYSIS OF ALGORITHMS LABORATORY', course_style))
story.append(Paragraph('CONTINUOUS EVALUATION &amp; DIGITAL LAB RECORD SHEET', sheet_title_style))
story.append(Spacer(1, 6))

info_text = '<b>Name:</b> ___________________________ &nbsp;&nbsp;&nbsp;&nbsp; <b>Reg No:</b> ___________________ &nbsp;&nbsp;&nbsp;&nbsp; <b>Year / Sec:</b> ________'
story.append(Paragraph(info_text, info_style))
story.append(Spacer(1, 6))

# Table setup: Total width = 535 pt (left & right margins 30 pt)
# Col 1: 175 pt, Col 2: 175 pt, Col 3: 185 pt
table_rows = [
    [
        Paragraph('Name of the Week', th_style),
        Paragraph('QR Code (Scan for PDF)', th_style),
        Paragraph('Place to Sign / Evaluation', th_style)
    ]
]

for w in weeks_info:
    col1 = [
        Paragraph(f'<b>{w["week"]}</b>', week_title_style),
        Spacer(1, 2),
        Paragraph(f'{w["title"]}', week_desc_style),
        Spacer(1, 2),
        Paragraph(w['topics'], week_topics_style)
    ]
    
    col2 = [
        RLImage(w['qr_file'], width=62, height=62),
        Spacer(1, 2),
        Paragraph(f'<a href="{w["url"]}" color="#1E3A8A"><u>Scan / View PDF</u></a>', qr_caption_style)
    ]
    
    col3 = [
        Paragraph('<b>Date:</b> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;____ / ____ / 2026', sign_label_style),
        Paragraph('<b>Marks:</b> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;________ / 100', sign_label_style),
        Spacer(1, 4),
        Paragraph('<b>Staff Sign:</b> __________________', sign_label_style)
    ]
    
    table_rows.append([col1, col2, col3])

t = Table(table_rows, colWidths=[175, 175, 185])
t.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1E3A8A')),
    ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
    ('VALIGN', (0, 0), (-1, 0), 'MIDDLE'),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 5),
    ('TOPPADDING', (0, 0), (-1, 0), 5),
    
    ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
    ('ALIGN', (1, 1), (1, -1), 'CENTER'),
    ('LEFTMARGIN', (0, 0), (-1, -1), 6),
    ('RIGHTMARGIN', (0, 0), (-1, -1), 6),
    ('TOPPADDING', (0, 1), (-1, -1), 4),
    ('BOTTOMPADDING', (0, 1), (-1, -1), 4),
    
    ('GRID', (0, 0), (-1, -1), 0.75, colors.HexColor('#94A3B8')),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F8FAFC')]),
]))

story.append(t)

doc = SimpleDocTemplate(
    temp_p2,
    pagesize=A4,
    leftMargin=30,
    rightMargin=30,
    topMargin=22,
    bottomMargin=18
)
doc.build(story)

# 3. Create Page 1 (WhatsApp Image)
temp_p1 = 'temp_page1.pdf'
c = canvas.Canvas(temp_p1, pagesize=A4)
# Draw the WhatsApp image to fill the page cleanly
c.drawImage('WhatsApp Image 2026-10-12 at 15.10.18.jpeg', 0, 0, width=a4_w, height=a4_h)
c.save()

# 4. Merge Page 1 and Page 2 into final PDF
final_doc = pymupdf.open()
doc1 = pymupdf.open(temp_p1)
doc2 = pymupdf.open(temp_p2)

final_doc.insert_pdf(doc1)
final_doc.insert_pdf(doc2)

output_name = 'daa final lab sheet.pdf'
final_doc.save(output_name)
print(f'Successfully created {output_name} with {len(final_doc)} pages!')

# 5. Render previews of both pages
for idx, page in enumerate(final_doc):
    pix = page.get_pixmap(dpi=150)
    pix.save(f'final_page_{idx+1}.png')
print('Rendered final_page_1.png and final_page_2.png')
