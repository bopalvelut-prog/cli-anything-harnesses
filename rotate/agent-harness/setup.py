from setuptools import setup
setup(
    name='cli-anything-rotate',
    version='1.0.0',
    packages=['cli_anything.rotate'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rotate=cli_anything.rotate:cli']},
)
