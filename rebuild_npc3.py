import re

filepath = r'c:\Users\360\Dropbox\Claude Projects\Projects\rdd-hypnos\RDD.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

start_m = '<div class="sheet-npc-tab-content sheet-npc-tab3"><!-- Onglet Animal/Creature -->'
end_m   = '</div><!-- fin Onglet Animal/Creature -->\n\n    </div>'
start_idx = content.index(start_m)
end_idx   = content.index(end_m) + len(end_m)

before  = content[:start_idx]
after   = content[end_idx:]
section = content[start_idx:end_idx]

# ── Extract button opening tags by roll name ──────────────────────────────────
BTN_RE = re.compile(r'<button(?:[^">]|"[^"]*")*>')
buttons = {}
for m in BTN_RE.finditer(section):
    tag = m.group(0)
    name_m = re.search(r'\bname="([^"]+)"', tag)
    if name_m:
        buttons[name_m.group(1)] = tag

def btn(roll_name, label):
    tag = buttons.get(roll_name, f'<button type="roll" class="sheet-roll-btn" name="{roll_name}" value="">')
    return f'{tag}{label}</button>'

IMG_HDR = 'https://cdn.jsdelivr.net/gh/icotom/rdd-hypnos@master/images/header_wide.png'

lines = []
lines.append('<div class="sheet-npc-tab-content sheet-npc-tab3"><!-- Onglet Animal/Creature -->\n')
lines.append(f'    <div style="background-image:url({IMG_HDR}); width:1193px; height:86px;margin-top:5px;"></div>\n')

# ── Personal info ─────────────────────────────────────────────────────────────
lines.append('    <input type="text" name="attr_character_name" class="npcname" disabled />\n')
lines.append('    <div style="margin-top:10px;">Description</div>\n')
lines.append('    <textarea style="width:450px;height:40px" name="attr_signes_part"></textarea>\n')

# ── Characteristics ───────────────────────────────────────────────────────────
lines.append('    <div style="margin-top:15px;">\n')
lines.append('    <div class="sheet-npc-char-grid">\n')
# Header
lines.append('        <div class="sheet-center">Attribut</div><div style="padding-left:5px">Valeur</div>\n')
lines.append('        <div class="sheet-center">Attribut</div><div style="padding-left:5px">Valeur</div>\n')
# Row 1: TAILLE | CONSTITUTION(btn)
lines.append('        <div>TAILLE</div>\n')
lines.append('        <div><input type="number" name="attr_Taille" value="0" class="sheet-center"></div>\n')
lines.append(f'        <div>{btn("roll_constitution", "CONSTITUTION")}</div>\n')
lines.append('        <div><input type="number" name="attr_constitution_value" value="0" class="sheet-center"></div>\n')
# Row 2: FORCE(btn) | PERCEPTION(btn)
lines.append(f'        <div>{btn("roll_force", "FORCE")}</div>\n')
lines.append('        <div><input type="number" name="attr_force_value" value="0" class="sheet-center"></div>\n')
lines.append(f'        <div>{btn("roll_perception", "PERCEPTION")}</div>\n')
lines.append('        <div><input type="number" name="attr_perception_value" value="0" class="sheet-center"></div>\n')
# Row 3: VOLONTE(btn) | RÊVE(btn)
lines.append(f'        <div>{btn("roll_Volonté", "VOLONTÉ")}</div>\n')
lines.append('        <div><input type="number" name="attr_volonte_value" value="0" class="sheet-center"></div>\n')
lines.append(f'        <div>{btn("roll_Rêve", "RÊVE")}</div>\n')
lines.append('        <div><input type="number" name="attr_reve_value" value="0" class="sheet-center"></div>\n')
lines.append('    </div><!-- fin sheet-npc-char-grid -->\n')
lines.append('    </div><!-- fin caractéristiques -->\n')

# ── Stats ─────────────────────────────────────────────────────────────────────
lines.append('    <div style="margin-top:15px;">\n')
lines.append('    <div class="sheet-vitals">\n')
lines.append('        <div class="sheet-vitals-row">\n')
lines.append('            <span class="sheet-center">+Dom</span><input class="bulle" type="number" name="attr_dom">\n')
lines.append('            <span class="sheet-center">Protection</span><input class="bulle" type="number" name="attr_prot">\n')
lines.append('        </div>\n')
lines.append('        <div class="sheet-vitals-row">\n')
lines.append('            <span style="width:140px;">Points de Vie</span>\n')
lines.append('            <span style="font-style:italic;">Actuel</span><input type="number" name="attr_PV_total" class="bulle">\n')
lines.append('            <span style="font-style:italic;">Max</span><input type="number" name="attr_PV_total_max" class="bulle">\n')
lines.append('        </div>\n')
lines.append('        <div class="sheet-vitals-row">\n')
lines.append("            <span style=\"width:140px;\">Points d'Endurance</span>\n")
lines.append('            <span style="font-style:italic;">Actuel</span><input type="number" name="attr_PE_total" class="bulle">\n')
lines.append('            <span style="font-style:italic;">Max</span><input type="number" name="attr_PE_total_max" class="bulle">\n')
lines.append('        </div>\n')
lines.append('    </div><!-- fin sheet-vitals -->\n')
lines.append('    </div><!-- fin stats -->\n')

# ── Combat et Possession ──────────────────────────────────────────────────────
lines.append('    <div class="title-separate">Combat et Possession</div>\n')
lines.append('    <div class="sheet-npc-weapons-header">\n')
lines.append('        <span style="width:225px;">Compétences de Combat</span>\n')
lines.append('        <span style="width:50px;">Attr.</span>\n')
lines.append('        <span style="width:50px;">Niv</span>\n')
lines.append('        <span style="width:55px;">Init</span>\n')
lines.append('        <span style="width:57px;">Dom</span>\n')
lines.append('    </div>\n')
lines.append('    <fieldset class="repeating_weapons">\n')
lines.append('        <div class="sheet-npc-weapons-row">\n')
lines.append('            <input type="text" name="attr_CombatCap" style="width:225px;">\n')
lines.append('            <input type="number" name="attr_CombatAttr" style="width:50px;">\n')
lines.append('            <input type="number" name="attr_CombatNiv" style="width:50px;">\n')
lines.append('            <input type="number" name="attr_CombatInit" style="width:55px;">\n')
lines.append('            <input type="number" name="attr_CombatDom" style="width:57px;">\n')
lines.append(f'            {btn("roll_Combat", "Roll")}\n')
lines.append('        </div>\n')
lines.append('    </fieldset>\n')

lines.append('</div><!-- fin Onglet Animal/Creature -->')

new_section = ''.join(lines)
result = before + new_section + after
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(result)

print('Done. Buttons found:', list(buttons.keys()))
