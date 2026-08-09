#!/usr/bin/env python3
"""
Translate meta description for Arabic pages - final attempt.
"""

import os
import re

def translate_meta(filepath):
    """Translate meta description in an Arabic HTML file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Translate meta description using a more flexible pattern
    old_pattern = r'<meta name="description" content="[^"]*Samara Group[^"]*"'
    new_desc = '<meta name="description" content="مجموعة سمارة - بناء مستقبل المملكة العربية السعودية. مجموعة أعمال عائلية متنوعة مع أكثر من 40 عامًا من التميز في جميع أنحاء دول مجلس التعاون الخليجي."'
    content = re.sub(old_pattern, new_desc, content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  Translated meta: {filepath}")

def main():
    workspace = '/workspace'
    
    # Get all HTML files at root level (Arabic versions)
    html_files = []
    for filename in os.listdir(workspace):
        if filename.endswith('.html') and os.path.isfile(os.path.join(workspace, filename)):
            html_files.append(os.path.join(workspace, filename))
    
    print(f"Found {len(html_files)} Arabic HTML files to fix")
    
    for filepath in html_files:
        translate_meta(filepath)
    
    print("\nFix complete!")

if __name__ == '__main__':
    main()
