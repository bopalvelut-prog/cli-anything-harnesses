from setuptools import setup
setup(
    name='cli-anything-flatpak',
    version='1.0.0',
    packages=['cli_anything.flatpak'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-flatpak=cli_anything.flatpak:cli']},
)
