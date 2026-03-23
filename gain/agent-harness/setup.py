from setuptools import setup
setup(
    name='cli-anything-gain',
    version='1.0.0',
    packages=['cli_anything.gain'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gain=cli_anything.gain:cli']},
)
