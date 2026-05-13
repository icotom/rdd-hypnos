filepath = r'c:\Users\360\Dropbox\Claude Projects\Projects\rdd-hypnos\RDD.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# ── Outcome classes — most specific first to avoid partial matches ────────────

# Echec Total
content = content.replace('class="sheet-failure sheet-caps">Echec Total!!!', 'class="sheet-echec-tot">Echec Total!!!')
content = content.replace('class="sheet-failure">Echec Total!!!',            'class="sheet-echec-tot">Echec Total!!!')

# Echec Particulier
content = content.replace('class="sheet-failure sheet-caps">Echec Particulier !', 'class="sheet-echec-part">Echec Particulier !')
content = content.replace('class="sheet-failure">Echec Particulier !',            'class="sheet-echec-part">Echec Particulier !')

# Plain Echec
content = content.replace('class="sheet-failure sheet-caps">Echec</td>', 'class="sheet-echec">Echec</td>')
content = content.replace('class="sheet-failure">Echec</td>',            'class="sheet-echec">Echec</td>')

# Réussite Particulière
content = content.replace('class="sheet-success sheet-caps">Réussite Particulière !', 'class="sheet-reussite-part">Réussite Particulière !')
content = content.replace('class="sheet-success">Réussite Particulière !',            'class="sheet-reussite-part">Réussite Particulière !')

# Réussite Significative
content = content.replace('class="sheet-success sheet-caps">Réussite Significative !', 'class="sheet-reussite-sig">Réussite Significative !')
content = content.replace('class="sheet-success">Réussite Significative !',            'class="sheet-reussite-sig">Réussite Significative !')

# Plain Réussite
content = content.replace('class="sheet-success sheet-caps">Réussite</td>', 'class="sheet-reussite">Réussite</td>')
content = content.replace('class="sheet-success">Réussite</td>',            'class="sheet-reussite">Réussite</td>')

# ── Center targets row flanking cells ────────────────────────────────────────
# Visible templates (RDD, COMBAT, SKILLS, STRESS)
content = content.replace(
    'style="text-align:right; height:12px; width:15px; color: #3FB315; font-size:10px;"',
    'style="text-align:center; color: #3FB315; font-size:10px;"'
)
content = content.replace(
    'style="text-align:left;height:12px;    width:15px;    color: #B31515;    font-size:10px;margin-left:-20px"',
    'style="text-align:center; color: #B31515; font-size:10px;"'
)

# NPC hidden templates (NPC-Skill, Entite, Animal) — same styles + display:none
content = content.replace(
    'style="text-align:right; height:12px; width:15px; color: #3FB315; font-size:10px;" style="display:none"',
    'style="text-align:center; color: #3FB315; font-size:10px;" style="display:none"'
)
content = content.replace(
    'style="text-align:left;height:12px;    width:15px;    color: #B31515;    font-size:10px;margin-left:-20px" style="display:none"',
    'style="text-align:center; color: #B31515; font-size:10px;" style="display:none"'
)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print('Done.')
