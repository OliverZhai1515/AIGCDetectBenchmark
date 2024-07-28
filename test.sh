# CUDA_VISIBLE_DEVICES=0,1 python eval_all.py --detect_method Gram --model_path ./weights/classifier/Gram.pth
# CUDA_VISIBLE_DEVICES=0,1 python eval_all.py --detect_method FreDect --model_path ./weights/classifier/DCTAnalysis.pth
# CUDA_VISIBLE_DEVICES=0,1 python eval_all.py --detect_method LGrad --model_path ./weights/classifier/LGrad.pth
CUDA_VISIBLE_DEVICES=0 python eval_all.py --detect_method DIRE --model_path ./weights/classifier/DIRE.pth

