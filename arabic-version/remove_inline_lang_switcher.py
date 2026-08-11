#!/usr/bin/env python3
"""Remove inline onclick handlers from language switcher buttons in HTML files"""

import os
import re

def process_file(filepath):
    """Process a single HTML file"""
    print(f"Processing: {filepath}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Remove onclick attribute from lang-switcher buttons
    content = re.sub(
        r'(<button[^>]*class="lang-switcher"[^>]*id="lang-switcher"[^>]*)\s*onclick="switchLanguage\([\'"][^\'"]+[\'"]\)"',
        r'\1',
        content
    )
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✓ Updated {filepath}")
    else:
        print(f"  - No changes needed")

def main():
    # Process all HTML files (both Arabic and English)
    html_files = []
    
    # Root level Arabic pages
    for f in os.listdir('/workspace'):
        if f.endswith('.html'):
            html_files.append(f'/workspace/{f}')
    
    # English pages
    if os.path.exists('/workspace/en'):
        for f in os.listdir('/workspace/en'):
            if f.endswith('.html'):
                html_files.append(f'/workspace/en/{f}')
    
    print("Removing inline onclick handlers...\n")
    for page in html_files:
        if os.path.exists(page):
            process_file(page)
    
    print("\nDone!")

if __name__ == '__main__':
    main()
