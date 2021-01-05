import csv
import reportlab
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, PageBreak
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

WEEKNO = 'X'
RECORDS_PATH = f'./Week{WEEKNO}.csv'
FONT_PATH = './fonts/'
PID_IDX = 0
LAST_NAME_IDX = 1
FIRST_NAME_IDX = 2
EMAIL_IDX = 3
DISCUSSION_ATDC_IDX = 4
PRACTICUM_ATDC_IDX = 5

GENERATE_TEMPLATE = True

reportlab.rl_config.TTFSearchPath.append(FONT_PATH)
pdfmetrics.registerFont(TTFont('CedarvilleCursive', 'CedarvilleCursive-Regular.ttf'))
pdfmetrics.registerFont(TTFont('DOANewDay', 'DawningofaNewDay-Regular.ttf'))
pdfmetrics.registerFont(TTFont('NYCD', 'NothingYouCouldDo-Regular.ttf'))
# styles = getSampleStyleSheet()
# para_style = ParagraphStyle(name = 'Attendance',fontName='CedarvilleCursive', fontSize=12)
para_style = ParagraphStyle(name = 'Attendance',fontName='NYCD', fontSize=16)
template_doc = SimpleDocTemplate("template.pdf")

discussion_doc = SimpleDocTemplate(f"discussion{WEEKNO}.pdf")
practicum_doc = SimpleDocTemplate(f"practicum{WEEKNO}.pdf")
style_sheet = getSampleStyleSheet()
para_style = style_sheet['BodyText']

discussion_flowables = []
practicum_flowables = []
template_flowables = []
csv_reader = []

csv_reader = csv.reader(open(RECORDS_PATH, 'r'))

if GENERATE_TEMPLATE:
	template_flowables.append(Paragraph("PID", para_style))
	# template_flowables.append(Paragraph("<br/>", style_sheet['BodyText']))
	# template_flowables.append(Paragraph("<br/>", style_sheet['BodyText']))
	# template_flowables.append(Paragraph("<br/>", style_sheet['BodyText']))
	# template_flowables.append(Paragraph("<br/>", style_sheet['BodyText']))
	# template_flowables.append(Paragraph("<br/>", style_sheet['BodyText']))
	# template_flowables.append(Paragraph("<br/>", style_sheet['BodyText']))
	template_flowables.append(Paragraph("<br/>", style_sheet['BodyText']))
	template_flowables.append(Paragraph("<br/>", style_sheet['BodyText']))
	template_flowables.append(Paragraph("Name", para_style))
	# template_flowables.append(Paragraph("<br/>", style_sheet['BodyText']))
	# template_flowables.append(Paragraph("<br/>", style_sheet['BodyText']))
	# template_flowables.append(Paragraph("<br/>", style_sheet['BodyText']))
	# template_flowables.append(Paragraph("<br/>", style_sheet['BodyText']))
	# template_flowables.append(Paragraph("<br/>", style_sheet['BodyText']))
	# template_flowables.append(Paragraph("<br/>", style_sheet['BodyText']))
	template_flowables.append(Paragraph("<br/>", style_sheet['BodyText']))
	template_flowables.append(Paragraph("<br/>", style_sheet['BodyText']))
	# template_flowables.append(Paragraph("<br/>", para_style))
	template_flowables.append(Paragraph("Email", para_style))
	template_flowables.append(PageBreak())
	template_doc.build(template_flowables)


