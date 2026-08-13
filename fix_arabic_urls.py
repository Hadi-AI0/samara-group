#!/usr/bin/env python3
import re
import os

# Mapping of translated URLs/paths to their correct English versions
url_mapping = {
    # Canonical and alternate URLs
    'https://سمارى.co.com': 'https://samara.co.com',
    
    # Image sources
    'سمارى-logo-group.png': 'samara-logo-group.png',
    
    # HTML file links
    'سمارى-تبريد و تكييف.html': 'samara-H-VACR.html',
    'سمارى-parking.html': 'samara-parking.html',
    'سمارى-real-estate.html': 'samara-real-estate.html',
    'بيلميكس.html': 'builmix.html',
    'Saudi بيلميكس.html': 'builmix.html',
    'سالمية-oasis.html': 'salmiya-oasis.html',
    'سريرية للرعاية الصحية.html': 'saryryah-healthcare.html',
    'مهارة للتوظيف.html': 'mahara-recruitment.html',
    
    # Email addresses
    'info@سمارىgroup.biz': 'info@samaragroup.biz',
    'info@سمارىgroup.co.com': 'info@samaragroup.co.com',
    
    # Social media links
    'https://www.linkedin.com/company/سمارىgroup-sa/': 'https://www.linkedin.com/company/samaragroup-sa/',
    'https://x.com/سمارىgroup_sa': 'https://x.com/samaragroup_sa',
    'https://www.facebook.com/سمارىgroup.sa/': 'https://www.facebook.com/samaragroup.sa/',
}

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Replace URLs and paths
    for arabic_url, english_url in url_mapping.items():
        # Escape special regex characters
        arabic_url_escaped = re.escape(arabic_url)
        content = re.sub(arabic_url_escaped, english_url, content)
    
    # Fix canonical URL in head section - ensure it's samara.co.com
    content = re.sub(
        r'<link rel="canonical" href="https://samara\.co\.com/en/" />',
        '<link rel="canonical" href="https://samara.co.com" />',
        content
    )
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed: {filepath}")
        return True
    return False

# Fix all Arabic HTML files (root level)
arabic_files = [
    '/workspace/index.html',
    '/workspace/builmix.html',
    '/workspace/mahara-recruitment.html',
    '/workspace/salmiya-oasis.html',
    '/workspace/samara-H-VACR.html',
    '/workspace/samara-parking.html',
    '/workspace/samara-real-estate.html',
    '/workspace/saryryah-healthcare.html',
]

for filepath in arabic_files:
    if os.path.exists(filepath):
        fix_file(filepath)

print("Done fixing Arabic pages!")
