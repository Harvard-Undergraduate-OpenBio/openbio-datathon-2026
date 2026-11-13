import zipfile, numpy as np, pandas as pd, time
Z='raw/figshare/sc_PE_allcells_with_metadata_29-May-2023.txt.zip'
meta=pd.read_csv('raw/figshare/cell_metadata.csv',dtype=str)
key=meta.donorID+'|'+meta.celltype
codes,uniq=pd.factorize(key)
G=len(uniq)
f=zipfile.ZipFile(Z).open('sc_PE_allcells_with_metadata_29-May-2023.txt')
for _ in range(23): f.readline()
genes=[];out=[];nonint=0;neg=0;t=time.time()
for i,line in enumerate(f):
    g,rest=line.split(b'\t',1)
    v=np.fromstring(rest,sep='\t')
    assert v.size==len(meta),(g,v.size)
    if (v%1!=0).any(): nonint+=1
    if (v<0).any(): neg+=1
    out.append(np.bincount(codes,weights=v,minlength=G).astype(np.int64))
    genes.append(g.decode())
    if i%2000==0: print(i,g,round(time.time()-t),flush=True)
M=pd.DataFrame(np.vstack(out),index=genes,columns=uniq)
M.index.name='gene'
M.to_pickle('build/sc_pseudobulk_fine.pkl')
print('done',M.shape,'nonint',nonint,'neg',neg,'dupgenes',M.index.duplicated().sum(),flush=True)