next(csv_reader)
for row in csv_reader :
	if row[DISCUSSION_ATDC_IDX] == 'TRUE':
		# name = row[LAST_NAME_IDX] + ", " + row[FIRST_NAME_IDX]
		name = row[FIRST_NAME_IDX] + ' ' + row[LAST_NAME_IDX]
		discussion_flowables.append(Paragraph("PID &nbsp; {}".format(row[PID_IDX]), para_style))
		# discussion_flowables.append(Paragraph("<br/>", style_sheet['BodyText']))
		# discussion_flowables.append(Paragraph("<br/>", style_sheet['BodyText']))
		# discussion_flowables.append(Paragraph("<br/>", style_sheet['BodyText']))
		# discussion_flowables.append(Paragraph("<br/>", style_sheet['BodyText']))
		# discussion_flowables.append(Paragraph("<br/>", style_sheet['BodyText']))
		# discussion_flowables.append(Paragraph("<br/>", style_sheet['BodyText']))
		discussion_flowables.append(Paragraph("<br/>", style_sheet['BodyText']))
		discussion_flowables.append(Paragraph("<br/>", style_sheet['BodyText']))

		# name = row[ROSTER_NAME_IDX]

		discussion_flowables.append(Paragraph("Name &nbsp; {}".format(name), para_style))
		# discussion_flowables.append(Paragraph("<br/>", style_sheet['BodyText']))
		# discussion_flowables.append(Paragraph("<br/>", style_sheet['BodyText']))
		# discussion_flowables.append(Paragraph("<br/>", style_sheet['BodyText']))
		# discussion_flowables.append(Paragraph("<br/>", style_sheet['BodyText']))
		# discussion_flowables.append(Paragraph("<br/>", style_sheet['BodyText']))
		# discussion_flowables.append(Paragraph("<br/>", style_sheet['BodyText']))
		discussion_flowables.append(Paragraph("<br/>", style_sheet['BodyText']))
		discussion_flowables.append(Paragraph("<br/>", style_sheet['BodyText']))


		# discussion_flowables.append(Paragraph("<br/>", para_style))
		discussion_flowables.append(Paragraph("Email &nbsp; {}".format(row[EMAIL_IDX]), para_style))
		discussion_flowables.append(PageBreak())
	if row[PRACTICUM_ATDC_IDX] == 'TRUE':
		# name = row[LAST_NAME_IDX] + ", " + row[FIRST_NAME_IDX]
		name = row[FIRST_NAME_IDX] + ' ' + row[LAST_NAME_IDX]
		practicum_flowables.append(Paragraph("PID &nbsp; {}".format(row[PID_IDX]), para_style))
		# practicum_flowables.append(Paragraph("<br/>", style_sheet['BodyText']))
		# practicum_flowables.append(Paragraph("<br/>", style_sheet['BodyText']))	
		# practicum_flowables.append(Paragraph("<br/>", style_sheet['BodyText']))
		# practicum_flowables.append(Paragraph("<br/>", style_sheet['BodyText']))		
		# practicum_flowables.append(Paragraph("<br/>", style_sheet['BodyText']))
		# practicum_flowables.append(Paragraph("<br/>", style_sheet['BodyText']))
		practicum_flowables.append(Paragraph("<br/>", style_sheet['BodyText']))
		practicum_flowables.append(Paragraph("<br/>", style_sheet['BodyText']))
		practicum_flowables.append(Paragraph("Name &nbsp; {}".format(name), para_style))
		# practicum_flowables.append(Paragraph("<br/>", style_sheet['BodyText']))
		# practicum_flowables.append(Paragraph("<br/>", style_sheet['BodyText']))	
		# practicum_flowables.append(Paragraph("<br/>", style_sheet['BodyText']))
		# practicum_flowables.append(Paragraph("<br/>", style_sheet['BodyText']))		
		# practicum_flowables.append(Paragraph("<br/>", style_sheet['BodyText']))
		# practicum_flowables.append(Paragraph("<br/>", style_sheet['BodyText']))
		practicum_flowables.append(Paragraph("<br/>", style_sheet['BodyText']))
		practicum_flowables.append(Paragraph("<br/>", style_sheet['BodyText']))
		# practicum_flowables.append(Paragraph("<br/>", para_style))	
		practicum_flowables.append(Paragraph("Email &nbsp; {}".format(row[EMAIL_IDX]), para_style))
		practicum_flowables.append(PageBreak())

discussion_doc.build(discussion_flowables)
practicum_doc.build(practicum_flowables)
