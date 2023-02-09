import scanpy as sc

## VIASH START

par = {
    'input': 'resources_test/batch_integration/feature/integrated.h5ad',
    'ouput': 'output.h5ad'
}

meta = {
    'functionality_name': 'foo'
}

## VIASH END

print('Read input', flush=True)
adata= sc.read_h5ad(par['input'])

print('Run PCA', flush=True)
adata.obsm['X_emb'] = sc.pp.pca(
    adata.X,
    n_comps=50,
    use_highly_variable=False,
    svd_solver='arpack',
    return_info=False
)
del adata.X

print('Store outputs', flush=True)
adata.uns['parent_method_id'] = adata.uns['method_id']
adata.uns['method_id'] = meta['functionality_name']
adata.write_h5ad(par['output'], compression='gzip')