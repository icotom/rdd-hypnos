filepath = r'c:\Users\360\Dropbox\Claude Projects\Projects\rdd-hypnos\RDD.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

IMG_HDR = 'https://cdn.jsdelivr.net/gh/icotom/rdd-hypnos@master/images/header_wide.png'

# ── 1. Insert Tab 6 radio after Tab 5 radio ─────────────────────────────────
TAB5_RADIO = '<input type="radio" name="attr_tab" class="sheet-pc-tab sheet-pc-tab5" value="5" title="Sorts" />'
TAB6_RADIO = '<input type="radio" name="attr_tab" class="sheet-pc-tab sheet-pc-tab6" value="6" title="Vrai Rêve" />'

content = content.replace(
    TAB5_RADIO,
    TAB5_RADIO + '\n    ' + TAB6_RADIO,
    1
)

# ── 2. Build Tab 6 content block ─────────────────────────────────────────────
TAB6 = (
    '\n    <div class="sheet-pc-tab-content sheet-pc-tab6"><!-- Onglet 6 -->\n'
    f'        <div style="background-image:url({IMG_HDR}); width:1193px; height:86px;margin-top:5px;"></div>\n'

    # Rules summary
    '        <div class="title-separate">Règles du Vrai Rêvant</div>\n'
    '        <div style="margin:10px 0; max-width:800px;">\n'
    '            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>\n'
    '            <ul>\n'
    '                <li>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</li>\n'
    '                <li>Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</li>\n'
    '                <li>Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.</li>\n'
    '                <li>Duis aute irure dolor in reprehenderit in voluptate velit esse cillum.</li>\n'
    '            </ul>\n'
    '        </div>\n'

    # Compétences de Vocation
    '        <div class="title-separate">Compétences de Vocation</div>\n'
    '        <div style="margin:10px 0; display:flex; flex-direction:column; gap:6px;">\n'
    '            <input type="text" name="attr_vocation1" style="width:500px;">\n'
    '            <input type="text" name="attr_vocation2" style="width:500px;">\n'
    '            <input type="text" name="attr_vocation3" style="width:500px;">\n'
    '            <input type="text" name="attr_vocation4" style="width:500px;">\n'
    '        </div>\n'

    # Têtes de Dragon
    '        <div class="title-separate">Têtes de Dragon</div>\n'
    '        <div class="sheet-vr-entry-header">\n'
    '            <span style="width:220px;">Nom</span>\n'
    '            <span>Description</span>\n'
    '        </div>\n'
    '        <fieldset class="repeating_tetesdragon">\n'
    '            <div class="sheet-vr-entry-row">\n'
    '                <input type="text" name="attr_tdnom" style="width:220px;">\n'
    '                <textarea name="attr_tddesc" style="width:600px; height:55px;"></textarea>\n'
    '            </div>\n'
    '        </fieldset>\n'

    # Talents Oniriques
    '        <div class="title-separate">Talents Oniriques</div>\n'
    '        <div class="sheet-vr-entry-header">\n'
    '            <span style="width:220px;">Nom</span>\n'
    '            <span>Description</span>\n'
    '        </div>\n'
    '        <fieldset class="repeating_talentsoniriques">\n'
    '            <div class="sheet-vr-entry-row">\n'
    '                <input type="text" name="attr_tonom" style="width:220px;">\n'
    '                <textarea name="attr_todesc" style="width:600px; height:55px;"></textarea>\n'
    '            </div>\n'
    '        </fieldset>\n'

    '    </div> <!-- fin Onglet 6 -->\n'
)

# Insert after Tab 5 closing div
TAB5_END = '    </div> <!-- fin Onglet 5 -->'
content = content.replace(TAB5_END, TAB5_END + TAB6, 1)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print('Done.')
