 #!/bin/bash

# def spectogramify(input_wav, output_image):
#     specto_file = 'tensorflow/examples/wav_to_spectrogram:wav_to_spectrogram'
#     subprocess.call(['bazel', 'run', specto_file, '--',
#                      '--input_wav={}'.format(input_wav),
#                      '--output_image={}'.format(output_image) ])

# def main():
#     input_base_dir = '/Users/wcyn/projects/tensorflow_data/speech_dataset'
#     output_base_dir = '/Users/wcyn/projects/tensorflow_data/spectograms'

#     for subdir, dirs, files in os.walk(input_base_dir):
#         for input_wav in files:
#             # print(os.path.join(subdir, file))
#             folder = subdir.split('/')[-1]
#             # print("Subdir: ", subdir.split('/')[-1], "Dir: ", dirs)
#             filepath = subdir + os.sep + input_wav
#             output_image = output_base_dir + os.sep + folder + os.sep + \
#                             input_wav.replace('.wav', '.png')
#             if filepath.endswith(".wav"):
#                 # spectogramify(input_wav, output_image)
#                 print('Output Image: ', output_image)
#                 spectogramify(filepath, output_image)

spectogramify () {
    bazel run $1 -- \
    --input_wav=$2 \
    --output_image=$3
}
DATA_FOLDER=''
INPUT_BASE_DIR='/Users/wcyn/projects/tensorflow_data/test'$DATA_FOLDER
OUTPUT_BASE_DIR='/Users/wcyn/projects/tensorflow_data/spectograms/test'
SPECTO_FILE='tensorflow/examples/wav_to_spectrogram:wav_to_spectrogram'

for i in $( ls $INPUT_BASE_DIR ); do
    echo item: $i
    filepath=''
    if [ -d "$INPUT_BASE_DIR/$i" ]; then
        # Control will enter here if $DIRECTORY exists.
        echo 'is dir'
        for input_wav in $(ls $INPUT_BASE_DIR/$i); do
            if [[ "$input_wav" == *.wav ]]; then
                filepath=$INPUT_BASE_DIR/$i/$input_wav
                output_image="${input_wav/.wav/.png}"
                output_image_dir=$OUTPUT_BASE_DIR/$i/$output_image
                echo $output_image_dir
                if [ ! -f "$output_image_dir" ]; then
                    spectogramify $SPECTO_FILE $filepath $output_image_dir
                fi
                # echo $filepath
            fi
            # echo '$filepath'
        done
    else
        echo 'is not dir: '$i
        if [[ "$i" == *.wav ]]; then
            filepath=$INPUT_BASE_DIR/$i
            output_image="${i/.wav/.png}"
            output_image_dir=$OUTPUT_BASE_DIR$DATA_FOLDER/$output_image
            # echo $output_image_dir
            if [ ! -f "$output_image_dir" ]; then
                spectogramify $SPECTO_FILE $filepath $output_image_dir
            fi
        fi
    fi
    # echo $filepath

done