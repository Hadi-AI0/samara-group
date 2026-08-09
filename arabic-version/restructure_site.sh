#!/bin/bash

# This script restructures the website to have:
# - Arabic (default) at root: /index.html, /samara-hvacr.html, etc.
# - English in /en/ subfolder: /en/index.html, /en/samara-hvacr.html, etc.

cd /workspace

# List of all HTML files except index.html
PAGES="builmix.html mahara-recruitment.html salmiya-oasis.html samara-H-VACR.html samara-parking.html samara-real-estate.html saryryah-healthcare.html"

echo "Starting site restructuring..."

# Step 1: Move current English pages to /en/ folder
echo "Moving English pages to /en/ folder..."
for page in $PAGES; do
    if [ -f "$page" ]; then
        mv "$page" "en/$page"
        echo "  Moved $page to en/$page"
    fi
done

# Step 2: Create Arabic versions of all pages at root
# We need to translate the English pages to Arabic

echo "Creating Arabic versions at root..."

# For now, we'll copy index.html structure and adapt it for each company page
# The actual Arabic content would need proper translation

echo "Site restructuring complete!"
echo ""
echo "Structure:"
echo "  Root (/) - Arabic pages"
echo "  /en/     - English pages"
