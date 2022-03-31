To continue following this tutorial we will need the following Python libraries: pdf2docx and docx2pdf.
If you don’t have it installed, please open “Command Prompt” (on Windows) and install it using the following code:

> pip install pdf2docx
> pip install docx2pdf

Convert all pages from PDF file to docx format using Python
Method 1:

First step is to import the required dependencies:

> from pdf2docx import Converter

Second step is to define input and output paths. The input path should be the path to your PDF file, and the output path should be the path to where you would like to write out the .docx file to (in our case it’s just filenames since the code and the files are located in the same directory):

> pdf_file = 'sample.pdf'
> docx_file = 'sample.docx'

Third step is to convert PDF file to .docx:

> cv = Converter(pdf_file)
> cv.convert(docx_file)
> cv.close()

And you should see the sample.docx created in the same directory.

Method 2:

First step is to import the required dependencies:

> from pdf2docx import parse

Second step is to define input and output paths. The input path should be the path to your PDF file, and the output path should be the path to where you would like to write out the .docx file to (in our case it’s just filenames since the code and the files are located in the same directory):

> pdf_file = 'sample.pdf'
> docx_file = 'sample.docx'

Third step is to convert PDF file to .docx:

> parse(pdf_file, docx_file)

And you should see the sample.docx created in the same directory.

Convert a single page from PDF file to docx format using Python
First step is to import the required dependencies:

> from pdf2docx import Converter

Second step is to define input and output paths. The input path should be the path to your PDF file, and the output path should be the path to where you would like to write out the .docx file to (in our case it’s just filenames since the code and the files are located in the same directory):

> pdf_file = 'sample.pdf'
> docx_file = 'sample.docx'

Third step is to define a list with the numbers of pages you would like to be converted. In our case, the PDF file has 2 pages and let’s say we would like to print the first one. We would define a pages_list and assign the index number of the page (first page is index 0).

> pages_list = [0]

Fourth step is to convert PDF file specific pages to .docx:

> cv = Converter(pdf_file)
> cv.convert(docx_file, pages=pages_list)
> cv.close()

How to convert docx files to PDF format using Python
Using docx2pdf library, we can perform the conversion in a few lines of code. This library is quite extensive and I encourage readers to check out their official documentation to learn more about its capabilities.

First step is to import the required dependencies:

> from docx2pdf import convert

Second step is to define input and output paths. The input path should be the path to your PDF file, and the output path should be the path to where you would like to write out the .docx file to (in our case it’s just filenames since the code and the files are located in the same directory):

> docx_file = 'input.docx'
> pdf_file = 'output.pdf'

Third step is to convert the .docx file to PDF:

> convert(docx_file, pdf_file)

And you should see the output.pdf created in the same directory.

