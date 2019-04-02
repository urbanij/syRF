# syRF

<!-- CAD tool to help you design RF and microwave circuits.<br> -->

Check [this webpage](https://urbanij.github.io/syRF/) for an overview.

##### Demo 

[![Alt Text](./doc/demo/syRF.gif)](https://youtu.be/yJPomOStffk)

Watch full video [demo](https://youtu.be/yJPomOStffk).


### Prerequisites


[Python3](https://www.python.org/) is supposed to be already installed on your local machine -- if not you have two main options:

- via [Anaconda](https://www.anaconda.com/download/) which usually turns to be a smooth process since it provides useful packages<sup>1</sup> together with the main Python installation;
- from [the website](https://www.python.org/).

To check whether Python is installed correctly on your computer open a shell and type `python --version`.


<sup>1</sup> This way [other](https://docs.anaconda.com/anaconda/packages/old-pkg-lists/4.3.1/py35/) useful/mandatory packages such as Numpy and Matplotlib will be installed as well.



### Running

These steps are also written in the text file `./venv_steps.txt`. 


Clone/download the repository on your local machine 
```sh
git clone https://github.com/urbanij/syRF.git
```
and `cd` into it.
```sh
cd syRF
```
Then create a virtual environment and activate it
```sh
python3 -m venv venv
source venv/bin/activate
```
install the required libraries (like PyQt5 for the GUI, Matplotlib for plotting, etc, which are not shipped with Python by default)
```sh
pip3 install -r requirements.txt
```
then move to the folder where the main code lives 
```sh
cd src/main/python 
```
and generate the necessary Python GUI files
```sh
make
```
and finally
```sh
python3 main.py
```
to launch the application.



Alternatively save the file `syRF_launch` (or `syRF_launch.bat` if on Windows), [edit the path](https://github.com/urbanij/syRF/blob/master/syRF_launch#L5), change its permission to executable `chmod +x syRF_launch` and use that to launch the app, the next times.



## Contributing

Please read [CONTRIBUTING.md](https://github.com/urbanij/syRF/blob/master/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests.

## TODO

- Turn this into a stand alone, easy-distributable application.

## Authors

* Francesco Urbani 

See also the list of [contributors](https://github.com/urbanij/syRF/graphs/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/urbanij/syRF/blob/master/LICENSE) file for details

## Acknowledgments

- [WebPlotDigitizer](https://automeris.io/WebPlotDigitizer/) used to extract the data of the printed plots into a handy `.csv` file ready to be plotted and manipulated.
- [PyQt5](https://pypi.python.org/pypi/PyQt5) and [Qt Designer](http://doc.qt.io/qt-5/qtdesigner-manual.html) used to create the GUI.
- [SciPy](https://www.scipy.org/) used to interpolate the data and smooth the functions.
- [Matplotlib](https://matplotlib.org/) used to display the plots

