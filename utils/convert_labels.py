import os.path as path
import os


def convert(labels_folder):
    for fname in os.listdir(labels_folder):
        if fname.startswith('.'):
            # ignore dot files
            continue
        new_labels_folder = labels_folder.replace('original_', '')
        with open(path.join(labels_folder, fname), 'r') as f:
            source = f.readline()
            gsd = f.readline()
            with open(path.join(new_labels_folder, fname), 'w') as nf:
                for label in f:
                    things = label.split(' ')
                    x1, y1, x2, y2, x3, y3, x4, y4 = map(float, things[:8])
                    category = things[8]
                    difficult = things[9]  # not used now
                    xmin = min(x1, x2, x3, x4)
                    xmax = max(x1, x2, x3, x4)
                    ymin = min(y1, y2, y3, y4)
                    ymax = max(y1, y2, y3, y4)
                    print(f'{category} {(xmax-xmin)/2+xmin} {(ymax-ymin)/2+ymin} {xmax-xmin} {ymax-ymin}', file=nf)


if __name__ == '__main__':
    convert('yolo/pytorch_custom_yolo_training/data/artifacts/original_labels')