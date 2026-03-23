from setuptools import setup
setup(
    name='cli-anything-taper',
    version='1.0.0',
    packages=['cli_anything.taper'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-taper=cli_anything.taper:cli']},
)
