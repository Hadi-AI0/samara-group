#!/usr/bin/env python3
"""
Translate English content to Arabic for all HTML pages.
This script replaces English text with proper Arabic translations.
"""

import os
import re

# Comprehensive translation dictionary for website content
TRANSLATIONS = {
    # Navigation
    "Companies": "الشركات",
    "About": "من نحن",
    "Founder": "المؤسس",
    "Journey": "رحلتنا",
    "Manufacturing": "التصنيع",
    "Ecosystem": "النظام البيئي",
    "Board": "مجلس الإدارة",
    "Labor": "العمالة",
    "Projects": "المشاريع",
    "Contact": "اتصل بنا",
    
    # Hero Section
    "ESTABLISHED 1984": "تأسست عام 1984",
    "Where Heritage Meets Ambition": "حيث يلتقي الإرث بالطموح",
    "Aligned with Saudi Vision 2030 — investing in the infrastructure of a thriving nation": "متماشية مع رؤية السعودية 2030 - نستثمر في بنية تحتية مزدهرة للأمة",
    "Raising New Horizons": "نرفع آفاقًا جديدة",
    "Construction, real estate, and infrastructure projects shaping Saudi Arabia's built environment": "مشاريع البناء والعقارات والبنية التحتية التي تشكل البيئة العمرانية للمملكة العربية السعودية",
    "BUILDING THE FUTURE": "نبني مستقبل",
    "OF SAUDI ARABIA": "المملكة العربية السعودية",
    "A diversified family business group with over four decades of excellence across the GCC, leading in refrigeration, real estate, healthcare, and industrial solutions.": "مجموعة أعمال عائلية متنوعة مع أكثر من أربعة عقود من التميز في جميع أنحاء دول مجلس التعاون الخليجي، رائدة في مجال التبريد والعقارات والرعاية الصحية والحلول الصناعية.",
    "Subsidiaries": "شركات تابعة",
    "Years": "سنة",
    "Presence": "وجود",
    "Global Factories": "مصانع عالمية",
    "Explore Our Companies": "استكشف شركاتنا",
    "Get In Touch": "تواصل معنا",
    "Slide 1": "الشريحة 1",
    "Slide 2": "الشريحة 2",
    "Slide 3": "الشريحة 3",
    
    # Sectors Section
    "What We Do": "ماذا نفعل",
    "Our 8 Companies": "شركاتنا الثماني",
    "HVAC": "التكييف والتهوية",
    "Refrigeration": "التبريد",
    "Smart Parking": "مواقف السيارات الذكية",
    "Construction": "البناء والتشييد",
    "Real Estate": "العقارات",
    "BuildMix": "بيلد ميكس",
    "Hospitality": "الضيافة",
    "Recruitment": "التوظيف",
    
    # About Section
    "Who We Are": "من نحن",
    "Samara Group — A Diversified Holding Company": "مجموعة سمارة - شركة قابضة متنوعة",
    "Samara Group is a diversified holding company operating across multiple industries, delivering integrated solutions in engineering, manufacturing, construction, technology, and hospitality through its subsidiaries and international manufacturing partnerships.": "مجموعة سمارة هي شركة قابضة متنوعة تعمل عبر صناعات متعددة، وتقدم حلولاً متكاملة في الهندسة والتصنيع والبناء والتكنولوجيا والضيافة من خلال شركاتها التابعة وشراكات التصنيع الدولية.",
    "Headquartered in Al-Khobar, Saudi Arabia, we build international manufacturing partnerships spanning Egypt and China, serving clients across MENA and beyond.": "مقرنا الرئيسي في الخبر، المملكة العربية السعودية، نبني شراكات تصنيع دولية تمتد إلى مصر والصين، ونخدم العملاء في منطقة الشرق الأوسط وشمال أفريقيا وخارجها.",
    "Our Companies": "شركاتنا",
    "Learn More": "اعرف المزيد",
    
    # Founder Section
    "Our Founder": "مؤسسنا",
    "Abdulaziz Al-Samara": "عبدالعزيز السمارة",
    "Founder & Chairman": "المؤسس والرئيس التنفيذي",
    "For over 40 years, Abdulaziz Al-Samara has led Samara Group with a vision rooted in integrity, innovation, and long-term value creation.": "لأكثر من 40 عامًا، قاد عبدالعزيز السمارة مجموعة سمارة برؤية قائمة على النزاهة والابتكار وخلق القيمة طويلة الأمد.",
    "Starting with a small refrigeration workshop in Dammam, he grew the company into a multi-sector enterprise aligned with Saudi Arabia's economic transformation.": "بدءًا بورشة تبريد صغيرة في الدمام، طور الشركة لتصبح مؤسسة متعددة القطاعات متماشية مع التحول الاقتصادي للمملكة العربية السعودية.",
    "His commitment to quality, strategic partnerships, and national development continues to guide every decision at Samara Group.": "التزامه بالجودة والشراكات الاستراتيجية والتنمية الوطنية continua توجيه كل قرار في مجموعة سمارة.",
    "Read Full Bio": "اقرأ السيرة الكاملة",
    
    # Timeline Section
    "Our Journey": "رحلتنا",
    "Four Decades of Growth": "أربعة عقود من النمو",
    "Heritage": "الإرث",
    "Growth": "النمو",
    "Expansion": "التوسع",
    "Vision": "الرؤية",
    
    # Manufacturing Partners
    "Manufacturing Partners": "شركاء التصنيع",
    "Global Production Excellence": "التميز الإنتاجي العالمي",
    "We partner with world-class manufacturers to deliver high-quality products across HVAC, refrigeration, and building materials.": "نتعاون مع مصنعين عالميين لتقديم منتجات عالية الجودة في مجالات التكييف والتبريد ومواد البناء.",
    
    # Investments/Ecosystem
    "Strategic Investments": "الاستثمارات الاستراتيجية",
    "Building an Integrated Business Ecosystem": "بناء نظام بيئي أعمال متكامل",
    
    # Board of Directors
    "Board of Directors": "مجلس الإدارة",
    "Experienced Leadership": "قيادة ذات خبرة",
    
    # Labor Banner
    "Skilled Workforce": "قوى عاملة ماهرة",
    "Empowering Talent Across Borders": "تمكين المواهب عبر الحدود",
    
    # Featured Projects
    "Featured Projects": "المشاريع المميزة",
    "Delivering Excellence": "تقديم التميز",
    
    # Contact Section
    "Get In Touch": "تواصل معنا",
    "Contact Information": "معلومات الاتصال",
    "Send Message": "إرسال رسالة",
    "Your Name": "اسمك",
    "Your Email": "بريدك الإلكتروني",
    "Message": "الرسالة",
    "Submit": "إرسال",
    
    # Footer
    "All Rights Reserved": "جميع الحقوق محفوظة",
    "Privacy Policy": "سياسة الخصوصية",
    "Terms of Service": "شروط الخدمة",
    
    # Company specific names (keep as is or translate appropriately)
    "Samara H-VACR": "سمارة للتكييف والتبريد",
    "Samara Parking Solutions": "سمارة لحلول المواقف",
    "Saudi Builmix": "السعودية لبيلد ميكس",
    "Samara Real Estate": "سمارة للعقارات",
    "Saryryah Healthcare": "سريرية للرعاية الصحية",
    "Mahara Recruitment": "مهرة للتوظيف",
    "Salmiya Oasis": "سلمية الواحة",
}

