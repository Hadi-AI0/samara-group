#!/usr/bin/env python3
"""
Fix HTML lang and dir attributes for Arabic pages at root level.
"""

import os
import re

def fix_arabic_page(filepath):
    """Fix HTML lang and dir attributes in an Arabic HTML file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix html tag - should be lang="ar" dir="rtl"
    content = re.sub(r'<html lang="en" dir="ltr">', '<html lang="ar" dir="rtl">', content)
    
    # Fix canonical URL - should point to root (Arabic version)
    content = re.sub(
        r'<link rel="canonical" href="https://samara\.co\.com/en/" />',
        '<link rel="canonical" href="https://samara.co.com" />',
        content
    )
    
    # Fix x-default - should point to Arabic (root)
    content = re.sub(
        r'<link rel="alternate" hreflang="x-default" href="https://samara\.co\.com/en/" />',
        '<link rel="alternate" hreflang="x-default" href="https://samara.co.com" />',
        content
    )
    
    # Remove ltr.css from Arabic pages (only needed for English)
    content = re.sub(r'\s*<link rel="stylesheet" href="css/ltr\.css">', '', content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  Fixed Arabic page: {filepath}")

def main():
    workspace = '/workspace'
    
    # Get all HTML files at root level (Arabic versions)
    html_files = []
    for filename in os.listdir(workspace):
        if filename.endswith('.html') and os.path.isfile(os.path.join(workspace, filename)):
            html_files.append(os.path.join(workspace, filename))
    
    print(f"Found {len(html_files)} Arabic HTML files to fix")
    
    for filepath in html_files:
        fix_arabic_page(filepath)
    
    print("\nFix complete!")

if __name__ == '__main__':
    main()
