import argparse

def get_train_test_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--batch-size', type=int, default=64)
    parser.add_argument('--num-epochs', type=int, default=3)
    parser.add_argument('--lr', type=float, default=3e-5)
    parser.add_argument('--num-visuals', type=int, default=10)
    parser.add_argument('--seed', type=int, default=42)
    parser.add_argument('--save-dir', type=str, default='save/')
    parser.add_argument('--train', action='store_true')
    parser.add_argument('--eval', action='store_true')
    parser.add_argument('--train-datasets', type=str, default='squad,nat_questions,newsqa')
    parser.add_argument('--run-name', type=str, default='multitask_distilbert')
    parser.add_argument('--recompute-features', action='store_true')
    parser.add_argument('--train-dir', type=str, default='datasets/indomain_train')
    parser.add_argument('--val-dir', type=str, default='datasets/indomain_val')
    parser.add_argument('--eval-dir', type=str, default='datasets/oodomain_test')
    parser.add_argument('--eval-datasets', type=str, default='race,relation_extraction,duorc')
    parser.add_argument('--do-train', action='store_true')
    parser.add_argument('--do-eval', action='store_true')
    parser.add_argument('--do-vanilla-finetune', action='store_true')
    parser.add_argument('--vanilla-finetune-train-dir', type=str, default='datasets/oodomain_train')
    parser.add_argument('--vanilla-finetune-val-dir', type=str, default='datasets/oodomain_val')
    parser.add_argument('--sub-file', type=str, default='')
    parser.add_argument('--visualize-predictions', action='store_true')
    parser.add_argument('--eval-every', type=int, default=5000)
    parser.add_argument('--baseline-model-dir', type=str, default='save/baseline-01/checkpoint')

    args = parser.parse_args()
    return args

# Train a baseline system with python:
# python train.py --do-train --eval-every 2000 --run-name baseline
# 
# Evaluate the system on test set with python:
# python train.py --do-eval --sub-file mtl_submission.csv --save-dir save/baseline-01 
# 
# Train a fine-tune model based on baseline system:
# python train.py --do-train --do-vanilla-finetune --eval-every 1000  --run-name vanilla-finetune --baseline-model-dir save/baseline-01/checkpoint
#
# Evaluate the fine-tune system on test set with python:
# python train.py --do-eval --sub-file mtl_submission.csv --save-dir save/vanilla-finetune-01





