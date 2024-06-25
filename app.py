from weasyprint import HTML

# Path to the HTML invoice template
html_path = 'invoice.html'

# Output path for the generated PDF
pdf_path = 'invoice.pdf'

# Generate PDF
HTML(html_path).write_pdf(pdf_path)

print(f'Invoice generated and saved to {pdf_path}')
