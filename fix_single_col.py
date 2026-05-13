filepath = r'c:\Users\360\Dropbox\Claude Projects\Projects\rdd-hypnos\RDD.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

FLEX_ROW = 'style="display:flex; justify-content:space-around; text-align:center;"'

# ── 1. Visible templates — tcat header + sheet-center values (RDD, COMBAT, SKILLS) ──
OLD_TCAT = (
    '                <tr>\n'
    '                <td class="tcat">Attribut</td>\n'
    '                <td class="tcat">Difficulté</td>\n'
    '                </tr>\n'
    '                <tr>\n'
    '                <td class="sheet-center">{{attribut}}</td>\n'
    '                <td class="sheet-center">{{difficulte}}</td>\n'
    '                </tr>'
)
NEW_TCAT = (
    '                <tr>\n'
    f'                <td {FLEX_ROW}>'
    '<span class="tcat">Attribut</span><span class="tcat">Difficulté</span>'
    '</td>\n'
    '                </tr>\n'
    '                <tr>\n'
    f'                <td {FLEX_ROW}>'
    '<span class="sheet-center">{{attribut}}</span><span class="sheet-center">{{difficulte}}</span>'
    '</td>\n'
    '                </tr>'
)
n1 = content.count(OLD_TCAT)
content = content.replace(OLD_TCAT, NEW_TCAT)
print(f'tcat (RDD/COMBAT/SKILLS): {n1}')

# ── 2. STRESS — sheet-center for both header and values ──────────────────────
OLD_STRESS = (
    '                <tr>\n'
    '                <td class="sheet-center">Attribut</td>\n'
    '                <td class="sheet-center">Difficulté</td>\n'
    '                </tr>\n'
    '                <tr>\n'
    '                <td class="sheet-center">{{attribut}}</td>\n'
    '                <td class="sheet-center">{{difficulte}}</td>\n'
    '                </tr>'
)
NEW_STRESS = (
    '                <tr>\n'
    f'                <td {FLEX_ROW}>'
    '<span class="sheet-center">Attribut</span><span class="sheet-center">Difficulté</span>'
    '</td>\n'
    '                </tr>\n'
    '                <tr>\n'
    f'                <td {FLEX_ROW}>'
    '<span class="sheet-center">{{attribut}}</span><span class="sheet-center">{{difficulte}}</span>'
    '</td>\n'
    '                </tr>'
)
n2 = content.count(OLD_STRESS)
content = content.replace(OLD_STRESS, NEW_STRESS)
print(f'STRESS: {n2}')

# ── 3. NPC hidden Attribut/Difficulté rows ────────────────────────────────────
OLD_NPC = (
    '                <tr style="display:none">\n'
    '                <td class="npcroll" style="display:none">Attribut</td>\n'
    '                <td class="npcroll" style="display:none">Difficulté</td>\n'
    '                </tr>\n'
    '                <tr style="display:none">\n'
    '                <td class="sheet-center" class="npcroll" style="display:none">{{attribut}}</td>\n'
    '                <td class="sheet-center" class="npcroll" style="display:none">{{difficulte}}</td>\n'
    '                </tr>'
)
NEW_NPC = (
    '                <tr style="display:none">\n'
    '                <td style="display:none">Attribut / Difficulté</td>\n'
    '                </tr>\n'
    '                <tr style="display:none">\n'
    '                <td style="display:none">{{attribut}} / {{difficulte}}</td>\n'
    '                </tr>'
)
n3 = content.count(OLD_NPC)
content = content.replace(OLD_NPC, NEW_NPC)
print(f'NPC hidden Attribut/Difficulté: {n3}')

# ── 4. NPC hidden 3-cell targets row → single hidden cell ────────────────────
OLD_NPC_TGT = (
    '                <tr style="display:none">\n'
    '                <td style="text-align:center; color: #3FB315; font-size:10px;" style="display:none">{{reussite_par}}</td>\n'
    '                <td style="font-size:15px;text-align:center" style="display:none">{{cible}}</td>\n'
    '                <td class="echec" style="text-align:center; color: #B31515; font-size:10px;" style="display:none">{{echec_tot}}</td>\n'
    '                </tr>'
)
NEW_NPC_TGT = (
    '                <tr style="display:none">\n'
    '                <td style="display:none">{{reussite_par}} {{cible}} {{echec_tot}}</td>\n'
    '                </tr>'
)
n4 = content.count(OLD_NPC_TGT)
content = content.replace(OLD_NPC_TGT, NEW_NPC_TGT)
print(f'NPC hidden targets row: {n4}')

# ── 5. Remove all remaining COLSPAN="2" (table is now 1-column everywhere) ───
n5 = content.count(' COLSPAN="2"')
content = content.replace(' COLSPAN="2"', '')
print(f'COLSPAN="2" stripped: {n5}')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print('Done.')
