from setuptools import setup
setup(
    name='cli-anything-buffer',
    version='1.0.0',
    packages=['cli_anything.buffer'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-buffer=cli_anything.buffer:cli']},
)
