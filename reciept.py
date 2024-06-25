from weasyprint import HTML
from jinja2 import Template

# Sample data
data = {
    "date": "2024-06-25",
    "receipt_number": "123456",
    "customer_name": "John Doe",
    "customer_email": "johndoe@example.com",
    "items": [
        {"description": "Product 1", "quantity": 2, "price": "$10.00"},
        {"description": "Product 2", "quantity": 1, "price": "$20.00"}
    ],
    "total_amount": "$40.00"
}

# Load HTML template
with open("reciept.html") as f:
    template = Template(f.read())

# Render HTML with data
html_content = template.render(data)

# Generate PDF
HTML(string=html_content).write_pdf("receipt.pdf")
