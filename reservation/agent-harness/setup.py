from setuptools import setup
setup(
    name='cli-anything-reservation',
    version='1.0.0',
    packages=['cli_anything.reservation'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-reservation=cli_anything.reservation:cli']},
)
