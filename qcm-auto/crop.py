import sys,json
from PIL import Image,ImageFilter,ImageStat
# spec: list of {src,box:[x0,y0,x1,y1] (100dpi coords),masks:[[x0,y0,x1,y1],...],out}
S=2
for sp in json.load(open(sys.argv[1])):
    im=Image.open(sp["src"]).convert("L")
    for m in sp.get("masks",[]):
        b=[int(v*S) for v in m]
        pad=6;ring=im.crop((b[0]-pad,b[1]-pad,b[2]+pad,b[3]+pad))
        blur=ring.filter(ImageFilter.GaussianBlur(14))
        fill=Image.new("L",(b[2]-b[0],b[3]-b[1]),int(ImageStat.Stat(ring).median[0]))
        # soft fill: blurred surroundings
        im.paste(blur.crop((pad,pad,pad+b[2]-b[0],pad+b[3]-b[1])).filter(ImageFilter.GaussianBlur(4)),(b[0],b[1]))
    x0,y0,x1,y1=[int(v*S) for v in sp["box"]]
    out=im.crop((x0,y0,x1,y1))
    out.save(sp["out"],"JPEG",quality=85);print(sp["out"],out.size)
