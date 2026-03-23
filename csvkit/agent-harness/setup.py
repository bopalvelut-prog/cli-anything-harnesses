from setuptools import setup
setup(
    name='cli-anything-csvkit',
    version='1.0.0',
    packages=['cli_anything.csvkit'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-csvkit=cli_anything.csvkit:cli']},
)
