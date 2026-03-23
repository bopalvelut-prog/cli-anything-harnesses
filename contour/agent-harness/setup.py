from setuptools import setup
setup(
    name='cli-anything-contour',
    version='1.0.0',
    packages=['cli_anything.contour'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-contour=cli_anything.contour:cli']},
)
