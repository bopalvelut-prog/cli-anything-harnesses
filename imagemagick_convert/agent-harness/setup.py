from setuptools import setup
setup(
    name='cli-anything-imagemagick_convert',
    version='1.0.0',
    packages=['cli_anything.imagemagick_convert'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-imagemagick_convert=cli_anything.imagemagick_convert:cli']},
)
