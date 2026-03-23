from setuptools import setup
setup(
    name='cli-anything-frequency',
    version='1.0.0',
    packages=['cli_anything.frequency'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-frequency=cli_anything.frequency:cli']},
)
