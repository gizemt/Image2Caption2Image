TRAINING_STEPS="$1"
MSCOCO_DIR="im2txt/data/flickr_6k_1k_1k"

# Inception v3 checkpoint file.
INCEPTION_CHECKPOINT="im2txt/data/inception_v3.ckpt"

# Directory to save the model.
MODEL_DIR="im2txt/model"

#Path to bazel binaryi
export JAVA_HOME=/opt/java/jdk1.8.0_51/
export JAVA_VERSION=1.8
BAZEL_PATH=~/bin/bazel/output/bazel


# Build the model.
${BAZEL_PATH} build -c opt im2txt/...

# Run the training script.
bazel-bin/im2txt/train \
  --input_file_pattern="${MSCOCO_DIR}/train-?????-of-00256" \
  --inception_checkpoint_file="${INCEPTION_CHECKPOINT}" \
  --train_dir="${MODEL_DIR}/train_RMSProp" \
  --train_inception=false \
  --number_of_steps="$TRAINING_STEPS"

