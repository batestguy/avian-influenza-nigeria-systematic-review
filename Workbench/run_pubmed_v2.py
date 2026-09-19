import urllib.request, urllib.parse, json
def esearch(term, label):
    q = {'db': 'pubmed', 'term': term, 'retmode': 'json', 'retmax': 500}
    url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?' + urllib.parse.urlencode(q)
    d = json.load(urllib.request.urlopen(url))
    r = d['esearchresult']
    print(label, 'count=', r['count'], 'returned=', len(r['idlist']))
    print('  translation:', r.get('querytranslation', '')[:250])
    return r['idlist'], r['count']
AIV = '(avian influenza[tiab] OR avian influenza virus[tiab] OR AIV[tiab] OR highly pathogenic avian influenza[tiab] OR HPAI[tiab] OR low pathogenic avian influenza[tiab] OR LPAI[tiab] OR H5N1[tiab] OR H5N2[tiab] OR H5N6[tiab] OR H5N8[tiab] OR H9N2[tiab] OR H7N9[tiab])'
NIG = '(Nigeria[Mesh] OR Nigeria[tiab] OR Nigerian[tiab])'
DAT = '("2006/01/01"[dp] : "2026/09/30"[dp])'
MOL = '(genome[tiab] OR molecular[tiab] OR phylogen*[tiab] OR clade[tiab] OR lineage[tiab] OR sublineage[tiab] OR reassort*[tiab] OR mutation[tiab] OR evolution[tiab] OR genetic diversity[tiab])'
EPI = '(outbreak[tiab] OR surveillance[tiab] OR prevalence[tiab] OR distribution[tiab] OR spatial[tiab] OR geographic[tiab] OR temporal[tiab] OR emergence[tiab] OR spread[tiab] OR introduction[tiab])'
WILD = '(wild bird*[tiab] OR waterfowl[tiab] OR migratory[tiab] OR wetland[tiab] OR wildlife[tiab])'
base = AIV + ' AND ' + NIG + ' AND ' + DAT
b, bc = esearch(base, 'BASEv2')
m, mc = esearch(base + ' AND ' + MOL, 'MOL facet')
e, ec = esearch(base + ' AND ' + EPI, 'EPI facet')
w, wc = esearch(base + ' AND ' + WILD, 'WILD facet')
open(r'D:\AvianInfluenzaSysRev\Workbench\34_PUBMED_v2_base.txt', 'w').write('\n'.join(b))
open(r'D:\AvianInfluenzaSysRev\Workbench\34_PUBMED_v2_mol.txt', 'w').write('\n'.join(m))
open(r'D:\AvianInfluenzaSysRev\Workbench\34_PUBMED_v2_epi.txt', 'w').write('\n'.join(e))
open(r'D:\AvianInfluenzaSysRev\Workbench\34_PUBMED_v2_wild.txt', 'w').write('\n'.join(w))
print('saved v2 lists')
