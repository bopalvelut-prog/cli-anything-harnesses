from setuptools import setup
setup(
    name='cli-anything-nim',
    version='1.0.0',
    packages=['cli_anything.nim'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nim=cli_anything.nim:cli']},
)
