# Training YOLO with Custom Dataset in PyTorch

Full story:
https://towardsdatascience.com/training-yolo-for-object-detection-in-pytorch-with-your-custom-dataset-the-simple-way-1aa6f56cf7d9


When using DOTA labels, have all of them in `data/artifacts/original_labels` and run `python utils\convert_labels.py`. That is a generalization of DOTA bbox, since we take the fixed bbox with max height and max weight, while DOTA labels are also non-perfect rectangles.

Execute `python createlist.py` the first time to create lists of labels and images.

Execute `python train.py` to actually train the model on your images.