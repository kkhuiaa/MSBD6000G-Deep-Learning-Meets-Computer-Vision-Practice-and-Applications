# MSBD6000G-Spring2019

For assignment, please check the subfolder.

Group project for MSBD6000G

## Getting Started
Important: it is assumed that the pwd is in root directory of this project (if not, please use cd command to change the driectory)

### Prerequisites
The script is written in python 3 with required packages:
```
numpy==1.15.4
scipy==1.2.0
pandas==0.24.2
opencv==3.4.4
keras==2.2.4
tensorflow==1.13.1
matplotlib==3.0.4
```

### Installing
os, time, pickle, warnings should be installed already when installing python. For installing specific version of package, you can install it as follow: (through pip)
```
pip install -Iv pandas==0.23.4
```

### Run the script

To run step1:
```
pip3 step1/fashion.py
```

To run step2:
```
python3 step2/cagan.py
```

If you do not have the data in step2/input, please run
```
python3 step2/data.py
```
For step2, please make sure you have GPU environment to build the model.

### Coding style tests

The scipt follows [pip8](https://www.python.org/dev/peps/pep-0008/) standard python notation.

### Acknowledgments
Model has been considered and modified from [anish9](https://github.com/anish9/Fashion-AI-segmentation) and [shaoanlu](https://github.com/shaoanlu/Conditional-Analogy-GAN-keras/).

### Authors
* **Hui Kwat Kong** - *20123133*
* **Song Yangyang** - *20534320*
