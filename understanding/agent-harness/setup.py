from setuptools import setup
setup(
    name='cli-anything-understanding',
    version='1.0.0',
    packages=['cli_anything.understanding'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-understanding=cli_anything.understanding:cli']},
)
