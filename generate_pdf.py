import markdown
import os
import sys

# List of files to include in order
files = [
    "unit_3_network_layer.md",
    "unit_4_transport_layer.md",
    "unit_5_application_layer.md",
    "unit_6_network_security.md",
    "glossary.md"
]

output_html = "study_guide.html"
output_pdf = "Network_Theory_Study_Guide.pdf"
css_file = "styles.css"

def generate_pdf():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Network Theory Exam Study Guide</title>
        <link rel="stylesheet" href="styles.css">
    </head>
    <body>
        <div class="title-page">
            <h1>Network Theory Exam Study Guide</h1>
            <p>Comprehensive Guide for Units III-VI</p>
            <p>Undergraduate Level</p>
        </div>
        <div class="toc">
            <h2>Table of Contents</h2>
            <ul>
                <li>Unit III: Network Layer</li>
                <li>Unit IV: Transport Layer</li>
                <li>Unit V: Application Layer</li>
                <li>Unit VI: Network Security</li>
                <li>Glossary</li>
            </ul>
        </div>
    """

    for filename in files:
        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as f:
                md_text = f.read()
                # Convert Markdown to HTML
                html_segment = markdown.markdown(md_text, extensions=['tables', 'fenced_code'])
                html_content += f"<div class='section'>{html_segment}</div><hr>"
        else:
            print(f"Warning: {filename} not found.")

    html_content += """
    </body>
    </html>
    """

    # Write HTML file
    with open(output_html, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print(f"HTML generated: {output_html}")

    # Convert to PDF using WeasyPrint if available
    try:
        from weasyprint import HTML, CSS
        HTML(output_html).write_pdf(output_pdf, stylesheets=[CSS(css_file)])
        print(f"PDF generated successfully: {output_pdf}")
    except ImportError:
        print("WeasyPrint not found. Please install it using: pip install weasyprint")
        print("Alternatively, you can open 'study_guide.html' in your browser and 'Print to PDF'.")
    except Exception as e:
        print(f"Error generating PDF: {e}")

if __name__ == "__main__":
    generate_pdf()
