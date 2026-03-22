from setuptools import setup
setup(
    name='cli-anything-file_cmd',
    version='1.0.0',
    packages=['cli_anything.file_cmd'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-file_cmd=cli_anything.file_cmd:cli']},
)
