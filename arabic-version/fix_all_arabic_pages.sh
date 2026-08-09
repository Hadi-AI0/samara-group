#!/bin/bash

# List of Arabic pages in root that need fixing
files=(
  "/workspace/builmix.html"
  "/workspace/mahara-recruitment.html"
  "/workspace/salmiya-oasis.html"
  "/workspace/samara-H-VACR.html"
  "/workspace/samara-parking.html"
  "/workspace/samara-real-estate.html"
  "/workspace/saryryah-healthcare.html"
)

for file in "${files[@]}"; do
  if [ -f "$file" ]; then
    echo "Fixing $file..."
    
    # Get basename without extension for URL
    basename=$(basename "$file" .html)
    
    # Fix html tag to Arabic RTL
    sed -i 's/<html lang="en">/<html lang="ar" dir="rtl">/' "$file"
    
    # Fix canonical to point to Arabic version (no /en/)
    sed -i "s|<link rel=\"canonical\" href=\"https://samara.co.com/en/${basename}.html\" />|<link rel=\"canonical\" href=\"https://samara.co.com/${basename}\" />|" "$file"
    
    # Fix hreflang ar to point to root
    sed -i "s|hreflang=\"ar\" href=\"https://samara.co.com/en/${basename}.html\"|hreflang=\"ar\" href=\"https://samara.co.com/${basename}\"|" "$file"
    
    # Fix hreflang en to point to /en/
    sed -i "s|hreflang=\"en\" href=\"https://samara.co.com/${basename}\"|hreflang=\"en\" href=\"https://samara.co.com/en/${basename}.html\"|" "$file"
    
    # Fix x-default to point to Arabic (root)
    sed -i "s|hreflang=\"x-default\" href=\"https://samara.co.com/en/${basename}.html\"|hreflang=\"x-default\" href=\"https://samara.co.com/${basename}\"|" "$file"
    
    # Remove ltr.css link
    sed -i 's|<link rel="stylesheet" href="../css/ltr.css">||' "$file"
    
    echo "Fixed $file"
  fi
done

echo "Done!"
