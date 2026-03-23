from setuptools import setup
setup(
    name='cli-anything-undo',
    version='1.0.0',
    packages=['cli_anything.undo'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-undo=cli_anything.undo:cli']},
)
