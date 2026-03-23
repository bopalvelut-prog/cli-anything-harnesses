from setuptools import setup
setup(
    name='cli-anything-appimage',
    version='1.0.0',
    packages=['cli_anything.appimage'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-appimage=cli_anything.appimage:cli']},
)
