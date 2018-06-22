GAME_SETTINGS = "GameSettings.ini"

def _get_config_file_name():
	return os.path.join(os.getcwd(), "data", "r6_dir.dat")


def get_config_root_directory():
	with open(_get_config_file_name()) as file:
		return file.readline().rstrip("\n")


def set_config_file_directory(new_config):
	with open(_get_config_file_name(), 'w') as file:
		file.write(new_config)


def is_valid_subdir(rootdir, subdir):
	valid = os.path.isdir(os.path.join(rootdir, subdir))
	if valid:
		# Each game contains a hash code of 4 number sequences separated by a dash.
		valid = len(subdir.split("-")) is 4

	return valid


def get_all_r6_settings_files():
	root_filepath = get_config_root_directory()
	subdirs = os.listdir(root_filepath)
	subdirs = [f for f in subdirs if is_valid_subdir(root_filepath, f)]
	return [os.path.join(f, GAME_SETTINGS)]
