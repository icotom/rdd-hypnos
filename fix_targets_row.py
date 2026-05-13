filepath = r'c:\Users\360\Dropbox\Claude Projects\Projects\rdd-hypnos\RDD.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# ── 1. Consolidate 3-cell targets row into single COLSPAN=4 cell ─────────────
# Appears in visible templates: RDD, COMBAT, SKILLS, STRESS
OLD_TARGETS = (
    '                <tr>\n'
    '                <td style="text-align:center; color: #3FB315; font-size:10px;">{{reussite_par}}</td>\n'
    '                <td COLSPAN="2" style="font-size:15px;text-align:center">{{cible}}</td>\n'
    '                <td class="echec" style="text-align:center; color: #B31515; font-size:10px;">{{echec_tot}}</td>\n'
    '                </tr>'
)

NEW_TARGETS = (
    '                <tr>\n'
    '                <td COLSPAN="4" style="text-align:center; padding:2px 0;">'
    '<span style="color:#3FB315; font-size:10px;">{{reussite_par}}</span>'
    '&nbsp;&nbsp;&nbsp;'
    '<span style="font-size:18px; font-weight:bold;">{{cible}}</span>'
    '&nbsp;&nbsp;&nbsp;'
    '<span style="color:#B31515; font-size:10px;">{{echec_tot}}</span>'
    '</td>\n'
    '                </tr>'
)

count = content.count(OLD_TARGETS)
print(f'Targets row: found {count} occurrences')
content = content.replace(OLD_TARGETS, NEW_TARGETS)

# ── 2. Add text-align:center to visible separator <td> (the one before targets)
# Pattern: <td align="center" valign="middle" COLSPAN="4"> with no inline style
OLD_SEP = '<td align="center" valign="middle" COLSPAN="4">\n'
NEW_SEP = '<td align="center" valign="middle" COLSPAN="4" style="text-align:center;">\n'

count2 = content.count(OLD_SEP)
print(f'Separator td: found {count2} occurrences')
content = content.replace(OLD_SEP, NEW_SEP)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print('Done.')
