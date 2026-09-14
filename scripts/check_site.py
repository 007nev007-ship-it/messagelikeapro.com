"""Validate static sales routes, accessibility markup and local assets (stdlib only)."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, parse_qs
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(); self.tags=[]; self.feed(text)
    def handle_starttag(self, tag, attrs): self.tags.append((tag, dict(attrs)))
    def select(self, tag): return [a for t,a in self.tags if t == tag]

pages={p.name:Page(p.read_text()) for p in ROOT.glob('*.html')}
errors=[]
allowed={'on-track','at-work','off-script','in-conflict','under-pressure','professional-communication-system','complete-series'}
purchases=0
for name,page in sorted(pages.items()):
    def check(ok, msg):
        if not ok: errors.append(f'{name}: {msg}')
    check(len(page.select('h1'))==1, 'expected one page heading')
    check(page.select('html')[0].get('lang')=='en-GB','British English language tag')
    ids=[a['id'] for _,a in page.tags if 'id' in a]
    check(len(ids)==len(set(ids)),'duplicate IDs')
    check(any(a.get('id')=='main-content' for a in page.select('main')),'main landmark')
    check(len(page.select('summary'))==1,'native menu control')
    check(any(a.get('aria-label')=='Main navigation' for a in page.select('nav')),'navigation label')
    canonical=[a for a in page.select('link') if a.get('rel')=='canonical']
    expected='https://messagelikeapro.com/'+('' if name=='index.html' else name)
    check(len(canonical)==1 and canonical[0].get('href')==expected,'canonical URL')
    for prop in ('og:title','og:description','og:type','og:url','og:image'):
        check(sum(a.get('property')==prop for a in page.select('meta'))==1,f'{prop} metadata')
    for tag,a in page.tags:
        u=a.get('href', a.get('src','')); parsed=urlsplit(u)
        if not u: continue
        if not parsed.scheme and not parsed.netloc:
            target=parsed.path or name
            check((ROOT/target).is_file(), f'missing asset {u}')
            if parsed.fragment and target in pages:
                check(any(d.get('id')==parsed.fragment for _,d in pages[target].tags),f'missing anchor {u}')
        if parsed.hostname=='messagelikeapro.gumroad.com':
            purchases+=1
            check(parsed.path.split('/')[-1] in allowed,f'unknown product {u}')
            q=parse_qs(parsed.query)
            check(q.get('utm_source')==['messagelikeapro.com'] and bool(q.get('utm_content')),'missing attribution')
        if tag=='img':
            check('alt' in a and a.get('width') and a.get('height'),f'image accessibility/dimensions {u}')
            check((ROOT/parsed.path).stat().st_size>0,f'empty image {u}')
    text=(ROOT/name).read_text()
    check('type="checkbox"' not in text,'legacy menu remains')
    check('MLAP%20PDF%20Purchase%20Enquiry' not in text,'email book purchase route')
    check('Buy The App' not in text,'misleading app purchase label')

sitemap=ET.parse(ROOT/'sitemap.xml')
urls={n.text for n in sitemap.findall('.//{*}loc')}
assert len(urls)==len(pages),'Sitemap coverage mismatch'
assert 'Sitemap: https://messagelikeapro.com/sitemap.xml' in (ROOT/'robots.txt').read_text()
assert not errors,'\n'.join(errors)
print(f'PASS: {len(pages)} pages; {purchases} Gumroad links; local assets and anchors; metadata; native navigation; image attributes; sitemap.')
print('This is static validation, not a browser or completed-purchase test.')
