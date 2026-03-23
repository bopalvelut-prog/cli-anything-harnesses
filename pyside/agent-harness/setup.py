from setuptools import setup
setup(
    name='cli-anything-pyside',
    version='1.0.0',
    packages=['cli_anything.pyside'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pyside=cli_anything.pyside:cli']},
)
