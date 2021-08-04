package(default_visibility = ["PUBLIC"])

subinclude("//build/please:python.plz")

python_library(
  name="oaas-lib",
  srcs=glob([
    "oaas/**/*.py",
  ]),
)

ge_python_library(
  name="oaas",
  srcs=glob(["oaas/**/*.py"]),
)
