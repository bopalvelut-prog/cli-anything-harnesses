from setuptools import setup
setup(
    name='cli-anything-tauri',
    version='1.0.0',
    packages=['cli_anything.tauri'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tauri=cli_anything.tauri:cli']},
)
