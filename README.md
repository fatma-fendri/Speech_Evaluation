# Speech_Evaluation


1) VSCode :

install ffmpeg

install yt_dlp

python audioCrawler.py

2) Anaconda prompt :


conda env create -f env.yml  


conda activate nisqa 


python run_predict.py --mode predict_dir --pretrained_model weights/nisqa.tar --data_dir C:\Users\GMI\Desktop\Speech\audio --num_workers 0 --bs 10 --output_dir C:\Users\GMI\Desktop\Speech\results  
