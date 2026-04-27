filepath = r'c:\Users\360\Dropbox\Claude Projects\Projects\rdd-hypnos\RDD.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

start_m = '<div class="sheet-pc-tab-content sheet-pc-tab4"><!-- Onglet 4 -->'
end_m   = '</div> <!-- fin Onglet 4 -->'
start_idx = content.index(start_m)
end_idx   = content.index(end_m) + len(end_m)

before = content[:start_idx]
after  = content[end_idx:]

IMG_HDR    = 'https://cdn.jsdelivr.net/gh/icotom/rdd-hypnos@master/images/header_wide.png'
IMG_COMBAT = 'https://cdn.jsdelivr.net/gh/icotom/rdd-hypnos@master/images/bg_combat_header.jpg'

def bag(nom_attr, poids_attr, fieldset_name, contenu_attr, conpoids_attr):
    return (
        f'                <div class="sheet-bag-header">\n'
        f'                    <input type="text" name="attr_{nom_attr}" class="sheet-bag-name">\n'
        f'                    <input type="text" name="attr_{poids_attr}" class="sheet-bag-weight">\n'
        f'                </div>\n'
        f'                <fieldset class="repeating_{fieldset_name}">\n'
        f'                    <div class="sheet-bag-row">\n'
        f'                        <input type="text" name="attr_{contenu_attr}">\n'
        f'                        <input type="text" name="attr_{conpoids_attr}" class="sheet-bag-item-weight">\n'
        f'                    </div>\n'
        f'                </fieldset>\n'
    )

lines = []
lines.append('<div class="sheet-pc-tab-content sheet-pc-tab4"><!-- Onglet 4 -->\n')
lines.append(f'    <div style="background-image:url({IMG_HDR}); width:1193px; height:86px;margin-top:5px;"></div>\n')
lines.append(f'    <div style="background-image:url({IMG_COMBAT}); width:493px; height:88px;margin-top:5px;"></div>\n')
lines.append('    <div class="sheet-tab4-layout">\n')

# ── Left column: sacgauche 1-4 ───────────────────────────────────────────
lines.append('        <div class="sheet-tab4-col">\n')
for i in range(1, 5):
    lines.append(bag(
        f'nomsacgauche{i}',  f'sacgauchepoids{i}',
        f'contenusacgauche{i}',
        f'sacgauchecontenu{i}', f'sacgauchecontenupoids{i}'
    ))
lines.append('        </div>\n')

# ── Centre column: saccentre 1-4 ─────────────────────────────────────────
lines.append('        <div class="sheet-tab4-col">\n')
for i in range(1, 5):
    lines.append(bag(
        f'nomsaccentre{i}',  f'saccentre{i}',
        f'contenusaccentre{i}',
        f'saccentrecontenu{i}', f'saccentrepoids{i}'
    ))
lines.append('        </div>\n')

# ── Right column: sacdroite 1-4 ──────────────────────────────────────────
lines.append('        <div class="sheet-tab4-col">\n')
for i in range(1, 5):
    lines.append(bag(
        f'nomsacdroite{i}',  f'sacdroite{i}',
        f'contenusacdroite{i}',
        f'sacdroitecontenu{i}', f'sacdroitepoids{i}'
    ))
lines.append('        </div>\n')

lines.append('    </div><!-- fin sheet-tab4-layout -->\n')
lines.append('</div> <!-- fin Onglet 4 -->')

new_section = ''.join(lines)
result = before + new_section + after
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(result)

print('Done.')
