from setuptools import setup
setup(
    name='cli-anything-military',
    version='1.0.0',
    packages=['cli_anything.military'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-military=cli_anything.military:cli']},
)
