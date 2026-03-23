from setuptools import setup
setup(
    name='cli-anything-move',
    version='1.0.0',
    packages=['cli_anything.move'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-move=cli_anything.move:cli']},
)
