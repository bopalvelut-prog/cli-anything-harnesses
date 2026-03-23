from setuptools import setup
setup(
    name='cli-anything-dunst',
    version='1.0.0',
    packages=['cli_anything.dunst'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dunst=cli_anything.dunst:cli']},
)
