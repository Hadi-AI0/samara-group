#!/usr/bin/env python3
"""
Fix HTML comments in all Arabic HTML pages.
"""

import os
import re

def fix_comments(filepath):
    """Fix HTML comments in an HTML file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix the Saudi Vision 2030 comment
    content = re.sub(r'<!-- Saudi Vision 2030 Badge -->', '<!-- شعار رؤية السعودية 2030 -->', content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  Fixed comments in: {filepath}")

def main():
    workspace = '/workspace'
    
    # Get all HTML files at root level (Arabic versions)
    html_files = []
    for filename in os.listdir(workspace):
        if filename.endswith('.html') and os.path.isfile(os.path.join(workspace, filename)):
            html_files.append(os.path.join(workspace, filename))
    
    print(f"Found {len(html_files)} Arabic HTML files to fix")
    
    for filepath in html_files:
        fix_comments(filepath)
    
    print("\nFix complete!")

if __name__ == '__main__':
    main()
