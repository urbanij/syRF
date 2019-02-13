# syRF

<!-- CAD tool to help you design RF and microwave circuits.<br> -->

Check [this webpage](https://urbanij.github.io/syRF/) for an overview.

### Prerequisites


[Python](https://www.python.org/)3 installed on your machine – preferably via [Anaconda](https://www.anaconda.com/download/), to make things as smooth as possible. 
This way [other](https://docs.anaconda.com/anaconda/packages/old-pkg-lists/4.3.1/py35/) useful/mandatory packages such as Numpy and Matplotlib will be installed as well.

`PyQt5` i.e. the GUI engine is also mandatory. If not already installed do that by typing

```sh
pip3 install PyQt5
``` 

### Running

Clone/download the repository on your local machine and `cd` into it

then 
```sh
cd src/main/python
```
and finally
```sh
python3 main.py
```
to launch it.

<br>
Alternatively save the file `syRF_launch` (or `syRF_launch.bat` if on Windows), [edit the path](https://github.com/urbanij/syRF/blob/master/syRF_launch#L5), change its permission to executable `chmod +x syRF_launch` and use that to launch the app.



## Contributing

Please read [CONTRIBUTING.md](https://github.com/urbanij/syRF/blob/master/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests.


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

