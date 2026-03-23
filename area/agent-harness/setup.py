from setuptools import setup
setup(
    name='cli-anything-area',
    version='1.0.0',
    packages=['cli_anything.area'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-area=cli_anything.area:cli']},
)
