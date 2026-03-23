from setuptools import setup
setup(
    name='cli-anything-forward',
    version='1.0.0',
    packages=['cli_anything.forward'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-forward=cli_anything.forward:cli']},
)
