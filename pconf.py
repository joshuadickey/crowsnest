apps = {
    'starter' : 6001,
    'proc_data' : 6002,
    'picker' : 6003,
    'assoc_feed' : 6004,
    'assoc' : 6005,
    'origin' : 6006,
    'catalog' : 6007,
    'loci' : 6008
}

head = {"Content-Type":"application/json"}
host = '127.0.0.1'

model_folder = 'models'
picker_model = 'f:64|k:20|d:2x4x16x256|s:2|bs:100|o_len:1800|w_len:1800|n_phs:4|shift:0|left_trim:500|right_trim:1000|r_smp:20|f_low:0.5|f_hig:8|c_len:60|c_buf:0|c_shp:gauss|c_amp:1|noise:0.1|mixed:0.1|lr:0.0005|pat:10|time:1627374037.h5'
assoc_model = 'MatrixLink.h5'