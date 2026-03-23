from setuptools import setup
setup(
    name='cli-anything-linear',
    version='1.0.0',
    packages=['cli_anything.linear'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-linear=cli_anything.linear:cli']},
)
