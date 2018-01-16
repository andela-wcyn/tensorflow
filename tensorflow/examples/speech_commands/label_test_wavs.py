import label_wav
import csv
import os
# from input_data import AudioProcessor

# audio_processor = AudioProcessor(data_dir='~/projects/tensorflow_data/test.7z')
def prepare_csv_file(csv_dir, csv_headers):
    # Delete csv file if it exists
    try:
        os.remove(csv_dir)
    except OSError:
        pass

    # Add CSV header
    with open(csv_dir, 'w') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow(csv_headers)

def label_test_files(data_dir, graph, labels, input_name,
                     output_name, how_many_labels, csv_dir=None,
                     csv_headers=None):
    test_outputs = []
    # Loop through files in all the directories to get the audio files
    # for testing
    if csv_dir:
        prepare_csv_file(csv_dir, csv_headers)
    count = 0
    for subdir, dirs, files in os.walk(data_dir):
        for file in files:
            # print(os.path.join(subdir, file))
            filepath = subdir + os.sep + file

            if filepath.endswith(".wav"):
                count += 1
                print(count, ". File: ", file)
                test_outputs.append(
                    label_wav.label_wav(
                        wav=filepath, labels=labels, graph=graph,
                        input_name=input_name, output_name=output_name,
                        how_many_labels=how_many_labels))
    return test_outputs

def print_to_csv(data, csv_dir):
  # print ("CSV Here")
  with open(csv_dir, 'a+') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    csvwriter.writerows(data)

graph = '/tmp/my_frozen_graph.pb'
labels = '/Users/wcyn/venv-projects/tensor-f-tut/tensorflow/tensorflow/examples/speech_commands/speech_labels.txt'
input_name, output_name, how_many_labels = ('wav_data:0', 'labels_softmax:0', 3)
# data_dir = '/Users/wcyn/Documents/other'
data_dir = '/Users/wcyn/projects/tensorflow_data/test'
csv_dir = '/Users/wcyn/projects/tensorflow_data/test_outputs.csv'
csv_headers = ['fname','label']


print_to_csv(label_test_files(data_dir, graph, labels, input_name, output_name,
                              how_many_labels), csv_dir)


python tensorflow/examples/speech_commands/freeze.py \
--start_checkpoint=/Users/wcyn/projects/tensorflow_data/speech_commands_train/conv.ckpt-18000 \
--output_file=/Users/wcyn/projects/tensorflow_data/my_frozen_graph.pb
