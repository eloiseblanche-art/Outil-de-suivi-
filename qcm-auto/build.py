"""Compact text -> qcm document JSON.
Header lines: cours=, matiere=, ordre=, titre=
'# Section' starts a section; '? sujet' starts a question (optional '@assetid' at end for photo);
'+ texte | commentaire' true item, '- texte | commentaire' false item."""
import json,sys,re,random
src,out=sys.argv[1],sys.argv[2]
doc={"sections":[],"questions":[]};cur=None;nq=np=0
for raw in open(src,encoding="utf-8"):
    l=raw.rstrip("\n").strip()
    if not l or l.startswith("//"):continue
    m=re.match(r"^(cours|matiere|ordre|titre)=(.*)$",l)
    if m:doc[m[1]]=int(m[2]) if m[1]=="ordre" else m[2];continue
    if l.startswith("# "):doc["sections"].append(l[2:].strip());continue
    if l.startswith("? "):
        q=l[2:].strip();img=None
        mm=re.search(r"\s@([0-9a-f]{32})$",q)
        if mm:img=mm[1];q=q[:mm.start()].strip()
        if img:np+=1;cur={"id":"p%02d"%np,"q":q,"s":len(doc["sections"])-1,"it":[],"img":img}
        else:nq+=1;cur={"id":"q%02d"%nq,"q":q,"s":len(doc["sections"])-1,"it":[]}
        doc["questions"].append(cur);continue
    if l[0] in "+-":
        t,_,c=l[1:].partition("|");cur["it"].append({"t":t.strip(),"v":l[0]=="+","c":c.strip()});continue
    raise SystemExit("ligne inconnue: "+l)
for q in doc["questions"]:
    v=sum(i["v"] for i in q["it"])
    assert len(q["it"])==5,(q["id"],len(q["it"]))
    assert 1<=v<=4,(q["id"],v)
    for i in q["it"]:
        if not i["v"]:assert i["c"],(q["id"],"fausse sans commentaire",i["t"])
    assert q["s"]>=0
# order of true/false items is randomised (a bank is never re-shuffled once saved)
for q in doc["questions"]:random.shuffle(q["it"])
json.dump(doc,open(out,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
from collections import Counter
print(out,len(doc["questions"]),"questions",Counter(sum(i["v"] for i in q["it"]) for q in doc["questions"]))
