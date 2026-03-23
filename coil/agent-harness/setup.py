from setuptools import setup
setup(
    name='cli-anything-coil',
    version='1.0.0',
    packages=['cli_anything.coil'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-coil=cli_anything.coil:cli']},
)
