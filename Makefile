TARGET=syRF

FLAGS=--remove-output --follow-imports

all: ui #$(TARGET)


ui: ui/syRF.ui ui/rect2polar.ui ui/lambda4.ui ui/about.ui ui/microstrip_matching_window.ui  ui/smith_chart.ui ui/lumped_matching.ui ui/check_update.ui ui/new_update.ui 
	# creates non runnable python scripts
	pyuic5 ui/syRF.ui                       > src/main/python/pyui/syRF_ui.py
	pyuic5 ui/rect2polar.ui                 > src/main/python/pyui/rect2polar_ui.py
	pyuic5 ui/lambda4.ui                    > src/main/python/pyui/lambda4_ui.py
	pyuic5 ui/about.ui                      > src/main/python/pyui/about_ui.py
	pyuic5 ui/microstrip_matching_window.ui > src/main/python/pyui/microstrip_matching_window_ui.py
	pyuic5 ui/smith_chart.ui                > src/main/python/pyui/smith_chart_ui.py
	pyuic5 ui/lumped_matching.ui            > src/main/python/pyui/lumped_matching_ui.py
	pyuic5 ui/integrated_matching.ui        > src/main/python/pyui/integrated_matching_ui.py
	pyuic5 ui/check_update.ui               > src/main/python/pyui/check_update_ui.py
	pyuic5 ui/new_update.ui                 > src/main/python/pyui/new_update_ui.py



$(TARGET): main.py
	python3.6 -m nuitka $(FLAGS) main.py -o $(TARGET)



clean:
	rm $(TARGET)
	
	rm -rf __pycache__/
	rm -rf pyui/__pycache__/
	rm -rf twoport/__pycache__/
	rm -rf microstrip_matching/__pycache__/
	rm *.pyc

	
	