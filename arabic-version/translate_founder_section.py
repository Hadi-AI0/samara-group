#!/usr/bin/env python3
"""
Fix the founder section translation in all Arabic HTML pages.
"""

import os
import re

def fix_founder_section(filepath):
    """Fix the founder section in an HTML file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix the blockquote text
    old_blockquote = r'Since founding Samara Group in 1984, our vision has remained steadfast: to build a legacy rooted in <strong>integrity, quality, and service</strong>\. Over four decades, we have grown from a single refrigeration company into a diversified conglomerate\. As Saudi Arabia strides toward.*?الرؤية 2030.*?, we stand ready to shape the future through infrastructure, healthcare, and innovation\.'
    
    new_blockquote = 'منذ تأسيس مجموعة سمارة عام 1984، ظلت رؤيتنا راسخة: بناء إرث قائم على <strong>النزاهة والجودة والخدمة</strong>. على مدى أربعة عقود، نما我们从 شركة تبريد واحدة إلى مجمع متنوع. ومع تقدم المملكة العربية السعودية نحو رؤية 2030، نحن مستعدون لتشكيل المستقبل من خلال البنية التحتية والرعاية الصحية والابتكار.'
    
    # More targeted replacement
    content = re.sub(
        r'<blockquote>\s*Since founding Samara Group in 1984[^<]*?<strong>integrity, quality, and service</strong>[^<]*?Over four decades[^<]*?As Saudi Arabia strides toward[^<]*?الرؤية 2030[^<]*?we stand ready to shape the future through infrastructure, healthcare, and innovation\.\s*</blockquote>',
        '<blockquote>\n           منذ تأسيس مجموعة سمارة عام 1984، ظلت رؤيتنا راسخة: بناء إرث قائم على <strong>النزاهة والجودة والخدمة</strong>. على مدى أربعة عقود، نمونا من شركة تبريد واحدة إلى مجمع متنوع. ومع تقدم المملكة العربية السعودية نحو رؤية 2030، نحن مستعدون لتشكيل المستقبل من خلال البنية التحتية والرعاية الصحية والابتكار.\n          </blockquote>',
        content,
        flags=re.DOTALL
    )
    
    # Fix "The Founder" text
    content = re.sub(r'<cite>The المؤسس<br>', '<cite>المؤسس<br>', content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  Fixed founder section in: {filepath}")

def main():
    workspace = '/workspace'
    
    # Get all HTML files at root level (Arabic versions)
    html_files = []
    for filename in os.listdir(workspace):
        if filename.endswith('.html') and os.path.isfile(os.path.join(workspace, filename)):
            html_files.append(os.path.join(workspace, filename))
    
    print(f"Found {len(html_files)} Arabic HTML files to fix")
    
    for filepath in html_files:
        fix_founder_section(filepath)
    
    print("\nFix complete!")

if __name__ == '__main__':
    main()
