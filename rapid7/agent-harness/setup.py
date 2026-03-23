from setuptools import setup
setup(
    name='cli-anything-rapid7',
    version='1.0.0',
    packages=['cli_anything.rapid7'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rapid7=cli_anything.rapid7:cli']},
)
