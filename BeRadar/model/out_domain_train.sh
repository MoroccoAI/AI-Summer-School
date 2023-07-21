for seed in {1..100}
do
    for shots in {1..10}
    do
        python train.py --n-shots $shots  --val-shots 0 --batch-size 128 --backbone clip_l14 --n-aug 1 --train-transforms "['clip_l14','centercrop']" --test-transforms "['clip_l14','resize_1.2','centercrop']" --dataset-path data/dataset/area1/ --device cuda:0 --seed $seed --preprocessing 'ME' --log-metrics data/logs/ --test-dataset-path data/beradar/area2/
    done
done