# Additional context-specific translations
SECTOR_DESCRIPTIONS = {
    "HVAC": {
        "title": "سمارة للتكييف والتهوية والتبريد",
        "description": "حلول متقدمة لأنظمة التكييف والتهوية والتبريد للمباني السكنية والتجارية والصناعية"
    },
    "Refrigeration": {
        "title": "سمارة للتبريد",
        "description": "أنظمة تبريد صناعية وتجارية متطورة للمستودعات الباردة وسلاسل التوريد المبردة"
    },
    "Smart Parking": {
        "title": "سمارة لحلول المواقف",
        "description": "أنظمة مواقف سيارات ذكية ومتطورة تستخدم أحدث التقنيات لإدارة المواقف بكفاءة"
    },
    "Construction": {
        "title": "سمارة للبناء",
        "description": "مقاولات عامة وتنفيذ مشاريع البنية التحتية والمباني التجارية والسكنية"
    },
    "Real Estate": {
        "title": "سمارة للعقارات",
        "description": "تطوير وإدارة العقارات السكنية والتجارية والاستثمارية"
    },
    "BuildMix": {
        "title": "السعودية لبيلد ميكس",
        "description": "إنتاج مواد بناء مبتكرة وصديقة للبيئة باستخدام تقنيات متطورة"
    },
    "Hospitality": {
        "title": "سلمية الواحة",
        "description": "خدمات ضيافة فاخرة تشمل الفنادق والمنتجعات والمرافق الترفيهية"
    },
    "Recruitment": {
        "title": "مهرة للتوظيف",
        "description": "حلول توظيف متخصصة توفر الكفاءات والمواهب للشركات في مختلف القطاعات"
    }
}

