#!/usr/bin/env python3
"""
Script to add language switcher functionality to all HTML pages
and fix the misspellings:
- salmiya = سالمية (not واحة السلمية)
- builmix = بيلميكس (not بيلد ميكس)
"""

import os
import re

# Define the workspace directory
WORKSPACE = "/workspace"

# Files to process
arabic_files = [
    "index.html",
    "builmix.html",
    "mahara-recruitment.html",
    "salmiya-oasis.html",
    "samara-H-VACR.html",
    "samara-parking.html",
    "samara-real-estate.html",
    "saryryah-healthcare.html"
]

english_files = [
    "en/index.html",
    "en/builmix.html",
    "en/mahara-recruitment.html",
    "en/salmiya-oasis.html",
    "en/samara-H-VACR.html",
    "en/samara-parking.html",
    "en/samara-real-estate.html",
    "en/saryryah-healthcare.html"
]

# Language switcher button HTML for Arabic pages (switches to English)
ARABIC_LANG_SWITCHER = '''
      <!-- Language Switcher -->
      <button class="lang-switcher" id="lang-switcher" aria-label="Switch to English" onclick="switchLanguage('en')">
        <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/><path d="M2 12h20"/></svg>
        <span>EN</span>
      </button>
'''

# Language switcher button HTML for English pages (switches to Arabic)
ENGLISH_LANG_SWITCHER = '''
      <!-- Language Switcher -->
      <button class="lang-switcher" id="lang-switcher" aria-label="Switch to Arabic" onclick="switchLanguage('ar')">
        <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/><path d="M2 12h20"/></svg>
        <span>عربي</span>
      </button>
'''

def add_lang_switcher_to_nav(content, is_arabic):
    """Add language switcher button to navigation"""
    # Find the mobile-menu-btn and add lang switcher before it
    nav_container_pattern = r'(<button class="nav-toggle" id="mobile-menu-btn")'
    
    if is_arabic:
        replacement = ARABIC_LANG_SWITCHER + r'\1'
    else:
        replacement = ENGLISH_LANG_SWITCHER + r'\1'
    
    content = re.sub(nav_container_pattern, replacement, content)
    return content

def fix_misspellings(content):
    """Fix the specified misspellings"""
    # Fix salmiya: واحة السلمية -> واحة سالمية
    content = content.replace("واحة السلمية", "واحة سالمية")
    content = content.replace("واحة سالمية", "واحة سالمية")  # Ensure consistency
    
    # Fix builmix: بيلد ميكس -> بيلميكس
    content = content.replace("بيلد ميكس", "بيلميكس")
    
    return content

def add_language_script(content, is_arabic):
    """Add JavaScript for language switching before closing body tag"""
    
    lang_script = '''
  <script>
    // Language switching functionality
    function switchLanguage(lang) {
      const currentPath = window.location.pathname;
      const currentHost = window.location.host;
      const protocol = window.location.protocol;
      
      // Get the filename from the path
      let fileName = currentPath.split('/').pop() || 'index.html';
      
      // Handle root path
      if (currentPath === '/' || currentPath === '') {
        fileName = 'index.html';
      }
      
      if (lang === 'en') {
        // Switching to English
        if (currentPath.includes('/en/')) {
          // Already in English folder, stay on same page
          return;
        }
        
        // Remove any leading slash for proper path construction
        let cleanFileName = fileName.startsWith('/') ? fileName.substring(1) : fileName;
        
        // Navigate to English version
        window.location.href = protocol + '//' + currentHost + '/en/' + cleanFileName;
      } else {
        // Switching to Arabic
        if (!currentPath.includes('/en/')) {
          // Already in Arabic (root), stay on same page
          return;
        }
        
        // Remove /en/ prefix to get Arabic version
        let arabicFileName = fileName;
        if (currentPath.includes('/en/')) {
          // Extract just the filename without /en/
          const parts = currentPath.split('/');
          arabicFileName = parts[parts.length - 1] || 'index.html';
        }
        
        // Navigate to Arabic version (root)
        window.location.href = protocol + '//' + currentHost + '/' + arabicFileName;
      }
    }
    
    // Auto-redirect based on user's language preference when entering root
    document.addEventListener('DOMContentLoaded', function() {
      const currentPath = window.location.pathname;
      const storedLang = localStorage.getItem('preferredLanguage');
      
      // Only auto-redirect on root index page if no language is stored
      if ((currentPath === '/' || currentPath === '' || currentPath === '/index.html') && !storedLang) {
        const userLang = navigator.language || navigator.userLanguage;
        if (userLang && userLang.startsWith('ar')) {
          // User prefers Arabic, stay on root
          localStorage.setItem('preferredLanguage', 'ar');
        } else if (userLang && userLang.startsWith('en')) {
          // User prefers English, redirect to /en/
          localStorage.setItem('preferredLanguage', 'en');
          window.location.href = '/en/';
        }
      }
      
      // Store current language preference
      if (currentPath.includes('/en/')) {
        localStorage.setItem('preferredLanguage', 'en');
      } else {
        localStorage.setItem('preferredLanguage', 'ar');
      }
    });
  </script>
'''
    
    # Add script before closing body tag
    content = content.replace('</body>', lang_script + '\n</body>')
    return content

