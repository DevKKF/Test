from weasyprint import HTML

# Test simple
HTML(string='<h1>Hello, WeasyPrint!</h1>').write_pdf('test.pdf')

print("PDF généré avec succès.")
