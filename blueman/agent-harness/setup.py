from setuptools import setup
setup(
    name='cli-anything-blueman',
    version='1.0.0',
    packages=['cli_anything.blueman'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-blueman=cli_anything.blueman:cli']},
)
