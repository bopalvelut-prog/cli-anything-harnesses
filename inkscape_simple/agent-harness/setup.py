from setuptools import setup
setup(
    name='cli-anything-inkscape_simple',
    version='1.0.0',
    packages=['cli_anything.inkscape_simple'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-inkscape_simple=cli_anything.inkscape_simple:cli']},
)
