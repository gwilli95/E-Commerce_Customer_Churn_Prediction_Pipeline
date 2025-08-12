#centralized configuration and variable definitions (variables, paths, parameter values)

import pathlib
SOURCE_PATH = pathlib.Path(__file__).resolve().parent
DATA_PATH = SOURCE_PATH.joinpath("data")
NOTEBOOKS_PATH = SOURCE_PATH.joinpath("notebooks")
MODELS_PATH = SOURCE_PATH.joinpath("models")