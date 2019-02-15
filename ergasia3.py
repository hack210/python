f=open("C:\Users\evogi\OneDrive\Desktop\ergasia3 patsOK\kodikaspy.txt","r")
L=[]
newline=[]
for line in f:
    arsx=1
    for k in line:#gia kathe gramma tou line
        L.append(k)
        if k=="#":#vriski plithos ton #
            arsx=arsx+1
        x=""
        for j in range (len(line)):
            x=x+line[j]
        if '"' in x:#arxi telos diplon eisagogikon
            arxds=x.find('"')
            trxds=x.find('"', arxds+1)
        elif "'" in x:#arxi telos monon eisagogikon
            arxms=x.find("'")
            txms=x.find("'", arxms+1)
    if "#" not in line:#ean den exei # stin grammi to vazi stin nea grammi
        newline.append(line)
    for l in range(1,arsx):
        hessx=x.find("#")#vriski tin thesi tou sxoleiou
        if l>=1 and arsx>2 :#ean exei pano apo 1 sxoleio
            thesix=x.find("#",hessx+1)#thesi teleutaiou sxoleiou
            if thesix==0:
                None
            if '"' in line:#ean exei " h grammi
                if thesix<arxds or thesix>trxds:#elenxei an den einai to # mesa se ""
                    prmetseir=[]
                    for i in range(len(x)):
                        if i <=thesix :
                            prmetseir.append(x[i])
                    prmetseir.pop(thesix)
                    y=""
                    for ji in range(len(prmetseir)):
                        y=y+prmetseir[ji]
                    if y in newline:
                        None
                    else:
                        newline.append(y)
                else:
                    newline.append(line)
            elif "'" in line:#ean exei' h grammi
                if thesix<arxms or thesix>txms :#elenxei an den einai to # mesa se ''
                    prmetseir=[]
                    for ja in range(len(x)):
                        if ja <=thesix :
                            prmetseir.append(x[ja])
                    prmetseir.pop(thesix)
                    y=""
                    for jl in range(len(prmetseir)):
                        y=y+prmetseir[jl]
                    if y in newline:
                        None
                    else:
                        newline.append(y)
                else:
                    newline.append(line)
        else:#ean exei 1 sxoleio
            if hessx==0:
                None
            if '"' in line:#ean exei " h grammi
                if hessx<arxds or hessx>trxds:#elenxei an den einai to # mesa se ""
                    prmetseir=[]
                    for jb in range(len(x)):
                        if jb <=hessx :
                            prmetseir.append(x[jb])
                    prmetseir.pop(hessx)
                    y=""
                    for jp in range(len(prmetseir)):
                        y=y+prmetseir[jp]
                    if y in newline:
                        None
                    else:
                        newline.append(y)
                else:
                    newline.append(line)
            elif "'" in line:#ean exei' h grammi
                if hessx<arxms or hessx>txms :#elenxei an den einai to # mesa se ''
                    prmetseir=[]
                    for jc in range(len(x)):
                        if jc <=hessx :
                            prmetseir.append(x[jc])
                    prmetseir.pop(hessx)
                    y=""
                    for jz in range(len(prmetseir)):
                        y=y+prmetseir[jz]
                    if y in newline:
                        None
                    else:
                        newline.append(y)
                else:
                    newline.append(line)
            elif hessx!=0 and '"' or "'" not in line :
                prmetseir=[]
                for jf in range(len(x)):
                    if jf <=hessx :
                        prmetseir.append(x[jf])
                prmetseir.pop(hessx)
                y=""
                for jh in range(len(prmetseir)):
                    y=y+prmetseir[jh]
                if y in newline:
                    None
                else:
                    newline.append(y)
for abc in newline:
    print abc
            
        
