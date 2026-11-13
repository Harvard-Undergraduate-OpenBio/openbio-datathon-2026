import gzip, glob, re, os, numpy as np, pandas as pd
RAW='raw'; OUT='track-01/data'
# ---------- metadata from series matrix ----------
lines=[l.rstrip('\n').split('\t') for l in gzip.open(f'{RAW}/geo/GSE203507_series_matrix.txt.gz','rt') if l.startswith('!Sample_')]
acc=[x.strip('"') for x in next(l for l in lines if l[0]=='!Sample_geo_accession')[1:]]
title=[x.strip('"') for x in next(l for l in lines if l[0]=='!Sample_title')[1:]]
ch={}
for l in lines:
    if l[0]=='!Sample_characteristics_ch1':
        vals=[x.strip('"') for x in l[1:]]
        k=vals[0].split(': ',1)[0]
        ch[k]=[v.split(': ',1)[1] if ': ' in v else v for v in vals]
m=pd.DataFrame(ch); m.insert(0,'geo_accession',acc); m.insert(1,'title',title)
m['donor_id']=[t.split(', ')[1] for t in title]
m['tissue_code']=['VT' if 'villous' in x else 'DB' for x in m['tissue']]
m['sample_id']=m.donor_id+'_'+m.tissue_code
def na(x): return None if x in ('N/A','','NA') else x
def ga(x):
    x=na(x)
    if x is None: return (None,None,None)
    w,_,d=x.partition('.'); d=int(d) if d else 0
    return (int(w),d,round(int(w)+d/7,3))
meta=pd.DataFrame({'sample_id':m.sample_id,'geo_accession':m.geo_accession,'donor_id':m.donor_id,'tissue':m.tissue_code})
meta['group']=m['clinical group']
meta['pe_status']=meta.group.map(lambda g:'PE' if g.startswith('EOPE') else 'no_PE')
meta['pe_onset']=meta.group.map(lambda g:'early_onset' if g.startswith('EOPE') else 'not_applicable')
meta['fgr_status']=meta.group.map(lambda g:'FGR' if 'FGR' in g else 'no_FGR')
meta['control_type']=meta.group.map({'iPTB':'preterm_birth','TB':'term_birth'}).fillna('not_control')
g=m['gestational age_at_delivery_(weeks.days)'].map(ga)
meta['ga_delivery_source']=m['gestational age_at_delivery_(weeks.days)'].map(na)
meta['ga_delivery_completed_weeks']=[x[0] for x in g]
meta['ga_delivery_extra_days']=[x[1] for x in g]
meta['ga_delivery_weeks']=[x[2] for x in g]
meta['preterm_delivery']=[None if x[2] is None else ('yes' if x[2]<37 else 'no') for x in g]
meta['maternal_age_years']=m['age of_mother_(years)'].map(na)
bw=m['birthweight interval_(grams)'].map(na)
meta['birthweight_interval_g']=bw
meta['birthweight_lower_g']=bw.map(lambda x:None if pd.isna(x) else int(x.split('-')[0]))
meta['birthweight_upper_g']=bw.map(lambda x:None if pd.isna(x) else int(x.split('-')[1]))
meta['fetal_sex']=m['assigned neonatal_sex'].str.lower()
meta['sbp_max_mmhg']=m['highest antepartum_systolic_blood_pressure_(mm_hg)'].map(na)
meta['dbp_max_mmhg']=m['highest antepartum_diastolic_blood_pressure_(mm_hg)'].map(na)
# race/ethnicity kept organizer-side until clinical reviewer sign-off
m[['sample_id','maternal ethnicity','maternal race']].to_csv('build/organizer_only_race_ethnicity.csv',index=False)
for c in ['ga_delivery_completed_weeks','ga_delivery_extra_days','maternal_age_years','birthweight_lower_g','birthweight_upper_g','sbp_max_mmhg','dbp_max_mmhg']:
    meta[c]=pd.to_numeric(meta[c]).astype('Int64')
# ---------- audit flags (flag, never correct) ----------
def flags(r):
    f=[]
    if pd.notna(r.ga_delivery_weeks) and not (20<=r.ga_delivery_weeks<=42): f.append('ga_out_of_range')
    if pd.notna(r.ga_delivery_extra_days) and r.ga_delivery_extra_days>6: f.append('ga_days_component_gt6')
    if r.control_type=='preterm_birth' and pd.notna(r.ga_delivery_weeks) and r.ga_delivery_weeks>=37: f.append('preterm_group_ga_term')
    if r.control_type=='term_birth' and pd.notna(r.ga_delivery_weeks) and r.ga_delivery_weeks<37: f.append('term_group_ga_preterm')
    if r.pe_status=='PE' and pd.notna(r.ga_delivery_weeks) and r.ga_delivery_weeks>=34: f.append('early_onset_pe_delivered_ge34w')
    s,d=r.sbp_max_mmhg,r.dbp_max_mmhg
    if pd.notna(s) and not (70<=s<=250): f.append('sbp_out_of_range')
    if pd.notna(d) and not (30<=d<=150): f.append('dbp_out_of_range')
    if pd.notna(s) and pd.notna(d) and d>=s: f.append('dbp_ge_sbp')
    if r.pe_status=='PE' and pd.notna(s) and pd.notna(d) and s<140 and d<90: f.append('pe_without_bp_ge_140_90')
    if r.pe_status=='no_PE' and ((pd.notna(s) and s>=140) or (pd.notna(d) and d>=90)): f.append('no_pe_with_bp_ge_140_90')
    if pd.isna(s) or pd.isna(d): f.append('bp_missing')
    if pd.isna(r.birthweight_lower_g): f.append('birthweight_missing')
    return ';'.join(f) if f else 'none'
