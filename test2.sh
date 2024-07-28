CUDA_VISIBLE_DEVICES=0,1 python eval_all.py --detect_method UnivFD --model_path ./weights/classifier/UnivFD.pth
CUDA_VISIBLE_DEVICES=0,1 python eval_all.py --detect_method RPTC --model_path ./weights/classifier/RPTC.pth
CUDA_VISIBLE_DEVICES=0,1 python eval_all.py --detect_method LNP --model_path ./weights/classifier/LNP.pth