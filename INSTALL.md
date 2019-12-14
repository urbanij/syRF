#### Running <sup>1</sup>

Either clone 
```sh
git clone https://github.com/urbanij/syRF.git
``` 
or download the repository locally
and `cd` into it.
```sh
cd syRF
```
Then activate the virtual environment
```sh
pipenv shell
```
and sync/download the mandatory third-party libraries/packages
```sh
pipenv sync
```
If the process finishes successfully it should print: _All dependencies are now up-to-date!_

Now type 
```sh
make
```
to generate the Python GUI files from the XMLs, and finally
```sh
./syRF_launch
```
to launch the application. (use `syRF_launch.bat` if you're on Windows)




<sup>1</sup>: It works even on Windows but it can be slightly more cumbersome. You might need to add to the environment variables at least `python` and `pipenv` if you want to avoid writing the whole executable path each time. To do that open the environment variables settings and add to `path`: `C:\Users\<your_username>\AppData\Local\Programs\Python\Python37` and `C:\Users\<your_username>\AppData\Local\Programs\Python\Python37\Scripts`.

`make` too may fail: if that happens just paste each command inside `all` into the terminal, separately.

Get in touch if you have trouble or just use your favorite flavor of Linux.

