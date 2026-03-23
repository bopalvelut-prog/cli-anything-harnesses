from setuptools import setup
setup(
    name='cli-anything-juice',
    version='1.0.0',
    packages=['cli_anything.juice'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-juice=cli_anything.juice:cli']},
)
