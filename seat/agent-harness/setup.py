from setuptools import setup
setup(
    name='cli-anything-seat',
    version='1.0.0',
    packages=['cli_anything.seat'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-seat=cli_anything.seat:cli']},
)
