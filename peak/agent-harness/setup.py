from setuptools import setup
setup(
    name='cli-anything-peak',
    version='1.0.0',
    packages=['cli_anything.peak'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-peak=cli_anything.peak:cli']},
)
