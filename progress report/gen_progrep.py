import csv
import reportlab
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, PageBreak
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

RECORDS_PATH = './PR_source.csv'
FONT_PATH = './fonts/'
PID_IDX = 0
NAME_IDX = 1
EMAIL_IDX = 2
TIMELOG_IDXS = [3,4,5,6,7]
TIMELOG_NAMES = ['Week 0+1','Week 2','Week 3','Week 4','Week 5']
DISCUSSION_IDXS = [8,9,11,13,15,17]
PRACTICUM_IDXS = [10,12,14,16,18]
PPTSIGNUP_IDX = 19
MISSWEEKLYREFLECT = 20
HAVETODONEXT = 21
MISSDISCUSSION_IDX = 22
MISSPRACTICUM_IDX = 23
MISSOBSREFLECT_IDX = 24

headings = dict()
WEEKLY_REFLECT_HDR = 'Weekly reflection+time logs submitted'
PARTICIPATION_HDR = 'Participation'
ASSIGNMENT_HDR = 'Assignments'
SUMMARY_HDR = 'Summary'

GENERATE_TEMPLATE = True

template_doc = SimpleDocTemplate("template.pdf")
report_doc = SimpleDocTemplate("report.pdf")
style_sheet = getSampleStyleSheet()
para_style = style_sheet['BodyText']
hdr_style = style_sheet['Heading3']
report_flowables = []
template_flowables = []
csv_reader = []

csv_reader = csv.reader(open(RECORDS_PATH, 'r'))

if GENERATE_TEMPLATE:
	template_flowables.append(Paragraph("PID: ", hdr_style))
	template_flowables.append(Paragraph("<br/>", para_style))
	template_flowables.append(Paragraph("<br/>", para_style))
	template_flowables.append(Paragraph("Name: ", hdr_style))
	template_flowables.append(Paragraph("<br/>", para_style))
	template_flowables.append(Paragraph("<br/>", para_style))
	template_flowables.append(Paragraph("Email: ", hdr_style))
	template_flowables.append(Paragraph("<br/>", para_style))
	template_flowables.append(Paragraph("<br/>", para_style))
	template_flowables.append(Paragraph(f"{WEEKLY_REFLECT_HDR}: ", hdr_style))
	template_flowables.append(Paragraph("<br/>", para_style))
	template_flowables.append(Paragraph("<br/>", para_style))
	template_flowables.append(Paragraph(f"{PARTICIPATION_HDR}: ", hdr_style))
	template_flowables.append(Paragraph("<br/>", para_style))
	template_flowables.append(Paragraph("<br/>", para_style))
	template_flowables.append(Paragraph(f"{ASSIGNMENT_HDR}: ", hdr_style))
	template_flowables.append(Paragraph("<br/>", para_style))
	template_flowables.append(Paragraph("<br/>", para_style))
	template_flowables.append(Paragraph(f"{SUMMARY_HDR}: ", hdr_style))
	template_flowables.append(PageBreak())
	template_doc.build(template_flowables)

