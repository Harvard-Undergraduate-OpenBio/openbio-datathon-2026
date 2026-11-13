import pandas as pd, numpy as np, os
OUT='track-01/data/extension/pseudobulk'
M=pd.read_pickle('build/sc_pseudobulk_fine.pkl')
dups=sorted(set(M.index[M.index.duplicated()]))
open('build/sc_duplicate_genes.txt','w').write('\n'.join(dups))
M=M.groupby(level=0,sort=False).sum()
cm=pd.read_csv('raw/figshare/cell_metadata.csv',dtype=str)
CLASS={'TB_VCT1':'villous_cytotrophoblast','TB_VCT2':'villous_cytotrophoblast','TB_VCT_proliferating':'villous_cytotrophoblast','TB_VCT_IFN':'villous_cytotrophoblast',
'TB_SCT':'syncytiotrophoblast','TB_SCT-PSG':'syncytiotrophoblast','TB_EVT1':'extravillous_trophoblast','TB_EVT2':'extravillous_trophoblast',
'IMMUNE_HOFBAUER':'hofbauer_cell','IMMUNE_HOFAUER_IFN1':'hofbauer_cell',
'IMMUNE_MACROPHAGE_TREM2':'macrophage','IMMUNE_MACROPHAGE-M1':'macrophage','IMMUNE_MACROPHAGE_IFN1':'macrophage','IMMUNE_MACROPHAGE_IFN2':'macrophage',
'IMMUNE_MONOCYTE-CLASSICAL':'monocyte','IMMUNE_MONOCYTE-NON_CLASSICAL':'monocyte',
'IMMUNE_NK':'nk_cell','IMMUNE_NK_GZMK':'nk_cell','IMMUNE_NK_PRSS57':'nk_cell',
'IMMUNE_T-NAIVE':'t_cell','IMMUNE_T-NAIVE_CD8':'t_cell','IMMUNE_T-REG':'t_cell','IMMUNE_B':'b_cell',
'IMMUNE_NEURTOPHIL':'other_immune','IMMUNE_HSC':'other_immune','IMMUNE_proliferating':'other_immune',
'VASCULAR_CAPILLARY':'endothelial_cell','VASCULAR_CAPILLARY_TIP':'endothelial_cell','VASCULAR_ARTERIAL':'endothelial_cell','VASCULAR_VENOUS':'endothelial_cell',
'VASCULAR_EC_IFN':'endothelial_cell','VASCULAR_EC_proliferating':'endothelial_cell',
'VASCULAR_PERICYTE':'pericyte','VASCULAR_PERICYTE_IFN':'pericyte','VASCULAR_SM':'smooth_muscle_cell'}
for t in cm.celltype.unique():
    if t.startswith('STROMAL_'): CLASS[t]='stromal_cell'
assert set(cm.celltype)<=set(CLASS), set(cm.celltype)-set(CLASS)
COMP={'villous_cytotrophoblast':'trophoblast','syncytiotrophoblast':'trophoblast','extravillous_trophoblast':'trophoblast','stromal_cell':'stromal',
'endothelial_cell':'vascular','pericyte':'vascular','smooth_muscle_cell':'vascular'}
cm['cell_class']=cm.celltype.map(CLASS)
# genes x (donor|class)
donor=[c.split('|')[0] for c in M.columns]; cls=[CLASS[c.split('|')[1]] for c in M.columns]
keys=[f'{d}__{c}' for d,c in zip(donor,cls)]
P=M.T.groupby(keys).sum().T
assert int(P.values.sum())==int(M.values.sum())
# donors
cm['delivery_week']=cm.delivery_week.astype(float)
dg=cm.groupby('donorID')
D=pd.DataFrame(index=sorted(cm.donorID.unique())); D.index.name='donor_id'
first=dg.first()
D['pe_status']=np.where(D.index.str.startswith('PE'),'PE','control')
D['onset_group']=[('early' if (first.loc[d,'early_PE']=='1' or first.loc[d,'early_control']=='1') else 'late') for d in D.index]
D['clinical_group']=D.pe_status+'_'+D.onset_group
D['early_onset_comparison']=np.where(D.onset_group=='early','exploratory_3_control_vs_10_PE','not_applicable')
D['fgr_status']=np.where(first.IUGR=='1','FGR','no_FGR')
D['fetal_sex']=np.where(first.female_fetus=='1','female','male')
D['delivery_mode']=np.select([first['C-section_birth']=='1',first.vaginal_birth=='1'],['c_section','vaginal'],'NA')
D['labor_induction']=np.select([first.induction=='1',first['non-induction']=='1'],['yes','no'],'NA')
D['magnesium_sulfate']=np.where(first.magnesium=='1','yes','no')
def anesth(r):
    a=[n for n,c in (('spinal','spinal_anaesthesia'),('epidural','epidural_anaesthesia'),('general','general_anaesthesia')) if r[c]=='1']
    return '+'.join(a) if a else 'none_recorded'
