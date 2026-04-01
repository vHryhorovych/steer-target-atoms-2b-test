from huggingface_hub import snapshot_download, hf_hub_download

snapshot_download(
    repo_id="google/gemma-2-2b",
    local_dir="./model/a/gemma-2-2b",
    local_dir_use_symlinks=False,
)
hf_hub_download(
  repo_id="google/gemma-scope-2b-pt-res", 
  filename="layer_14/width_16k/average_l0_173/params.npz",
  local_dir="./sae/gemma-2-2b",
)
  
