all:
	# creates non runnable python scripts
	pyuic5 ../../../ui/syRF.ui                > syRF_ui.py  
	pyuic5 ../../../ui/rect2polar.ui          > rect2polar_ui.py
	pyuic5 ../../../ui/lambda4.ui             > lambda4_ui.py
	pyuic5 ../../../ui/about.ui               > about_ui.py
	pyuic5 ../../../ui/microstrip_matching_window.ui > microstrip_matching_window_ui.py
	pyuic5 ../../../ui/smith_chart.ui         > smith_chart_ui.py
	pyuic5 ../../../ui/lumped_matching.ui     > lumped_matching_ui.py


clean:
	rm -rf __pycache__/
	rm -rf twoport/__pycache__/
	rm -rf microstrip_matching/__pycache__/
	rm *.pyc