from setuptools import setup
setup(
    name='cli-anything-gui',
    version='1.0.0',
    packages=['cli_anything.gui'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gui=cli_anything.gui:cli']},
)
