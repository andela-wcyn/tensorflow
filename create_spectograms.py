import subprocess
import os


def spectogramify(input_wav, output_image):
    specto_file = 'tensorflow/examples/wav_to_spectrogram:wav_to_spectrogram'
    subprocess.call(['bazel', 'run', specto_file, '--',
                     '--input_wav={}'.format(input_wav),
                     '--output_image={}'.format(output_image) ])

def main():
    input_base_dir = '/Users/wcyn/projects/tensorflow_data/speech_dataset'
    output_base_dir = '/Users/wcyn/projects/tensorflow_data/spectograms'

    for subdir, dirs, files in os.walk(input_base_dir):
        for input_wav in files:
            # print(os.path.join(subdir, file))
            folder = subdir.split('/')[-1]
            # print("Subdir: ", subdir.split('/')[-1], "Dir: ", dirs)
            filepath = subdir + os.sep + input_wav
            output_image = output_base_dir + os.sep + folder + os.sep + \
                            input_wav.replace('.wav', '.png')
            if filepath.endswith(".wav"):
                # spectogramify(input_wav, output_image)
                print('Output Image: ', output_image)
                spectogramify(filepath, output_image)

if __name__ == '__main__':
    main()