D['anesthesia']=first.apply(anesth,axis=1)
D['ga_delivery_weeks']=first.delivery_week.astype(float).round(3)
D['birthweight_g']=pd.to_numeric(first.weight,errors='coerce').astype('Int64')
D['birthweight_percentile_dolberg']=pd.to_numeric(first['wieght_percentile-Dolberg'],errors='coerce')
D['maternal_age_years']=pd.to_numeric(first.donor_age,errors='coerce').astype('Int64')
D['n_libraries']=dg['sample'].nunique()
D['library_ids']=dg['sample'].agg(lambda s:';'.join(sorted(s.unique())))
D['n_cells']=dg.size()
def f(r):
    fl=[]
    if not 20<=r.ga_delivery_weeks<=42: fl.append('ga_out_of_range')
    if r.onset_group=='early' and r.ga_delivery_weeks>=37: fl.append('early_group_delivered_at_term')
    if r.onset_group=='late' and r.ga_delivery_weeks<34: fl.append('late_group_delivered_before_34w')
    if pd.notna(r.birthweight_g) and not 300<=r.birthweight_g<=5500: fl.append('birthweight_out_of_range')
    p=r.birthweight_percentile_dolberg
    if r.fgr_status=='FGR' and pd.notna(p) and p>=10: fl.append('fgr_with_birthweight_percentile_ge10')
    if r.fgr_status=='no_FGR' and pd.notna(p) and p<3: fl.append('no_fgr_with_birthweight_percentile_lt3')
    return ';'.join(fl) or 'none'
D['qc_flags']=D.apply(f,axis=1)
# per-column metadata
nc=cm.groupby(['donorID','cell_class']).size()
rows=[]
for k in P.columns:
    d,c=k.split('__'); rows.append(dict(pseudobulk_id=k,donor_id=d,cell_class=c,compartment=COMP.get(c,'immune'),n_cells=int(nc[(d,c)]),total_counts=int(P[k].sum())))
PM=pd.DataFrame(rows).set_index('pseudobulk_id').join(D.drop(columns=['n_cells']),on='donor_id')
order=PM.sort_values(['cell_class','donor_id']).index
P=P[order]; PM=PM.loc[order]
os.makedirs(OUT,exist_ok=True)
P.index.name='gene'
P.to_csv(f'{OUT}/track01_pseudobulk_counts.csv')
PM.to_csv(f'{OUT}/track01_pseudobulk_metadata.csv',na_rep='NA')
D.to_csv(f'{OUT}/track01_pseudobulk_donors.csv',na_rep='NA')
mp=cm.groupby(['celltype','cell_class']).size().rename('n_cells').reset_index().rename(columns={'celltype':'source_cell_type'})
mp['compartment']=mp.cell_class.map(lambda c:COMP.get(c,'immune'))
mp.sort_values(['compartment','cell_class','source_cell_type']).to_csv(f'{OUT}/track01_cell_class_map.csv',index=False)
print(P.shape, PM.shape, D.shape, int(M.values.sum()))
print(D[['clinical_group']].value_counts().to_string()); print(D.qc_flags.value_counts().to_string())
print(PM.n_cells.describe().to_string()); print((PM.n_cells<10).sum(),'columns with <10 cells')
