TARGET=syRF

FLAGS=--remove-output --follow-imports

all: ui $(TARGET)


ui: ../../../ui/syRF.ui ../../../ui/rect2polar.ui ../../../ui/lambda4.ui ../../../ui/about.ui ../../../ui/microstrip_matching_window.ui  ../../../ui/smith_chart.ui ../../../ui/lumped_matching.ui ../../../ui/check_update.ui ../../../ui/new_update.ui 
	# creates non runnable python scripts
	pyuic5 ../../../ui/syRF.ui                       > pyui/syRF_ui.py
	pyuic5 ../../../ui/rect2polar.ui                 > pyui/rect2polar_ui.py
	pyuic5 ../../../ui/lambda4.ui                    > pyui/lambda4_ui.py
	pyuic5 ../../../ui/about.ui                      > pyui/about_ui.py
	pyuic5 ../../../ui/microstrip_matching_window.ui > pyui/microstrip_matching_window_ui.py
	pyuic5 ../../../ui/smith_chart.ui                > pyui/smith_chart_ui.py
	pyuic5 ../../../ui/lumped_matching.ui            > pyui/lumped_matching_ui.py
	pyuic5 ../../../ui/integrated_matching.ui        > pyui/integrated_matching_ui.py
	pyuic5 ../../../ui/check_update.ui               > pyui/check_update_ui.py
	pyuic5 ../../../ui/new_update.ui                 > pyui/new_update_ui.py



$(TARGET): main.py
	python3.6 -m nuitka $(FLAGS) main.py -o $(TARGET)



clean:
	rm $(TARGET)
	
	rm -rf __pycache__/
	rm -rf pyui/__pycache__/
	rm -rf twoport/__pycache__/
	rm -rf microstrip_matching/__pycache__/
	rm *.pyc

	
	