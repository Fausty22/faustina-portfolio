import fitz, os, shutil, re
from PIL import Image

root='/mnt/data/editcase'
source='/mnt/data/files/Okonkwo Fintech case study FINAL.pptx_20261006_222045_0000(2).pdf'
out_pdf=os.path.join(root,'case-studies','Okonkwo-FinTech-Customer-Success.pdf')
# modify first page: cover old label with matching navy and replace with CUSTOMER SUCCESS

doc=fitz.open(source)
p=doc[0]
# old label bounding box from text extraction, slightly padded
rect=fitz.Rect(78,235,545,272)
p.draw_rect(rect, color=None, fill=(34/255,46/255,112/255), overlay=True)
p.insert_text((86.4,257.5), 'C U S T O M E R  S U C C E S S', fontsize=16, fontname='helv', fontfile=None, color=(0.86,0.65,0.25), overlay=True)
doc.save(out_pdf)
doc.close()

# regenerate first slide image from modified PDF
mod=fitz.open(out_pdf)
pix=mod[0].get_pixmap(matrix=fitz.Matrix(1400/1440,1400/1440), alpha=False)
slide1=os.path.join(root,'case-slides','okonkwo','slide-01.jpg')
pix.save(slide1)
mod.close()

# Replace homepage preview images with real screenshots from the presentations.
shutil.copy(os.path.join(root,'case-slides','okonkwo','slide-11.jpg'), os.path.join(root,'images','work','customer-health-dashboard.jpg'))
shutil.copy(os.path.join(root,'case-slides','sunrise','slide-14.jpg'), os.path.join(root,'images','work','saas-customer-onboarding.jpg'))

# Update homepage alt text to describe actual previews.
idx=os.path.join(root,'index.html')
s=open(idx,encoding='utf-8').read()
s=s.replace('alt="Sunrise Digital MFB customer onboarding case study preview"','alt="Sunrise Digital MFB customer journey map case study preview"')
s=s.replace('alt="Okonkwo FinTech customer health case study preview"','alt="Okonkwo FinTech HubSpot customer health case study preview"')
open(idx,'w',encoding='utf-8').write(s)

# Replace purple slide viewer styling with original green/teal palette.
css=os.path.join(root,'css','slide-viewer.css')
open(css,'w',encoding='utf-8').write('''
.slide-viewer{background:#0b3d3a;border:1px solid #176f68;border-radius:18px;padding:16px;box-shadow:0 22px 55px rgba(0,0,0,.20)}
.slide-toolbar{display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap;margin-bottom:14px;color:#eaf7f5;font-size:13px}
.slide-toolbar .slide-actions{display:flex;gap:8px;flex-wrap:wrap}
.slide-toolbar button,.slide-toolbar a{border:1px solid #0f766e;background:#0f766e;color:#fff;padding:8px 13px;border-radius:999px;text-decoration:none;cursor:pointer;font:inherit}
.slide-toolbar button:hover,.slide-toolbar a:hover{background:#0b5c56;border-color:#0b5c56}
.slide-stage{position:relative;background:#082a27;border-radius:12px;overflow:hidden;min-height:280px;display:flex;align-items:center;justify-content:center}
.slide-stage img{display:block;width:100%;height:auto;max-height:78vh;object-fit:contain}
.slide-counter{font-weight:700;color:#9ee2dc}
.slide-thumbs{display:flex;gap:8px;overflow-x:auto;padding:12px 2px 2px;scrollbar-width:thin}
.slide-thumbs button{flex:0 0 90px;border:2px solid transparent;background:#0e504b;border-radius:8px;padding:0;overflow:hidden;cursor:pointer}
.slide-thumbs button.active{border-color:#0f766e}
.slide-thumbs img{display:block;width:100%;height:56px;object-fit:cover}
.slide-note{margin-top:10px;color:#c8e3df;font-size:12px;line-height:1.6}
@media(max-width:600px){.slide-viewer{padding:10px;border-radius:14px}.slide-stage img{max-height:none}.slide-thumbs button{flex-basis:74px}.slide-thumbs img{height:46px}}
''')
