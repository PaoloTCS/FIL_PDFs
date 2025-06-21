#!/usr/bin/env python3
"""
PDF to Markdown Converter
Converts PDF files in the current directory to Markdown files in the md_files folder.
"""

import os
import re
import sys
from pathlib import Path
import PyPDF2
import fitz  # PyMuPDF
import argparse

def clean_text(text):
    """Clean and format extracted text for Markdown."""
    if not text:
        return ""
    
    # Remove excessive whitespace
    text = re.sub(r'\s+', ' ', text)
    
    # Remove page numbers and headers/footers
    text = re.sub(r'\b\d+\s*$', '', text, flags=re.MULTILINE)
    
    # Clean up line breaks
    text = re.sub(r'\n\s*\n', '\n\n', text)
    
    # Remove leading/trailing whitespace
    text = text.strip()
    
    return text

def extract_text_with_pymupdf(pdf_path):
    """Extract text using PyMuPDF (more reliable than PyPDF2)."""
    try:
        doc = fitz.open(pdf_path)
        text = ""
        
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text += page.get_text()
        
        doc.close()
        return clean_text(text)
    except Exception as e:
        print(f"Error extracting text from {pdf_path}: {e}")
        return None

def extract_text_with_pypdf2(pdf_path):
    """Fallback text extraction using PyPDF2."""
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            
            for page in reader.pages:
                text += page.extract_text() + "\n"
            
            return clean_text(text)
    except Exception as e:
        print(f"Error extracting text from {pdf_path}: {e}")
        return None

def pdf_to_markdown(pdf_path, output_dir):
    """Convert a PDF file to Markdown format."""
    pdf_name = Path(pdf_path).stem
    md_path = output_dir / f"{pdf_name}.md"
    
    print(f"Converting {pdf_path} to {md_path}...")
    
    # Try PyMuPDF first (better text extraction)
    text = extract_text_with_pymupdf(pdf_path)
    
    # Fallback to PyPDF2 if PyMuPDF fails
    if text is None:
        text = extract_text_with_pypdf2(pdf_path)
    
    if text is None:
        print(f"Failed to extract text from {pdf_path}")
        return False
    
    # Create markdown content
    markdown_content = f"""# {pdf_name.replace('_', ' ').replace('-', ' ')}

{text}

---
*Converted from PDF: {pdf_path}*
"""
    
    # Write to markdown file
    try:
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        print(f"Successfully converted {pdf_path} to {md_path}")
        return True
    except Exception as e:
        print(f"Error writing markdown file {md_path}: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description='Convert PDF files to Markdown format')
    parser.add_argument('--input-dir', default='.', help='Input directory containing PDFs (default: current directory)')
    parser.add_argument('--output-dir', default='md_files', help='Output directory for markdown files (default: md_files)')
    parser.add_argument('--files', nargs='+', help='Specific PDF files to convert')
    
    args = parser.parse_args()
    
    # Create output directory if it doesn't exist
    output_dir = Path(args.output_dir)
    output_dir.mkdir(exist_ok=True)
    
    # Get list of PDF files to convert
    if args.files:
        pdf_files = [Path(f) for f in args.files if f.endswith('.pdf')]
    else:
        input_dir = Path(args.input_dir)
        pdf_files = list(input_dir.glob('*.pdf'))
    
    if not pdf_files:
        print("No PDF files found to convert.")
        return
    
    print(f"Found {len(pdf_files)} PDF files to convert:")
    for pdf_file in pdf_files:
        print(f"  - {pdf_file}")
    
    # Convert each PDF
    successful = 0
    failed = 0
    
    for pdf_file in pdf_files:
        if pdf_to_markdown(pdf_file, output_dir):
            successful += 1
        else:
            failed += 1
    
    print(f"\nConversion complete: {successful} successful, {failed} failed")

if __name__ == "__main__":
    main() 