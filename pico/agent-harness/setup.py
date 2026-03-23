from setuptools import setup
setup(
    name='cli-anything-pico',
    version='1.0.0',
    packages=['cli_anything.pico'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pico=cli_anything.pico:cli']},
)
