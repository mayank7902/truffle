from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO

# Create a PDF document
doc = SimpleDocTemplate("feedback.pdf", pagesize=letter)
elements = []

# Title
styles = getSampleStyleSheet()
elements.append(Paragraph("Interview Feedback Report", styles["Title"]))
elements.append(Spacer(1, 12))

# Feedback text
feedback_text = "Dear Student, Thank you for participating in the interview. Here is your feedback:"
elements.append(Paragraph(feedback_text, styles["Normal"]))
elements.append(Spacer(1, 12))

# Visualizations
# Bar chart for "Technical Skills"
plt.figure(figsize=(6, 4))
data = {'Behavior': 8, 'Communication': 7, 'Confidence': 9, 'Problem Solving': 7}
categories = list(data.keys())
values = list(data.values())

# Change the color of each bar
colors_list = ['skyblue', 'lightgreen', 'lightcoral', 'lightpink']

bars = plt.bar(categories, values, color=colors_list)

# Add border to each bar
for bar in bars:
    bar.set_edgecolor('black')

plt.xlabel('Categories')
plt.ylabel('Scores')
plt.title('Interview Scores - Technical Skills')

# Save the plot to a buffer
buffer = BytesIO()
plt.savefig(buffer, format='png')
buffer.seek(0)

# Add the image to the PDF
elements.append(Image(buffer, width=400, height=300))
elements.append(Spacer(1, 12))

# Add scores for each parameter on a new line
elements.append(Paragraph("Interview Scores:", styles["Heading2"]))
for category, score in data.items():
    elements.append(Paragraph(f"{category}: {score}", styles["Normal"]))
    elements.append(Spacer(1, 6))  # Add some space between each line

# Closing message
closing_message = "We appreciate your time and effort. Good luck with your future endeavors!"
elements.append(Paragraph(closing_message, styles["Normal"]))

# Build the PDF document
doc.build(elements)
