from setuptools import setup
setup(
    name='cli-anything-gnome',
    version='1.0.0',
    packages=['cli_anything.gnome'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gnome=cli_anything.gnome:cli']},
)
