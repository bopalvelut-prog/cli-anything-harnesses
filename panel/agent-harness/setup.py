from setuptools import setup
setup(
    name='cli-anything-panel',
    version='1.0.0',
    packages=['cli_anything.panel'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-panel=cli_anything.panel:cli']},
)
