import os

REGION_LINE_PREFIX = "DataCenterHint="
REGION_LINE_TIMEPLATE = REGION_LINE_PREFIX + "{}\n"

def get_lines(filepath):
	with open(filepath) as file:
		return file.readlines()

def write_lines(filepath, lines):
	with open(filepath, 'w') as file:
		file.write("".join(lines))

def find_region_line_idx(lines):
	for idx, line in enumerate(lines):
		if line.startswith(REGION_LINE_PREFIX):
			return idx
	raise "Data Center Line Not Found"

def swap_regions(new_region, filepath):
	new_region = str(new_region)
	lines = get_lines(filepath)
	region_line_idx = find_region_line_idx(lines)
	lines[region_lines_idx] = REGION_LINE_TEMPLATE.format(new_region)
	write_lines(filepath, lines)

def pmwd():
	print(os.getcwd())