#!/usr/bin/env python3
"""
Fix remaining Vision 2030 translations in all Arabic HTML pages.
"""

import os
import re

def fix_vision_2030(filepath):
    """Fix Vision 2030 references in an HTML file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix "Saudi Vision 2030" mixed translations
    content = re.sub(r'Saudi الرؤية 2030', 'رؤية السعودية 2030', content)
    content = re.sub(r'الرؤية 2030', 'رؤية 2030', content)
    content = re.sub(r'Future الرؤية', 'رؤية المستقبل', content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  Fixed Vision 2030 in: {filepath}")

def main():
    workspace = '/workspace'
    
    # Get all HTML files at root level (Arabic versions)
    html_files = []
    for filename in os.listdir(workspace):
        if filename.endswith('.html') and os.path.isfile(os.path.join(workspace, filename)):
            html_files.append(os.path.join(workspace, filename))
    
    print(f"Found {len(html_files)} Arabic HTML files to fix")
    
    for filepath in html_files:
        fix_vision_2030(filepath)
    
    print("\nFix complete!")

if __name__ == '__main__':
    main()
