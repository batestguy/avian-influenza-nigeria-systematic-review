import urllib.request, urllib.parse, json
def esearch(term, label):
    q = {'db': 'pubmed', 'term': term, 'retmode': 'json', 'retmax': 500}
    url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?' + urllib.parse.urlencode(q)
    d = json.load(urllib.request.urlopen(url))
    r = d['esearchresult']
    print(label, 'count=', r['count'], 'returned=', len(r['idlist']))
    return r['idlist'], r['count']
AIV = '(avian influenza[tiab] OR avian flu[tiab] OR bird flu[tiab] OR fowl plague[tiab] OR avian influenza virus[tiab] OR AIV[tiab] OR highly pathogenic avian influenza[tiab] OR HPAI[tiab] OR low pathogenic avian influenza[tiab] OR LPAI[tiab] OR H5N1[tiab] OR H5N2[tiab] OR H5N6[tiab] OR H5N8[tiab] OR H9N2[tiab] OR H7N9[tiab] OR H5Nx[tiab])'
NIG = '(Nigeria[Mesh] OR Nigeria[tiab] OR Nigerian[tiab])'
DAT = '("2006/01/01"[dp] : "2026/09/30"[dp])'
base = AIV + ' AND ' + NIG + ' AND ' + DAT
b, bc = esearch(base, 'BASEv3')
m, mc = esearch(base + ' AND (genome[tiab] OR molecular[tiab] OR phylogen*[tiab] OR clade[tiab] OR lineage[tiab] OR reassort*[tiab] OR mutation[tiab] OR evolution[tiab])', 'MOLv3')
open(r'D:\AvianInfluenzaSysRev\Workbench\35_PUBMED_v3_base.txt', 'w').write('\n'.join(b))
open(r'D:\AvianInfluenzaSysRev\Workbench\35_PUBMED_v3_mol.txt', 'w').write('\n'.join(m))
print('saved v3')
