import re

filepath = r'c:\Users\360\Dropbox\Claude Projects\Projects\rdd-hypnos\RDD.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

start_m = '<div class="sheet-npc-tab-content sheet-npc-tab1"><!-- Onglet NPC -->'
end_m   = '</div><!-- fin Onglet NPC -->\n\n    </div>'
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
lines.append('<div class="sheet-npc-tab-content sheet-npc-tab1"><!-- Onglet NPC -->\n')
lines.append(f'    <div style="background-image:url({IMG_HDR}); width:1193px; height:86px;margin-top:5px;"></div>\n')

# ── Personal info ─────────────────────────────────────────────────────────────
lines.append('    <input type="text" name="attr_character_name" class="npcname" disabled />\n')
lines.append('    <div class="sheet-info-grid">\n')
lines.append('        <div class="sheet-info-row">\n')
lines.append('            <span class="sheet-info-label">Heure de Naissance</span>\n')
lines.append('            <input type="text" name="attr_birth" class="sheet-center">\n')
lines.append('        </div>\n')
lines.append('        <div class="sheet-info-row">\n')
lines.append('            <span class="sheet-info-label">Race</span>\n')
lines.append('            <input type="text" name="attr_race" style="width:80px;text-align:center">\n')
lines.append('            <span class="sheet-info-label">Sexe</span>\n')
lines.append('            <input type="text" name="attr_sexe" style="width:80px;text-align:center">\n')
lines.append('            <span class="sheet-info-label">Âge</span>\n')
lines.append('            <input type="number" name="attr_age" style="width:80px;text-align:center">\n')
lines.append('        </div>\n')
lines.append('        <div class="sheet-info-row">\n')
lines.append('            <span class="sheet-info-label">Taille</span>\n')
lines.append('            <input type="text" name="attr_taillerp" style="width:80px;text-align:center">\n')
lines.append('            <span class="sheet-info-label">Poids</span>\n')
lines.append('            <input type="text" name="attr_poids" style="width:80px;text-align:center">\n')
lines.append('        </div>\n')
lines.append('        <div class="sheet-info-row">\n')
lines.append('            <span class="sheet-info-label">Cheveux</span>\n')
lines.append('            <input type="text" name="attr_cheveux" style="width:80px;text-align:center">\n')
lines.append('            <span class="sheet-info-label">Yeux</span>\n')
lines.append('            <input type="text" name="attr_yeux" style="width:80px;text-align:center">\n')
lines.append('            <span class="sheet-info-label">Beauté</span>\n')
lines.append('            <input type="number" name="attr_beaute" class="sheet-center">\n')
lines.append('        </div>\n')
lines.append('    </div>\n')
lines.append('    <div style="margin-top:10px;">Signes Particuliers</div>\n')
lines.append('    <textarea style="width:450px;height:40px" name="attr_signes_part"></textarea>\n')

