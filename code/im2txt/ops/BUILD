package(default_visibility = ["//im2txt:internal"])

licenses(["notice"])  # Apache 2.0

exports_files(["LICENSE"])

py_library(
    name = "image_processing",
    srcs = ["image_processing.py"],
    srcs_version = "PY2AND3",
)

#####Added by Tarek
py_library(
    name = "slim",
    srcs = ["slim.py"],
    srcs_version = "PY2AND3",
)

py_library(
    name = "inception_v3",
    srcs = ["inception_v3.py"],
    srcs_version = "PY2AND3",
    deps = [
        ":slim"
     ],
)
###########

py_library(
    name = "image_embedding",
    srcs = ["image_embedding.py"],
    srcs_version = "PY2AND3",
     deps = [
        ":inception_v3",
	":slim"
	#"//im2txt/ops/slim:slim",
     ],
)

py_test(
    name = "image_embedding_test",
    size = "small",
    srcs = ["image_embedding_test.py"],
    deps = [
        ":image_embedding",
    ],
)

py_library(
    name = "inputs",
    srcs = ["inputs.py"],
    srcs_version = "PY2AND3",
)
