# Experiment Notes

All results below come from the saved notebook run. The original CNN and MLP were trained for 5 epochs with Adam (learning rate 0.001), batch size 64, and the same MNIST split.

| Model | Final validation accuracy | Test accuracy |
|---|---:|---:|
| CNN | 98.58% | 98.82% |
| MLP | 96.68% | 97.31% |
| CNN + augmentation | 98.82% | 99.01% |

The most frequent directional error in the original CNN's test confusion matrix was 8 → 9 (10 images). On five personal handwritten images, whole-image resizing gave 2/5 correct. Cropping the digit, preserving aspect ratio, resizing to fit 20 × 20, and centering on a 28 × 28 canvas gave 5/5 correct with the same weights. Five images are too few to estimate general real-world accuracy.

The notebook contains the plots and model outputs; screenshots are not duplicated here.