# ── Characteristics ───────────────────────────────────────────────────────────
lines.append('    <div style="margin-top:15px;">\n')
lines.append('    <div class="sheet-npc-char-grid">\n')
# Header row
lines.append('        <div class="sheet-center">Attribut</div><div style="padding-left:5px">Valeur</div>\n')
lines.append('        <div class="sheet-center">Attribut</div><div style="padding-left:5px">Valeur</div>\n')
# Row 1: TAILLE | VOLONTÉ(btn)
lines.append('        <div>TAILLE</div>\n')
lines.append('        <div><input type="number" name="attr_Taille" value="0" class="sheet-center"></div>\n')
lines.append(f'        <div>{btn("roll_Volonté", "VOLONTÉ")}</div>\n')
lines.append('        <div><input type="number" name="attr_volonte_value" value="0" class="sheet-center"></div>\n')
# Row 2: APPARENCE(btn) | INTELLECT(btn)
lines.append(f'        <div>{btn("roll_apparence", "APPARENCE")}</div>\n')
lines.append('        <div><input type="number" name="attr_apparence_value" value="0" class="sheet-center"></div>\n')
lines.append(f'        <div>{btn("roll_Intellect", "INTELLECT")}</div>\n')
lines.append('        <div><input type="number" name="attr_Intellect_value" value="0" class="sheet-center"></div>\n')
# Row 3: CONSTITUTION(btn) | EMPATHIE(btn)
lines.append(f'        <div>{btn("roll_constitution", "CONSTITUTION")}</div>\n')
lines.append('        <div><input type="number" name="attr_constitution_value" value="0" class="sheet-center"></div>\n')
lines.append(f'        <div>{btn("roll_empathie", "EMPATHIE")}</div>\n')
lines.append('        <div><input type="number" name="attr_empathie_value" value="0" class="sheet-center"></div>\n')
# Row 4: FORCE(btn) | RÊVE (no btn in char section)
lines.append(f'        <div>{btn("roll_Force", "FORCE")}</div>\n')
lines.append('        <div><input type="number" name="attr_force_value" value="0" class="sheet-center"></div>\n')
lines.append('        <div>RÊVE</div>\n')
lines.append('        <div><input type="number" name="attr_reve_value" value="0" class="sheet-center"></div>\n')
# Row 5: AGILITÉ(btn) | CHANCE
lines.append(f'        <div>{btn("roll_agilite", "AGILITÉ")}</div>\n')
lines.append('        <div><input type="number" name="attr_agilite_value" value="0" class="sheet-center"></div>\n')
lines.append('        <div>CHANCE</div>\n')
lines.append('        <div><input type="number" name="attr_chance_value" value="0" class="sheet-center"></div>\n')
# Row 6: DEXTERITÉ(btn) | Mêlée
lines.append(f'        <div>{btn("roll_dexterite", "DEXTERITÉ")}</div>\n')
lines.append('        <div><input type="number" name="attr_dexterite_value" value="0" class="sheet-center"></div>\n')
lines.append('        <div>Mêlée</div>\n')
lines.append('        <div><input type="number" name="attr_melee_value" value="0" class="sheet-center"></div>\n')
# Row 7: VUE | Tir
lines.append('        <div>VUE</div>\n')
lines.append('        <div><input type="number" name="attr_vue_value" value="0" class="sheet-center"></div>\n')
lines.append('        <div>Tir</div>\n')
lines.append('        <div><input type="number" name="attr_tir_value" value="0" class="sheet-center"></div>\n')
# Row 8: OUÏE | Lancer
lines.append('        <div>OUÏE</div>\n')
lines.append('        <div><input type="number" name="attr_ouie_value" value="0" class="sheet-center"></div>\n')
lines.append('        <div>Lancer</div>\n')
lines.append('        <div><input type="number" name="attr_lancer_value" value="0" class="sheet-center"></div>\n')
# Row 9: ODORAT-GOÛT | Dérobée
lines.append('        <div>ODORAT-GOÛT</div>\n')
lines.append('        <div><input type="number" name="attr_odoratgout_value" value="0" class="sheet-center"></div>\n')
lines.append('        <div>Dérobée</div>\n')
lines.append('        <div><input type="number" name="attr_derobee_value" value="0" class="sheet-center"></div>\n')
lines.append('    </div><!-- fin sheet-npc-char-grid -->\n')
lines.append('    </div><!-- fin caractéristiques -->\n')

# ── Vital Stats ───────────────────────────────────────────────────────────────
lines.append('    <div style="margin-top:15px;">\n')
lines.append('    <div class="sheet-vitals">\n')
lines.append('        <div class="sheet-vitals-row">\n')
lines.append('            <span class="sheet-center">Vie</span><input class="bulle" type="number" name="attr_vie">\n')
lines.append('            <span class="sheet-center">Endurance</span><input class="bulle" type="number" name="attr_endurance">\n')
lines.append('            <span class="sheet-center">Seuil de Constitution</span><input class="bulle" type="number" name="attr_const">\n')
lines.append('        </div>\n')
lines.append('        <div class="sheet-vitals-row">\n')
lines.append('            <span class="sheet-center">+Dom</span><input class="bulle" type="number" name="attr_dom">\n')
lines.append('            <span style="text-align:center;padding:0px 5px;">Malus Armure</span><input class="bulle" type="number" name="attr_malus_armure">\n')
lines.append('            <span style="text-align:center;padding:0px 5px;">Protection</span><input class="bulle" type="number" name="attr_prot">\n')
lines.append('        </div>\n')
lines.append('        <div class="sheet-vitals-row sheet-etat-general">\n')
lines.append('            <span>Etat Général</span>\n')
lines.append('            <input class="bulle" type="number" name="attr_etat_general1" value="@{etat_general}" disabled="disabled">\n')
lines.append('        </div>\n')
lines.append('        <div class="sheet-vitals-row">\n')
lines.append("            <span style=\"width:140px;\">Points d'Endurance</span>\n")
lines.append('            <span style="font-style:italic;">Actuel</span><input type="number" name="attr_PE_total" class="bulle">\n')
lines.append('            <span style="font-style:italic;">Max</span><input type="number" name="attr_PE_total_max" class="bulle">\n')
lines.append('        </div>\n')
lines.append('        <div class="sheet-vitals-row">\n')
lines.append('            <span style="width:140px;">Points de Vie</span>\n')
lines.append('            <span style="font-style:italic;">Actuel</span><input type="number" name="attr_PV_total" class="bulle" value="0">\n')
lines.append('            <span style="font-style:italic;">Max</span><input type="number" name="attr_PV_total_max" class="bulle" value="0">\n')
lines.append('        </div>\n')
lines.append('        <div class="sheet-vitals-row">\n')
lines.append('            <span style="width:140px;">Points de Rêve</span>\n')
lines.append('            <span style="font-style:italic;">Actuel</span><input type="number" name="attr_reve_total" class="bulle" value="0">\n')
lines.append('            <span style="font-style:italic;">Max</span><input type="number" name="attr_reve_total_max" class="bulle" value="0">\n')
# Rêve roll button (vitals version uses reve_total — last match in section wins)
lines.append(f'            {btn("roll_Rêve", "Rêve")}\n')
lines.append('        </div>\n')
lines.append('        <div class="sheet-vitals-row">\n')
lines.append('            <span style="width:140px;">Points de Chance</span>\n')
lines.append('            <span style="font-style:italic;">Actuel</span><input type="number" name="attr_chance_total" class="bulle" value="0">\n')
lines.append('            <span style="font-style:italic;">Max</span><input type="number" name="attr_chance_max_total" class="bulle" value="0">\n')
lines.append(f'            {btn("roll_Chance", "Chance")}\n')
lines.append('        </div>\n')
lines.append('    </div><!-- fin sheet-vitals -->\n')
lines.append('    </div><!-- fin vital stats -->\n')

