import base64,re,sys,os
S=os.path.dirname(os.path.abspath(__file__))
def uri(path,mime):
    return f"data:{mime};base64,"+base64.b64encode(open(path,'rb').read()).decode()
m={}
for w in (400,600,700):
    m[f'font{w}']=uri(f'{S}/font/package/files/open-sans-latin-{w}-normal.woff2','font/woff2')
for f in os.listdir(f'{S}/assets'):
    n,e=os.path.splitext(f)
    m[n]=uri(f'{S}/assets/{f}','image/png' if e=='.png' else 'image/jpeg')
t=open(f'{S}/vorlage.html',encoding='utf-8').read()
miss=set(re.findall(r'\{\{(\w+)\}\}',t))-set(m)
assert not miss,miss

# Silbentrennung fuer Blocksatz: weiche Trennstriche (&shy;) in Absaetzen der Blocksatz-Seiten,
# damit die Trennung in jedem Browser funktioniert (benoetigt: pip install pyphen)
BLOCKSATZ=('vorstellung','beratung','technologien','detail-1','detail-2','detail-3')
try:
    import pyphen
    _dic=pyphen.Pyphen(lang='de_DE',left=3,right=3)
    def _hy(text):
        return re.sub(r'[A-Za-zÄÖÜäöüß]{9,}',lambda w:_dic.inserted(w.group(0),hyphen='\u00ad'),text)
    def _para(mp):
        return re.sub(r'>([^<]+)<',lambda x:'>'+_hy(x.group(1))+'<',mp.group(0))
    for sid in BLOCKSATZ:
        a=t.index(f'id="{sid}"'); b=t.index('</section>',a)
        t=t[:a]+re.sub(r'<p[ >].*?</p>',_para,t[a:b],flags=re.S)+t[b:]
except ImportError:
    print('Hinweis: pyphen fehlt, Blocksatz ohne weiche Trennstriche')
t=re.sub(r'\{\{(\w+)\}\}',lambda x:m[x.group(1)],t)
out=sys.argv[1]
open(out,'w',encoding='utf-8').write(t)
print(out,round(os.path.getsize(out)/1e6,2),'MB')
