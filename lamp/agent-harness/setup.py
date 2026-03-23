from setuptools import setup
setup(
    name='cli-anything-lamp',
    version='1.0.0',
    packages=['cli_anything.lamp'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-lamp=cli_anything.lamp:cli']},
)
