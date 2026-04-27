filepath = r'c:\Users\360\Dropbox\Claude Projects\Projects\rdd-hypnos\RDD.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

start_m = '<div class="sheet-pc-tab-content sheet-pc-tab3"><!-- Onglet 3 -->'
end_m = '</div> <!-- fin onglet 3-->'
start_idx = content.index(start_m)
end_idx = content.index(end_m) + len(end_m)

before = content[:start_idx]
after = content[end_idx:]

def row(label, attr):
    return f'                <div class="sheet-arche-row"><span>{label}</span><input type="number" name="attr_{attr}" class="sheet-center" value="0"></div>\n'

def section(title):
    return f'                <div class="sheet-arche-section">{title}</div>\n'

IMG_HDR  = 'https://cdn.jsdelivr.net/gh/icotom/rdd-hypnos@master/images/header_wide.png'
IMG_COL  = 'https://cdn.jsdelivr.net/gh/icotom/rdd-hypnos@master/images/bg_pc_column_right.jpg'

lines = []
lines.append('<div class="sheet-pc-tab-content sheet-pc-tab3"><!-- Onglet 3 -->\n')
lines.append(f'        <div style="background-image:url({IMG_HDR}); width:1193px; height:86px;margin-top:5px;"></div>\n')
lines.append('        <div class="sheet-tab3-2col">\n')

# ── Col 1: Générales + Spécialisées ──────────────────────────────────────
lines.append('            <div class="sheet-tab3-col">\n')
lines.append(section('Générales (-4)'))
for label, attr in [
    ('Bricolage',  'brico_arche'), ('Chant',      'chant_arche'),
    ('Course',     'cours_arche'), ('Cuisine',    'cuisi_arche'),
    ('Danse',      'danse_arche'), ('Dessin',     'dessi_arche'),
    ('Discrétion', 'discr_arche'), ('Escalade',   'escal_arche'),
    ('Saut',       'saut_arche'),  ('Séduction',  'seduc_arche'),
    ('Vigilance',  'vigil_arche'),
]:
    lines.append(row(label, attr))

lines.append(section('Spécialisées (-11)'))
for label, attr in [
    ('Acrobatie',    'acrob_arche'), ('Chirurgie',   'chiru_arche'),
    ('Jeu',          'jeu_arche'),   ('Jonglerie',   'jongl_arche'),
    ('Maroquinerie', 'maroq_arche'), ('Métallurgie', 'metal_arche'),
    ('Natation',     'natat_arche'), ('Navigation',  'navig_arche'),
    ('Orfèvrerie',   'orfev_arche'), ('Serrurerie',  'serru_arche'),
]:
    lines.append(row(label, attr))

lines.append(section('Compétences de Mêlée (-6)'))
for label, attr in [
    ("Armes d'Hast", 'hast_arche'),   ('Bouclier',    'boucl_arche'),
    ('Corps à Corps', 'corps_arche'),  ('Dague',       'dague_arche'),
    ('Épée 1 main',  'epee1m_arche'), ('Épée 2 mains','epee2m_arche'),
    ('Esquive',      'esqui_arche'),   ('Fléau',       'fleau_arche'),
    ('Hache 1 main', 'hache1m_arche'),('Hache 2 mains','hache2m_arche'),
    ('Lance',        'lance_arche'),   ('Masse 1 main','masse1m_arche'),
    ('Masse 2 mains','masse2m_arche'),
]:
    lines.append(row(label, attr))
lines.append('            </div><!-- fin col 1 -->\n')

# ── Col 2: Particulières + Connaissances + Draconic ──────────────────────
lines.append('            <div class="sheet-tab3-col">\n')
lines.append(section('Particulières (-8)'))
for label, attr in [
    ('Charpenterie',   'charp_arche'), ('Comédie',       'comed_arche'),
    ('Commerce',       'comme_arche'), ('Équitation',    'equit_arche'),
    ('Maçonnerie',     'macon_arche'), ('Musique',       'musiq_arche'),
    ('Pickpocket',     'pickp_arche'), ('Survie Cité',   'srvci_arche'),
    ('Survie Extérieur','srvex_arche'),('Survie Désert', 'srvde_arche'),
    ('Survie Forêt',   'srvfo_arche'), ('Survie Glaces', 'srvgl_arche'),
    ('Survie Marais',  'srvma_arche'), ('Survie Montagne','srvmo_arche'),
    ('Survie Sous-sol','srvso_arche'), ('Travestissement','trave_arche'),
]:
    lines.append(row(label, attr))

lines.append(section('Connaissances (-11)'))
for label, attr in [
    ('Alchimie',  'alchi_arche'), ('Astrologie', 'astro_arche'),
    ('Botanique', 'botan_arche'), ('Écriture',   'ecrit_arche'),
    ('Légendes',  'legend_arche'),('Médecine',   'mede_arche'),
    ('Zoologie',  'zoolo_arche'),
]:
    lines.append(row(label, attr))

lines.append(section('Tir &amp; Lancer (-8)'))
for label, attr in [
    ('Arbalète', 'tirlancer_arche'), ('Arc',     'arc_arche'),
    ('Dague',    'dague_lancer_arche'),('Fouet',  'fouet_arche'),
    ('Fronde',   'frond_arche'),      ('Hache',   'hache_arche'),
    ('Javelot',  'javel_arche'),
]:
    lines.append(row(label, attr))

lines.append(section('Draconic (-11)'))
for label, attr in [
    ('Oniros',   'oniros_arche'),  ('Hypnos',   'hypnos_arche'),
    ('Narcos',   'narcos_arche'),  ('Thanatos', 'thanatos_arche'),
]:
    lines.append(row(label, attr))
lines.append('            </div><!-- fin col 2 -->\n')

lines.append(f'            <div style="background-image:url({IMG_COL}); width:450px; height:1251px;"></div><!-- col décorative -->\n')
lines.append('        </div><!-- fin sheet-tab3-2col -->\n')
lines.append('    </div> <!-- fin onglet 3-->')

new_section = ''.join(lines)
result = before + new_section + after
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(result)

print('Done.')
