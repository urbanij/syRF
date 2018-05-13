all:
	# pyuic5 -x syRF.ui -o syRF.py # create a runnable python script
	pyuic5 syRF_ui.ui > syRF_ui.py # create a non runnable python script but makes it suitable to be embedded into *_GUI.py which is then run as usual.

clean:
	rm -rf __pycache__/
	rm -rf twoport/__pycache__/
	rm -rf microstrip_matching/__pycache__/
	rm *.pyc
	