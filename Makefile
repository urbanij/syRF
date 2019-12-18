
all:
	### creates non runnable python scripts from UI files
	pyuic5 ui/mainwindow.ui                 > src/main/python/pyui/mainwindow_ui.py
	pyuic5 ui/rect2polar.ui                 > src/main/python/pyui/rect2polar_ui.py
	pyuic5 ui/lambda4.ui                    > src/main/python/pyui/lambda4_ui.py
	pyuic5 ui/about.ui                      > src/main/python/pyui/about_ui.py
	pyuic5 ui/microstrip_matching_window.ui > src/main/python/pyui/microstrip_matching_window_ui.py
	pyuic5 ui/smith_chart.ui                > src/main/python/pyui/smith_chart_ui.py
	pyuic5 ui/lumped_matching.ui            > src/main/python/pyui/lumped_matching_ui.py
	pyuic5 ui/integrated_matching.ui        > src/main/python/pyui/integrated_matching_ui.py
	pyuic5 ui/check_update.ui               > src/main/python/pyui/check_update_ui.py
	pyuic5 ui/new_update.ui                 > src/main/python/pyui/new_update_ui.py
	pyuic5 ui/impedance_at_distance.ui      > src/main/python/pyui/impedance_at_distance_ui.py
	pyuic5 ui/gamma2impedance.ui            > src/main/python/pyui/gamma2impedance_ui.py
	pyuic5 ui/parallel_stub_matching.ui     > src/main/python/pyui/parallel_stub_matching_ui.py
	

	### resources
	pyrcc5 src/main/resources/resources.qrc -o src/main/python/resources.py


clean:	
	rm -rf src/main/python/__pycache__/
	rm -rf src/main/python/pyui/__pycache__/
	rm -rf src/main/python/twoport/__pycache__/
	rm -rf src/main/python/microstrip_matching/__pycache__/
	rm -rf src/main/python/pyui/*
	rm -rf src/main/python/*.pyc
	rm -rf src/main/python/resources.py


