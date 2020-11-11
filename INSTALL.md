#### Running <sup>1</sup>

Either clone 
```sh
git clone https://github.com/urbanij/syRF.git
``` 
or download the repository locally
and `cd` into it:
```sh
cd syRF
```
then create/activate the virtual environment
```sh
pipenv shell
```
and install the dependencies
```sh
pip install -r requirements.txt
```

then
```sh
make
```
to generate the Python UI files from the XMLs.

and finally type `./syRF_launch` to launch the main app or one of the other launchers such as `./smith`, `./stub_matching` to launch the Smith chart tool and the stub matching tool respectively.

---




<sup>1</sup>: It works even on Windows but it can be slightly more cumbersome. You might need to add to the environment variables at least `python` and `pipenv` if you want to avoid writing the whole executable path each time. To do that open the environment variables settings and add to `path`: `C:\Users\<your_username>\AppData\Local\Programs\Python\Python37` and `C:\Users\<your_username>\AppData\Local\Programs\Python\Python37\Scripts`.

`make` too may fail: if that happens just paste each command inside `all` into the terminal, separately.

Get in touch if you have trouble or just use Linux.
