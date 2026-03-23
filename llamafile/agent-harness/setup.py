from setuptools import setup
setup(
    name='cli-anything-llamafile',
    version='1.0.0',
    packages=['cli_anything.llamafile'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-llamafile=cli_anything.llamafile:cli']},
)
