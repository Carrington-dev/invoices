# Invoice/PDF Generation Tutorial - Multi-Language & Library Overview

Welcome to the **Invoice or PDF Generation Tutorial**! This guide covers generating PDFs using different programming languages (Python, JavaScript, and Java) with several popular libraries such as **WeasyPrint, PDFReactor, Paged.js,** and others. 

---

## Table of Contents
1. [Overview](#overview)  
2. [Prerequisites](#prerequisites)  
3. [Supported Languages and Libraries](#supported-languages-and-libraries)  
4. [Getting Started](#getting-started)  
5. [Code Examples](#code-examples)  
6. [Library Comparisons](#library-comparisons)  
7. [Contributing](#contributing)  
8. [License](#license)  

---

## Overview
This tutorial demonstrates how to create invoices or PDFs using various tools across multiple languages and frameworks. Whether you need simple PDF generation or advanced styling with CSS, this guide will walk you through several approaches to cover your needs.

---

## Prerequisites
- Basic knowledge of **HTML/CSS** (for styling PDF templates)
- Familiarity with at least one programming language (Python, JavaScript, or Java)  
- Libraries or tools installed based on your preferred approach  
  - Python: `pip`  
  - JavaScript: `npm`  
  - Java: Maven or Gradle  

---

## Supported Languages and Libraries
Below are the libraries covered in this tutorial:

| **Language** | **Library**   | **Features**                                   |
|--------------|---------------|------------------------------------------------|
| Python       | WeasyPrint    | CSS support, HTML to PDF conversion            |
| Python       | ReportLab     | Custom PDF generation using Python scripts     |
| JavaScript   | Paged.js      | Paginated web content to PDFs using CSS rules  |
| JavaScript   | Puppeteer     | Headless Chrome for PDF generation             |
| Java         | PDFReactor    | HTML-to-PDF converter with CSS support         |
| JavaScript   | jsPDF         | Client-side PDF creation                       |

---

## Getting Started

### Installation

#### Python: WeasyPrint
```bash
pip install weasyprint
```

#### JavaScript: Paged.js  
```bash
npm install pagedjs
```

#### Java: PDFReactor  
Make sure to download the PDFReactor SDK [here](https://www.pdfreactor.com).

---

## Code Examples

### 1. **Python + WeasyPrint**
```python
from weasyprint import HTML

HTML('invoice.html').write_pdf('invoice.pdf')
```

### 2. **JavaScript + Paged.js**
```javascript
import paged from 'pagedjs';

const content = document.getElementById('invoice-content');
paged.preview(content).then(pdf => {
  pdf.save('invoice.pdf');
});
```

### 3. **Java + PDFReactor**
```java
import com.realobjects.pdfreactor.PDFreactor;

public class InvoiceGenerator {
    public static void main(String[] args) {
        PDFreactor pdfReactor = new PDFreactor();
        pdfReactor.convertHTML("invoice.html", "invoice.pdf");
    }
}
```

---

## Library Comparisons

| **Feature**            | **WeasyPrint** | **PDFReactor** | **Paged.js** | **ReportLab** | **Puppeteer** |
|------------------------|----------------|---------------|--------------|--------------|--------------|
| CSS Support            | ✔️             | ✔️            | ✔️           | ❌           | ✔️           |
| HTML to PDF Conversion | ✔️             | ✔️            | ✔️           | ❌           | ✔️           |
| Headless Browser       | ❌             | ❌            | ❌           | ❌           | ✔️           |
| Ease of Use            | ⭐⭐⭐⭐          | ⭐⭐⭐          | ⭐⭐⭐⭐⭐       | ⭐⭐⭐          | ⭐⭐⭐⭐        |

---

## Contributing
Contributions are welcome! If you would like to add more libraries or examples, feel free to submit a pull request or open an issue.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

---

This guide offers flexibility for developers who prefer different tools or languages. Choose the one that best fits your project needs!
