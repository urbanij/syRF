# syRF

<!-- CAD tool to help you design RF and microwave circuits.<br> -->

Check [this webpage](https://urbanij.github.io/syRF/) for an overview.

##### Demo 

[![Alt Text](./doc/demo/syRF.gif)](https://youtu.be/yJPomOStffk)

Watch full video [demo](https://youtu.be/yJPomOStffk).


### How to

#### Prerequisites
If not yet installed on your machine, install:
- install [Python3.7](https://www.python.org/)
- install [pipenv](https://github.com/pypa/pipenv)

#### Running

Clone/download the repository locally
```sh
git clone https://github.com/urbanij/syRF.git
```
and `cd` into it.
```sh
cd syRF
```
Then activate the virtual environment
```sh
pipenv shell
```
and download the mandatory third-party library/packages:
```sh
pipenv sync
```
If the process ends successfully it should print: "All dependencies are now up-to-date!"

Now type 
```sh
make
```
to generate the Python GUI files, and finally
```sh
./syRF_launch
```
to launch the application.



## Contributing

Please read [CONTRIBUTING.md](https://github.com/urbanij/syRF/blob/master/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests.

## TODO

- Turn this into a stand alone, easy-distributable application.

## Authors

* [Francesco Urbani](https://urbanij.github.io/)

See also the list of [contributors](https://github.com/urbanij/syRF/graphs/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/urbanij/syRF/blob/master/LICENSE) file for details

## Acknowledgments

- [WebPlotDigitizer](https://automeris.io/WebPlotDigitizer/) used to extract the data of the printed plots into a handy `.csv` file ready to be plotted and manipulated.
- [PyQt5](https://pypi.python.org/pypi/PyQt5) and [Qt Designer](http://doc.qt.io/qt-5/qtdesigner-manual.html) used to create the GUI.
- [SciPy](https://www.scipy.org/) used to interpolate the data and smooth the functions.
- [Matplotlib](https://matplotlib.org/) used to display the plots

