from weasyprint import HTML

# Path to the HTML invoice template
html_path = 'ticket.html'

# Output path for the generated PDF
pdf_path = 'ticket.pdf'

# Generate PDF
HTML(html_path).write_pdf(pdf_path)

print(f'Ticket generated and saved to {pdf_path}')