next(csv_reader)
for row in csv_reader :
	# name = row[FIRST_NAME_IDX] + ' ' + row[LAST_NAME_IDX]
	name = row[NAME_IDX]
	report_flowables.append(Paragraph("PID: &nbsp; {}".format(row[PID_IDX]), hdr_style))
	report_flowables.append(Paragraph("<br/>", para_style))
	report_flowables.append(Paragraph("<br/>", para_style))
	report_flowables.append(Paragraph("Name: &nbsp; {}".format(name), hdr_style))
	report_flowables.append(Paragraph("<br/>", para_style))
	report_flowables.append(Paragraph("<br/>", para_style))
	report_flowables.append(Paragraph("Email: &nbsp; {}".format(row[EMAIL_IDX]), hdr_style))
	report_flowables.append(Paragraph("<br/>", para_style))
	report_flowables.append(Paragraph("<br/>", para_style))
	report_flowables.append(Paragraph(f"{WEEKLY_REFLECT_HDR}: ", hdr_style))
	report_flowables.append(Paragraph("<br/>", para_style))
	
	for i, rowidx in enumerate(TIMELOG_IDXS):
		if(row[rowidx] == 'TRUE'):
			report_flowables.append(Paragraph(f"Submitted {TIMELOG_NAMES[i]}", para_style))
		else:
			report_flowables.append(Paragraph(f"{TIMELOG_NAMES[i]} PENDING", para_style))
		report_flowables.append(Paragraph("<br/>", para_style))
	report_flowables.append(Paragraph("<br/>", para_style))
	report_flowables.append(Paragraph("<br/>", para_style))

	report_flowables.append(Paragraph(f"{PARTICIPATION_HDR}: ", hdr_style))
	report_flowables.append(Paragraph("<br/>", para_style))
	for i, rowidx in enumerate(DISCUSSION_IDXS):
		if(row[rowidx] == 'TRUE'):
			report_flowables.append(Paragraph(f"Discussion Attendance Recorded for Week {i}", para_style))
		else:
			report_flowables.append(Paragraph(f"Discussion Attendance NOT RECORDED for Week {i}", para_style))
		report_flowables.append(Paragraph("<br/>", para_style))
	report_flowables.append(Paragraph("<br/>", para_style))
	report_flowables.append(Paragraph("<br/>", para_style))

	for i, rowidx in enumerate(PRACTICUM_IDXS):
		if(row[rowidx] == 'TRUE'):
			report_flowables.append(Paragraph(f"Practicum Attendance Recorded for Week {i+1}", para_style))
		else:
			report_flowables.append(Paragraph(f"Practicum Attendance NOT RECORDED for Week {i+1}", para_style))
		report_flowables.append(Paragraph("<br/>", para_style))
	report_flowables.append(Paragraph("<br/>", para_style))
	report_flowables.append(Paragraph("<br/>", para_style))

	report_flowables.append(Paragraph(f"{ASSIGNMENT_HDR}: ", hdr_style))
	report_flowables.append(Paragraph("<br/>", para_style))
	if row[PPTSIGNUP_IDX] == 'FALSE':
		#need to sign up for ppt
		report_flowables.append(Paragraph("Need to sign up for presentation", para_style))
	else:
		report_flowables.append(Paragraph("Signed up for presentation", para_style))
	report_flowables.append(Paragraph("<br/>", para_style))

	if row[MISSOBSREFLECT_IDX] == 'TRUE':
		#need to sign up for ppt
		report_flowables.append(Paragraph("Need to submit Observation Reflection", para_style))
	else:
		report_flowables.append(Paragraph("Observation Reflection Submitted", para_style))

	report_flowables.append(Paragraph("<br/>", para_style))
	report_flowables.append(Paragraph("<br/>", para_style))

	report_flowables.append(Paragraph(f"{SUMMARY_HDR}: ", hdr_style))
	report_flowables.append(Paragraph("<br/>", para_style))
	on_track = True

	if(row[HAVETODONEXT] == 'TRUE'):
		#need to complete the next weekly reflection
		report_flowables.append(Paragraph("You must complete the next weekly reflection+time log to stay on track for satisfying the passing requirements for this class.", para_style))
		report_flowables.append(Paragraph("<br/>", para_style))
		on_track = False
	if(row[MISSDISCUSSION_IDX] == 'TRUE'):
		#need to complete discussion make-up
		report_flowables.append(Paragraph("You must complete missing make-up work for the Missed Discussion(s) to stay on track for satisfying the passing requirements for this class.", para_style))		
		report_flowables.append(Paragraph("<br/>", para_style))
		on_track = False
	if(row[MISSPRACTICUM_IDX] == 'TRUE'):
		#need to complete practicum make-up
		report_flowables.append(Paragraph("You must complete missing make-up work for the Missed Practicum(s) to stay on track for satisfying the passing requirements for this class.", para_style))		
		report_flowables.append(Paragraph("<br/>", para_style))
		on_track = False
	if(row[PPTSIGNUP_IDX] == 'FALSE'):
		#need to sign up for ppt 
		report_flowables.append(Paragraph("You must sign up for a presentation slot to stay on track for satisfying the passing requirements for this class.", para_style))		
		report_flowables.append(Paragraph("<br/>", para_style))
		on_track = False

	if(row[MISSOBSREFLECT_IDX] == 'TRUE'): 
		report_flowables.append(Paragraph("You still have to complete your Observation Reflection Assignment.", para_style))		
		report_flowables.append(Paragraph("<br/>", para_style))

	if on_track:
		report_flowables.append(Paragraph("You are on track for satisfying the passing requirements for this class.", para_style))		
		report_flowables.append(Paragraph("<br/>", para_style))
	report_flowables.append(Paragraph("<br/>", para_style))


	report_flowables.append(PageBreak())

report_doc.build(report_flowables)