def add_css_styles(content):
    """Add CSS styles for language switcher"""
    css_styles = '''
  <style>
    .lang-switcher {
      display: flex;
      align-items: center;
      gap: 6px;
      padding: 8px 12px;
      background: transparent;
      border: 1px solid rgba(255, 255, 255, 0.3);
      border-radius: 6px;
      color: inherit;
      cursor: pointer;
      transition: all 0.3s ease;
      font-size: 13px;
      font-weight: 500;
    }
    
    .lang-switcher:hover {
      background: rgba(255, 255, 255, 0.1);
      border-color: rgba(255, 255, 255, 0.5);
    }
    
    .navbar.scrolled .lang-switcher {
      border-color: rgba(29, 79, 145, 0.3);
    }
    
    .navbar.scrolled .lang-switcher:hover {
      background: rgba(29, 79, 145, 0.1);
      border-color: rgba(29, 79, 145, 0.5);
    }
    
    @media (max-width: 768px) {
      .lang-switcher {
        margin: 10px 20px;
      }
    }
  </style>
'''
    
    # Add styles before closing head tag
    content = content.replace('</head>', css_styles + '\n</head>')
    return content

def process_file(filepath, is_arabic):
    """Process a single HTML file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Add CSS styles
        content = add_css_styles(content)
        
        # Add language switcher to navigation
        content = add_lang_switcher_to_nav(content, is_arabic)
        
        # Add language switching script
        content = add_language_script(content, is_arabic)
        
        # Fix misspellings (only for Arabic files)
        if is_arabic:
            content = fix_misspellings(content)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Processed: {filepath}")
        return True
    except Exception as e:
        print(f"✗ Error processing {filepath}: {e}")
        return False

def main():
    print("Adding language switcher and fixing misspellings...\n")
    
    success_count = 0
    total_count = 0
    
    # Process Arabic files
    print("Processing Arabic files...")
    for file in arabic_files:
        filepath = os.path.join(WORKSPACE, file)
        if os.path.exists(filepath):
            total_count += 1
            if process_file(filepath, is_arabic=True):
                success_count += 1
        else:
            print(f"⚠ File not found: {filepath}")
    
    # Process English files
    print("\nProcessing English files...")
    for file in english_files:
        filepath = os.path.join(WORKSPACE, file)
        if os.path.exists(filepath):
            total_count += 1
            if process_file(filepath, is_arabic=False):
                success_count += 1
        else:
            print(f"⚠ File not found: {filepath}")
    
    print(f"\n{'='*50}")
    print(f"Completed: {success_count}/{total_count} files processed successfully")

if __name__ == "__main__":
    main()
