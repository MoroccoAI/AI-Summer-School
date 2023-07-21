for seed in {1..400}
do
    python train.py --n-shots 10 --val-shots 10 --batch-size 128 --backbone clip_l14 --n-aug 1 --train-transforms "['clip_l14','centercrop']" --test-transforms "['clip_l14','resize_1.2','centercrop']" --dataset-path data/dataset/area1/ --device cuda:0 --seed $seed --preprocessing 'ME' --log-metrics data/logs/ #--test-dataset-path data/dataset/area1/
done