# ── Armement ──────────────────────────────────────────────────────────────────
lines.append('    <div class="title-separate">Armement</div>\n')
lines.append('    <div class="sheet-npc-weapons-header">\n')
lines.append('        <span style="width:225px;">C. de Combat</span>\n')
lines.append('        <span style="width:50px;">Niv</span>\n')
lines.append('        <span style="width:55px;">Init</span>\n')
lines.append('        <span style="width:57px;">Dom</span>\n')
lines.append('        <span style="width:50px;">Exp</span>\n')
lines.append('    </div>\n')
lines.append('    <fieldset class="repeating_weapons">\n')
lines.append('        <div class="sheet-npc-weapons-row">\n')
lines.append('            <input type="text" name="attr_CombatCap" style="width:225px;">\n')
lines.append('            <input type="number" name="attr_CombatNiv" style="width:50px;">\n')
lines.append('            <input type="number" name="attr_CombatInit" style="width:55px;">\n')
lines.append('            <input type="number" name="attr_CombatDom" style="width:57px;">\n')
lines.append('            <input type="number" name="attr_CombatExp" style="width:50px;">\n')
lines.append(f'            {btn("roll_Distance", "Roll")}\n')
lines.append('        </div>\n')
lines.append('    </fieldset>\n')

# ── Compétences ───────────────────────────────────────────────────────────────
lines.append('    <div class="title-separate">Compétences</div>\n')
lines.append('    <div class="sheet-npc-skills-header">\n')
lines.append('        <span style="width:225px;">Compétences</span>\n')
lines.append('        <span style="width:50px;">Niv</span>\n')
lines.append('    </div>\n')
lines.append('    <fieldset class="repeating_skills">\n')
lines.append('        <div class="sheet-npc-skills-row">\n')
lines.append('            <input type="text" name="attr_SkillName" style="width:225px;">\n')
lines.append('            <input type="number" name="attr_SkillNiv" style="width:50px;">\n')
lines.append(f'            {btn("roll_Skill", "Roll")}\n')
lines.append('        </div>\n')
lines.append('    </fieldset>\n')

# ── Haut-Rêve ─────────────────────────────────────────────────────────────────
lines.append('    <div class="title-separate">Haut-Rêve</div>\n')
lines.append('    <div class="sheet-spell-header">\n')
lines.append('        <span style="width:120px;">Voie</span>\n')
lines.append('        <span style="width:350px;">Titre</span>\n')
lines.append('        <span style="width:150px;">T.M.R.</span>\n')
lines.append('        <span style="width:100px;">Difficulté</span>\n')
lines.append('        <span style="width:100px;">Coût en Rêve</span>\n')
lines.append('        <span style="width:350px;">Bonus de case</span>\n')
lines.append('    </div>\n')
lines.append('    <fieldset class="repeating_spell">\n')
lines.append('        <div class="sheet-spell-row">\n')
lines.append('            <select name="attr_spellvoie" style="width:120px;text-align:center;">\n')
lines.append('                <option value="Oniros">Oniros</option>\n')
lines.append('                <option value="Hypnos">Hypnos</option>\n')
lines.append('                <option value="Narcos">Narcos</option>\n')
lines.append('                <option value="Thanatos">Thanatos</option>\n')
lines.append('            </select>\n')
lines.append('            <input type="text" name="attr_spelltitre" style="width:350px;text-align:center;">\n')
lines.append('            <input type="text" name="attr_spellttmr" style="width:150px;text-align:center;">\n')
lines.append('            <input type="text" name="attr_spelltr1" style="width:100px;text-align:center;">\n')
lines.append('            <input type="text" name="attr_spelltr2" style="width:100px;text-align:center;">\n')
lines.append('            <input type="text" name="attr_spelltbonuscase" style="width:350px;text-align:center;">\n')
lines.append('        </div>\n')
lines.append('    </fieldset>\n')

lines.append('</div><!-- fin Onglet NPC -->')

new_section = ''.join(lines)
result = before + new_section + after
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(result)

print('Done. Buttons found:', list(buttons.keys()))
