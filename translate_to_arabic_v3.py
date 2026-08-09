#!/usr/bin/env python3
"""
Translate English content to Arabic for all HTML pages (v3 - comprehensive).
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
    "His commitment to quality, strategic partnerships, and national development continues to guide every decision at Samara Group.": "التزامه بالجودة والشراكات الاستراتيجية والتنمية الوطنية يواصل توجيه كل قرار في مجموعة سمارة.",
    "Read Full Bio": "اقرأ السيرة الكاملة",
    "Since founding Samara Group in 1984, our vision has remained steadfast: to build a legacy rooted in integrity, quality, and service. Over four decades, we have grown from a single refrigeration company into a diversified conglomerate. As Saudi Arabia strides toward Vision 2030, we stand ready to shape the future through infrastructure, healthcare, and innovation.": "منذ تأسيس مجموعة سمارة عام 1984، ظلت رؤيتنا راسخة: بناء إرث قائم على النزاهة والجودة والخدمة. على مدى أربعة عقود، نما我们从 شركة تبريد واحدة إلى مجمع متنوع. ومع تقدم المملكة العربية السعودية نحو رؤية 2030، نحن مستعدون لتشكيل المستقبل من خلال البنية التحتية والرعاية الصحية والابتكار.",
    "Chairman, Samara Group": "الرئيس التنفيذي، مجموعة سمارة",
    
    # Timeline Section
    "Our Journey": "رحلتنا",
    "Four Decades of Growth": "أربعة عقود من النمو",
    "Heritage": "الإرث",
    "Growth": "النمو",
    "Expansion": "التوسع",
    "Vision": "الرؤية",
    "Milestones of Growth Since 1984": "محطات النمو منذ 1984",
    "Key moments that shaped our legacy": "لحظات رئيسية شكلت إرثنا",
    
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
    
    # Additional phrases
    "Proudly Aligned with Saudi Vision 2030": "نفخر بالانضمام إلى رؤية السعودية 2030",
    "Leading provider of heating, ventilation, air conditioning, and refrigeration solutions delivering innovative climate control systems for residential, commercial, and industrial applications across the Kingdom.": "مزود رائد لحلول التدفئة والتهوية والتكييف والتبريد نقدم أنظمة تحكم مناخي مبتكرة للتطبيقات السكنية والتجارية والصناعية في جميع أنحاء المملكة.",
    "Saudi Arabia skyline": "أفق المملكة العربية السعودية",
    "Construction site": "موقع البناء",
    "Saudi Arabia vision": "رؤية السعودية",
    "Founder portrait": "صورة المؤسس",
}

def translate_html_file(filepath, output_filepath=None):
    """Translate an HTML file from English to Arabic."""
    if output_filepath is None:
        output_filepath = filepath
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Sort translations by length (longest first) to avoid partial replacements
    sorted_translations = sorted(TRANSLATIONS.items(), key=lambda x: len(x[0]), reverse=True)
    
    # Replace text between tags
    def replace_text(match):
        text = match.group(1)
        for eng, arb in sorted_translations:
            if eng in text:
                text = text.replace(eng, arb)
        return '>' + text + '<'
    
    content = re.sub(r'>([^<]+)<', replace_text, content)
    
    # Replace placeholder attributes
    def replace_placeholder(match):
        text = match.group(1)
        for eng, arb in sorted_translations:
            if eng in text:
                text = text.replace(eng, arb)
        return f'placeholder="{text}"'
    content = re.sub(r'placeholder="([^"]*)"', replace_placeholder, content)
    
    # Replace aria-label attributes
    def replace_aria(match):
        text = match.group(1)
        for eng, arb in sorted_translations:
            if eng in text:
                text = text.replace(eng, arb)
        return f'aria-label="{text}"'
    content = re.sub(r'aria-label="([^"]*)"', replace_aria, content)
    
    # Replace alt attributes
    def replace_alt(match):
        text = match.group(1)
        for eng, arb in sorted_translations:
            if eng in text:
                text = text.replace(eng, arb)
        return f'alt="{text}"'
    content = re.sub(r'alt="([^"]*)"', replace_alt, content)
    
    # Replace title
    def replace_title(match):
        text = match.group(1)
        for eng, arb in sorted_translations:
            if eng in text:
                text = text.replace(eng, arb)
        return f'<title>{text}</title>'
    content = re.sub(r'<title>([^<]+)</title>', replace_title, content)
    
    # Replace meta description
    def replace_desc(match):
        full_match = match.group(0)
        text = match.group(1)
        for eng, arb in sorted_translations:
            if eng in text:
                text = text.replace(eng, arb)
        return f'<meta name="description" content="{text}"'
    content = re.sub(r'<meta name="description" content="([^"]+)"', replace_desc, content)
    
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
