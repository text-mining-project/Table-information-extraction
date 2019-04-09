# Table Information Extraction Based on PDFMiner

Our goal is to extract the tabular data from the PDF file in the field of Biochar. 
The reason for doing this is that there are often a lot of papers in this field that contain tabular data and therefore
it is often time consuming to extract data manually. Besides, unlike the field in some medical field,
most forms in the bioenergy field are presented as a three-line table so we could 
consider a general approach to parsing and extracting these tables.


Our preparatory work was based on [PDFminer](https://github.com/euske/pdfminer/) which 
has various capabilities for working with PDF files (we are only interested in one of them, the ability to parse them into HTML)

Workflow
---

- Obtain the related paper from DOCX file (2326587T_LeiyuTian_ENG5059P_FinalReport_2018.docx)
- Using web crawler or artificial extraction to extract the corresponding papers in batches.
- Using PDFminer convert it to HTML files in bulk.
- Recognize the parts of the table in the HTML and extract them separately (As figure shown below).
<img src='flow chart.png'>
- We use our regulation and method to get table information.
- Export the extracted information to an excel file


*Our work mainly focuses on the last two items.*

**Compare With Other Software**
# PDFTables
  When converting a PDF to a spreadsheet, an algorithm is used which examines the structures in the PDF. It understands the spacing
  between items to identify the rows and columns, much as human’s eye does when scanning a page.  It is designed to work reliably with
  large quantities of data to produce the best output from given PDF. 
# PDFtoXLS
  This includes several steps. Quality Conversions. Table Recovery. Headers and Footers. Form Recognition. Rotated Text Recovery. Hyper-
  -link Detection. Merging logical tables. List detection. OCR. It is able to extract comparatively complete information from pdf files.
# SimplyPDF
  It is a free and easy way to use online PDF to XLS converter to extract tables trapped in PDF files, without having to install any
  software. This software is capable of extracting relatively complicated tables.
 
All the testing result can be seen in the paperfile.


*All software here are not open-source and require pricing except SimplyPDF.*


COPYRIGHT
-----------------------------------------------------------

    Copyright 2019, 2019 Table-mining group
    Contact: lomo123456@foxmail.com

    you can redistribute our method and/or modify
    it under the terms of the MIT License as published 

    our method is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    MIT License for more details.

    You should have received a copy of the MIT license
    along with it.  If not, see <https://github.com/text-mining-project/Table-information-extraction/blob/master/LICENSE>.

-----------------------------------------------------------
