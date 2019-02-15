all:
	pyuic5 ../../../ui/syRF.ui > syRF_ui.py # creates a non runnable python script
	pyuic5 ../../../ui/rect2polar.ui > rect2polar_ui.py
	pyuic5 ../../../ui/lambda4.ui > lambda4_ui.py

clean:
	rm -rf __pycache__/
	rm -rf twoport/__pycache__/
	rm -rf microstrip_matching/__pycache__/
	rm *.pyc