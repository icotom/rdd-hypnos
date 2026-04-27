import re

filepath = r'c:\Users\360\Dropbox\Claude Projects\Projects\rdd-hypnos\RDD.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

start_m = '<!-- partie basse - compétences -->'
end_m = '<!-- fin partie basse -->'
start_idx = content.index(start_m)
end_idx = content.index(end_m) + len(end_m)
before = content[:start_idx]
after = content[end_idx:]
section = content[start_idx:end_idx]

# ── Extract all button opening tags by roll name ──────────────────────────
BTN_RE = re.compile(r'<button(?:[^">]|"[^"]*")*>')
buttons = {}  # roll_name → full opening tag
for m in BTN_RE.finditer(section):
    tag = m.group(0)
    name_m = re.search(r'\bname="([^"]+)"', tag)
    if name_m:
        buttons[name_m.group(1)] = tag

def btn(roll_name, label):
    """Return full button with label as text content."""
    tag = buttons.get(roll_name, '')
    # inject/overwrite title with label
    if 'title=' in tag:
        tag = re.sub(r'\btitle="[^"]*"', f'title="{label}"', tag)
    else:
        tag = tag.replace('<button ', f'<button title="{label}" ', 1)
    return f'{tag}{label}</button>'

def skill_row(label, roll_name, attr_prefix, default_val):
    b = btn(roll_name, label)
    return (
        f'        <div class="sheet-skill-row">\n'
        f'            {b}\n'
        f'            <input type="number" name="attr_{attr_prefix}_value" value="{default_val}">\n'
        f'            <input type="number" name="attr_{attr_prefix}_xp">\n'
        f'        </div>\n'
    )

def custom_row(text_attr, roll_name, val_attr, default_val):
    b = buttons.get(roll_name, f'<button type="roll" class="sheet-roll-btn" name="{roll_name}" value="">')
    return (
        f'        <div class="sheet-skill-row">\n'
        f'            <input type="text" class="sheet-skill-custom" name="attr_{text_attr}">\n'
        f'            {b}</button>\n'
        f'            <input type="number" name="attr_{val_attr}_value" value="{default_val}">\n'
        f'            <input type="number" name="attr_{val_attr}_xp">\n'
        f'        </div>\n'
    )

def drac_row(label, roll_name, attr_prefix):
    b = btn(roll_name, label)
    return (
        f'        <div class="sheet-skill-row">\n'
        f'            {b}\n'
        f'            <input type="number" name="attr_{attr_prefix}_value" value="-11">\n'
        f'            <input type="number" name="attr_{attr_prefix}_voie">\n'
        f'            <input type="number" name="attr_{attr_prefix}_sort">\n'
        f'        </div>\n'
    )

def subheader(text):
    return f'        <div class="sheet-skills-subheader">{text}</div>\n'

# ── Build new section ─────────────────────────────────────────────────────
lines = []
lines.append('<!-- partie basse - compétences -->\n')
lines.append('        <div class="sheet-skills-col">\n')
lines.append('        <div class="title-separate">Compétences</div>\n')
lines.append('        <div class="sheet-skills-2col">\n')

# ── Column 1: Générales + Spécialisées ───────────────────────────────────
lines.append('        <div class="sheet-skills-left">\n')

lines.append(subheader('Générales (-4)'))
for label, roll, attr in [
    ('Bricolage',   'roll_Bricolage',  'brico'),
    ('Chant',       'roll_Chant',      'chant'),
    ('Course',      'roll_Course',     'cours'),
    ('Cuisine',     'roll_Cuisine',    'cuisi'),
    ('Danse',       'roll_Danse',      'danse'),
    ('Dessin',      'roll_Dessin',     'dessi'),
    ('Discrétion',  'roll_Discretion', 'discr'),
    ('Escalade',    'roll_Escalade',   'escal'),
    ('Saut',        'roll_Saut',       'saut'),
    ('Séduction',   'roll_Seduction',  'seduc'),
    ('Vigilance',   'roll_Vigilance',  'vigil'),
]:
    lines.append(skill_row(label, roll, attr, -4))

