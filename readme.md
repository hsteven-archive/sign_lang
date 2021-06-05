# Sign Lang

American Sign Language (ASL) is a complete, natural language that has the same linguistic properties as spoken languages, with grammar that differs from English. This project is intent to capture the letters or numbers from stream images with power of the artificial intelligence.

![Sign_lang](docs/sign_lang.png)

## Installation

`This repository has been tested on Macos Big Sur 11.4 and Ubuntu 20.04 LTS`

- First, install python (better with version 3.9)

You could use [conda](https://www.anaconda.com/products/individual) to create a new environment
or directly download from [python 3.9](https://www.python.org/downloads/)


- Second, please download the git files.

```bash
git clone https://github.com/H-steven/sign_lang.git
```

- Third, install all the required packages with pip.

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all the necessary packages.
Python (>=3.7) supported.

```bash
cd sign_lang
python -m pip install -r requirements.txt
```

## Usage

try the demos and have fun. :)

```python
export DISPLAY=:0
python app.py
```

To obtain ground truth data, we have manually annotated ~30K real-world images with 21 3D coordinates, as shown below (we take Z-value from image depth map, if it exists per corresponding coordinate). Here is the hand landmarks.

![hand_landmarks](docs/hand_landmarks.png)

## Debug

- If you see the error that `no display name and no $DISPLAY environment variable`, 
please use this commands in your shell.

```shell
export DISPLAY=:0
```

- If you see the error `* Error performing wm_overrideredirect *` on Macos (>10.15),
please download the [python 3.9](https://www.python.org/downloads/) directly from python.org and install everything.

Please see the discussion [here](https://github.com/PySimpleGUI/PySimpleGUI/issues/3972)

- Please ignore the warnings in MacOS like this:

```shell
WARNING: Logging before InitGoogleLogging() is written to STDERR

W20210605 11:49:06.229305 124948480 tflite_model_loader.cc:32] Trying to resolve path manually as GetResourceContents failed: ; Can't find file: mediapipe/modules/palm_detection/palm_detection.tflite
```

## License

This is a private github repository. Please contact the author to get the authorization.

[MIT](https://choosealicense.com/licenses/mit/)
