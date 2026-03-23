from setuptools import setup
setup(
    name='cli-anything-note',
    version='1.0.0',
    packages=['cli_anything.note'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-note=cli_anything.note:cli']},
)
