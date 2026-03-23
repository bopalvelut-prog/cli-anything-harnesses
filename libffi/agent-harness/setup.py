from setuptools import setup
setup(
    name='cli-anything-libffi',
    version='1.0.0',
    packages=['cli_anything.libffi'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-libffi=cli_anything.libffi:cli']},
)
