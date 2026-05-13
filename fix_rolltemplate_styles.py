import re

filepath = r'c:\Users\360\Dropbox\Claude Projects\Projects\rdd-hypnos\RDD.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

BASE = 'text-align:center; font-size:14px; text-transform:none;'

STYLES = {
    'sheet-reussite-part': f'{BASE} font-weight:bold; color:#00aa00;',
    'sheet-reussite-sig':  f'{BASE} font-weight:bold; color:#006400;',
    'sheet-reussite':      f'{BASE} color:#006400;',
    'sheet-echec':         f'{BASE} color:#8b0000;',
    'sheet-echec-part':    f'{BASE} font-weight:bold; color:#8b0000;',
    'sheet-echec-tot':     f'{BASE} font-weight:bold; color:#cc0000;',
}

# Replace class + any trailing junk up to > with class + fresh style
for cls, style in STYLES.items():
    content = re.sub(
        rf'class="{re.escape(cls)}"[^>]*>',
        rf'class="{cls}" style="{style}">',
        content
    )

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print('Done.')
