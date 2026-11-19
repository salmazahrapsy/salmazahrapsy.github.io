rows=[("Not as described / unlike photo",27.8,14.0),("Fabric or material",23.2,6.4),("Delivery",22.8,31.5),("Colour",16.8,3.9),("Size or fit",13.5,5.2)]
W,L,top,rh=680,230,56,52; sc=(W-L-60)/35
o=[f'<svg class="chart" viewBox="0 0 {W} {top+rh*len(rows)+20}" role="img" aria-labelledby="ct cd" xmlns="http://www.w3.org/2000/svg"><title id="ct">Themes in negative reviews: clothing vs other categories</title><desc id="cd">'+"; ".join(f"{n}: clothing {a}%, other {b}%" for n,a,b in rows)+'.</desc>']
o.append(f'<rect x="{L}" y="14" width="12" height="12" class="c1"/><text x="{L+18}" y="25" class="lg">Clothing (4 categories)</text><rect x="{L+190}" y="14" width="12" height="12" class="c2"/><text x="{L+208}" y="25" class="lg">Other 25 categories</text>')
for i,(n,a,b) in enumerate(rows):
    y=top+i*rh
    o.append(f'<text x="{L-10}" y="{y+19}" text-anchor="end" class="lb">{n}</text>')
    o.append(f'<rect x="{L}" y="{y+4}" width="{a*sc:.1f}" height="16" class="c1"/><text x="{L+a*sc+6:.1f}" y="{y+17}" class="v">{a}%</text>')
    o.append(f'<rect x="{L}" y="{y+24}" width="{b*sc:.1f}" height="16" class="c2"/><text x="{L+b*sc+6:.1f}" y="{y+37}" class="v">{b}%</text>')
o.append(f'<line x1="{L}" x2="{L}" y1="{top}" y2="{top+rh*len(rows)}" class="ax"/></svg>')
open("chart.svg","w").write("".join(o))