meta['qc_flags']=meta.apply(flags,axis=1)
# ---------- counts ----------
def read(path):
    s=pd.read_csv(path,sep='\t',header=None,names=['gene','count'],quotechar='"',dtype={'gene':str})
    s['gene']=s.gene.str.strip(); return s
files=sorted(glob.glob(f'{RAW}/geo/files/*.count.txt.gz'))
mats={}; summ={}
for p in files:
    sid=re.search(r'_(S\d\d_(VT|DB))\.count',p).group(1)
    s=read(p); special=s.gene.str.startswith('__')
    summ[sid]=s[special].set_index('gene')['count']
    body=s[~special]
    assert not body.gene.duplicated().any(), sid
    mats[sid]=body.set_index('gene')['count']
C=pd.DataFrame(mats); assert C.notna().all().all()
C=C.astype('int64'); assert (C>=0).all().all()
C.index.name='gene'
vt=[c for c in C.columns if c.endswith('_VT')]; db=[c for c in C.columns if c.endswith('_DB')]
assert len(vt)==30 and len(db)==27
S=pd.DataFrame(summ).T; S.index.name='sample_id'
S.columns=[c.lstrip('_') for c in S.columns]
S.insert(0,'assigned_to_genes',C.sum())
# ---------- gene mapping ----------
h=pd.read_csv(f'{RAW}/hgnc/hgnc_complete_set_2026-10-06.txt',sep='\t',dtype=str,low_memory=False)
h=h[h.status=='Approved']
by_sym=h.set_index('symbol')
def explode(col):
    t=h[['hgnc_id','symbol',col]].dropna().assign(k=lambda d:d[col].str.split('|')).explode('k')
    t=t.groupby('k').agg(list); return t
prev=explode('prev_symbol'); alias=explode('alias_symbol')
rows=[]
for gname in C.index:
    if gname in by_sym.index:
        r=by_sym.loc[gname]; rows.append((gname,r.hgnc_id,gname,r.ensembl_gene_id,r.locus_type,'approved_symbol')); continue
    hit=None
    for tab,method in ((prev,'previous_symbol'),(alias,'alias_symbol')):
        if gname in tab.index:
            ids=tab.loc[gname,'hgnc_id']
            if len(set(ids))==1:
                r=h[h.hgnc_id==ids[0]].iloc[0]; hit=(gname,r.hgnc_id,r.symbol,r.ensembl_gene_id,r.locus_type,method)
            else: hit=(gname,None,None,None,None,f'ambiguous_{method}')
            break
    rows.append(hit or (gname,None,None,None,None,'unmapped'))
A=pd.DataFrame(rows,columns=['gene','hgnc_id','hgnc_symbol','ensembl_gene_id','locus_type','mapping_status']).set_index('gene')
dup=A.hgnc_id.notna() & A.hgnc_id.duplicated(keep=False)
A['shares_hgnc_id_with_other_row']=np.where(dup,'yes','no')
# ---------- write ----------
os.makedirs(f'{OUT}/extension/decidua',exist_ok=True); os.makedirs(f'{OUT}/qc',exist_ok=True)
C[vt].to_csv(f'{OUT}/track01_counts_vt.csv')
mvt=meta[meta.tissue=='VT'].drop(columns='tissue').set_index('sample_id').loc[vt]
mvt.to_csv(f'{OUT}/track01_metadata_vt.csv',na_rep='NA')
C[db].to_csv(f'{OUT}/extension/decidua/track01_counts_db.csv')
mdb=meta[meta.tissue=='DB'].drop(columns='tissue').set_index('sample_id').loc[db]
mdb.to_csv(f'{OUT}/extension/decidua/track01_metadata_db.csv',na_rep='NA')
A.to_csv(f'{OUT}/track01_gene_annotation.csv',na_rep='NA')
S.loc[vt+db].to_csv(f'{OUT}/qc/track01_htseq_summary.csv')
print(C.shape, A.mapping_status.value_counts().to_dict(), int(dup.sum()))
print(mvt.qc_flags.value_counts().to_string()); print(mvt.group.value_counts().to_dict())