lines.append(subheader('Spécialisées (-11)'))
for label, roll, attr in [
    ('Acrobatie',    'roll_Acrobatie',     'acrob'),
    ('Chirurgie',    'roll_Chirurgie',     'chiru'),
    ('Jeu',          'roll_Jeu',           'jeu'),
    ('Jonglerie',    'roll_Jonglerie',     'jongl'),
    ('Maroquinerie', 'roll_Maroquinerie',  'maroq'),
    ('Métallurgie',  'roll_Metallurgie',   'metal'),
    ('Natation',     'roll_Natation',      'natat'),
    ('Navigation',   'roll_Navigation',    'navig'),
    ('Orfèvrerie',   'roll_Orfevrerie',    'orfev'),
    ('Serrurerie',   'roll_Serrurerie',    'serru'),
]:
    lines.append(skill_row(label, roll, attr, -11))

lines.append('        </div><!-- end sheet-skills-left -->\n')

# ── Column 2: Particulières + Connaissances ──────────────────────────────
lines.append('        <div class="sheet-skills-right">\n')

lines.append(subheader('Particulières (-8)'))
for label, roll, attr in [
    ('Charpenterie',   'roll_Charpenterie',  'charp'),
    ('Comédie',        'roll_Comedie',       'comed'),
    ('Commerce',       'roll_Commerce',      'comme'),
    ('Équitation',     'roll_Equitation',    'equit'),
    ('Maçonnerie',     'roll_Maconnerie',    'macon'),
    ('Musique',        'roll_Musique',       'musiq'),
    ('Pickpocket',     'roll_Pickpocket',    'pickp'),
    ('Srv en cité',    'roll_Srv_Cite',      'srvci'),
    ('Srv extérieur',  'roll_Srv_Exterieur', 'srvex'),
    ('Srv Désert',     'roll_Srv_Désert',    'srvde'),
    ('Srv Forêt',      'roll_Srv_Foret',     'srvfo'),
    ('Srv Glaces',     'roll_Srv_Glaces',    'srvgl'),
    ('Srv Marais',     'roll_Srv_Marais',    'srvmar'),
    ('Srv Montagne',   'roll_Srv_Montagne',  'srvmo'),
    ('Srv Sous-sol',   'roll_Srv_Sous_sol',  'srvso'),
    ('Travestissement','roll_travest',        'trave'),
]:
    lines.append(skill_row(label, roll, attr, -8))

lines.append(subheader('Connaissances (-11)'))
for label, roll, attr in [
    ('Alchimie',   'roll_Alchimie',   'alchi'),
    ('Astrologie', 'roll_Astrologie', 'astro'),
    ('Botanique',  'roll_Botanique',  'botan'),
    ('Écriture',   'roll_Ecriture',   'ecrit'),
    ('Légendes',   'roll_Legendes',   'legen'),
    ('Médecine',   'roll_Medecine',   'medec'),
    ('Zoologie',   'roll_Zoologie',   'zoolo'),
]:
    lines.append(skill_row(label, roll, attr, -11))

lines.append('        </div><!-- end sheet-skills-right -->\n')
lines.append('        </div><!-- end sheet-skills-2col -->\n')
lines.append('        <div class="sheet-skills-drac-spacer"></div>\n')

# Voies Draconic (-11)
lines.append(subheader('Voies Draconic (-11)'))
lines.append('        <div class="sheet-skill-row sheet-skill-header-drac">\n')
lines.append('            <span class="sheet-skill-drac-label"></span>\n')
lines.append('            <span class="sheet-skill-drac-col">Niveau</span>\n')
lines.append('            <span class="sheet-skill-drac-col">Voie</span>\n')
lines.append('            <span class="sheet-skill-drac-col">Sorts</span>\n')
lines.append('        </div>\n')
for label, roll, attr in [
    ('Oniros',   'roll_oniros',   'oniros'),
    ('Hypnos',   'roll_hypnos',   'hypnos'),
    ('Narcos',   'roll_narcos',   'narcos'),
    ('Thanatos', 'roll_thanatos', 'thanatos'),
]:
    lines.append(drac_row(label, roll, attr))

lines.append('        </div><!-- fin sheet-skills-col -->\n')
lines.append('<!-- fin partie basse -->')

new_section = ''.join(lines)

result = before + new_section + after
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(result)

print('Done. Buttons found:', list(buttons.keys())[:5], '...')
print('Total buttons extracted:', len(buttons))