def translate_text(text):
    """Translate English text to Arabic using the translation dictionary."""
    if not text or not text.strip():
        return text
    
    result = text
    # Sort by length (longest first) to avoid partial replacements
    for eng, arb in sorted(TRANSLATIONS.items(), key=lambda x: len(x[0]), reverse=True):
        # Use word boundary matching for better accuracy
        pattern = r'\b' + re.escape(eng) + r'\b'
        result = re.sub(pattern, arb, result)
    
    return result

def translate_html_file(filepath, output_filepath=None):
    """Translate an HTML file from English to Arabic."""
    if output_filepath is None:
        output_filepath = filepath
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Translate title
    title_match = re.search(r'<title>([^<]+)</title>', content)
    if title_match:
        old_title = title_match.group(1)
        new_title = translate_text(old_title)
        content = content.replace(f'<title>{old_title}</title>', f'<title>{new_title}</title>')
    
    # Translate meta description
    desc_match = re.search(r'<meta name="description" content="([^"]+)"', content)
    if desc_match:
        old_desc = desc_match.group(1)
        new_desc = translate_text(old_desc)
        content = content.replace(f'content="{old_desc}"', f'content="{new_desc}"')
    
    # Translate visible text content (between tags)
    # This is a simplified approach - we translate common patterns
    
    # Translate navigation links
    for eng, arb in TRANSLATIONS.items():
        # Match in anchor tags
        pattern = r'>([^<]*' + re.escape(eng) + r'[^<]*)<'
        matches = re.findall(pattern, content)
        for match in matches:
            if eng in match:
                translated = translate_text(match)
                content = content.replace(f'>{match}<', f'>{translated}<', 1)
        
        # Match in span tags with class
        pattern = r'(<span[^>]*>)\s*([^<]*' + re.escape(eng) + r'[^<]*)\s*(</span>)'
        matches = re.findall(pattern, content)
        for match in matches:
            full_match = ''.join(match)
            text_content = match[1]
            if eng in text_content:
                translated = translate_text(text_content)
                new_full = f'{match[0]}{translated}{match[2]}'
                content = content.replace(full_match, new_full, 1)
    
    # Translate placeholder attributes
    placeholder_pattern = r'placeholder="([^"]*)"'
    placeholders = re.findall(placeholder_pattern, content)
    for ph in placeholders:
        if any(word in ph for word in TRANSLATIONS.keys()):
            translated = translate_text(ph)
            content = content.replace(f'placeholder="{ph}"', f'placeholder="{translated}"')
    
    # Translate aria-label attributes
    aria_pattern = r'aria-label="([^"]*)"'
    aria_labels = re.findall(aria_pattern, content)
    for label in aria_labels:
        if any(word in label for word in TRANSLATIONS.keys()):
            translated = translate_text(label)
            content = content.replace(f'aria-label="{label}"', f'aria-label="{translated}"')
    
    # Translate alt attributes for images
    alt_pattern = r'alt="([^"]*)"'
    alt_texts = re.findall(alt_pattern, content)
    for alt in alt_texts:
        if any(word in alt for word in TRANSLATIONS.keys()):
            translated = translate_text(alt)
            content = content.replace(f'alt="{alt}"', f'alt="{translated}"')
    
    with open(output_filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  Translated: {filepath} -> {output_filepath}")

def main():
    workspace = '/workspace'
    en_dir = os.path.join(workspace, 'en')
    
    # Get all HTML files in the en directory
    html_files = []
    for filename in os.listdir(en_dir):
        if filename.endswith('.html'):
            html_files.append(os.path.join(en_dir, filename))
    
    print(f"Found {len(html_files)} English HTML files to translate")
    
    for filepath in html_files:
        filename = os.path.basename(filepath)
        output_path = os.path.join(workspace, filename)
        translate_html_file(filepath, output_path)
    
    print("\nTranslation complete!")

if __name__ == '__main__':
    main()
