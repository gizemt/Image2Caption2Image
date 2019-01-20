package(default_visibility = [":internal"])

licenses(["notice"])  # Apache 2.0

exports_files(["LICENSE"])

package_group(
    name = "internal",
    packages = [
        "//im2txt/...",
    ],
)

py_binary(
    name = "build_mscoco_data",
    srcs = [
        "data/build_mscoco_data.py",
    ],
)

sh_binary(
    name = "download_and_preprocess_mscoco",
    srcs = ["data/download_and_preprocess_mscoco.sh"],
    data = [
        ":build_mscoco_data",
    ],
)

py_library(
    name = "configuration",
    srcs = ["configuration.py"],
    srcs_version = "PY2AND3",
)

###Added by Tarek

# py_library(
#    name = "common_shapes",
#    srcs = ["common_shapes.py"],
#    srcs_version = "PY2AND3",
#)

py_library(
    name = "constant_op",
    srcs = ["constant_op.py"],
    srcs_version = "PY2AND3",
    deps = [
# "common_shapes"
    ],
)

py_library(
    name = "file_io",
    srcs = ["file_io.py"],
    srcs_version = "PY2AND3",
)


py_library(
    name = "learning",
    srcs = ["learning.py"],
    srcs_version = "PY2AND3",
    deps = [
	":constant_op",
	":file_io",
    ],
)
#######

py_library(
    name = "show_and_tell_model",
    srcs = ["show_and_tell_model.py"],
    srcs_version = "PY2AND3",
    deps = [
        "//im2txt/ops:image_embedding",
        "//im2txt/ops:image_processing",
        "//im2txt/ops:inputs",
	"//im2txt/ops:inception_v3",
	":learning",
    ],
)

py_test(
    name = "show_and_tell_model_test",
    size = "large",
    srcs = ["show_and_tell_model_test.py"],
    deps = [
        ":configuration",
        ":show_and_tell_model",
    ],
)

py_library(
    name = "inference_wrapper",
    srcs = ["inference_wrapper.py"],
    srcs_version = "PY2AND3",
    deps = [
        ":show_and_tell_model",
        "//im2txt/inference_utils:inference_wrapper_base",
    ],
)

py_binary(
    name = "train",
    srcs = ["train.py"],
    srcs_version = "PY2AND3",
    deps = [
        ":configuration",
        ":show_and_tell_model",
    ],
)

py_binary(
    name = "evaluate",
    srcs = ["evaluate.py"],
    srcs_version = "PY2AND3",
    deps = [
        ":configuration",
        ":show_and_tell_model",
    ],
)

py_binary(
    name = "run_inference",
    srcs = ["run_inference.py"],
    srcs_version = "PY2AND3",
    deps = [
        ":configuration",
        ":inference_wrapper",
        "//im2txt/inference_utils:caption_generator",
        "//im2txt/inference_utils:vocabulary",
    ],
)
