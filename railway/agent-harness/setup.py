from setuptools import setup
setup(
    name='cli-anything-railway',
    version='1.0.0',
    packages=['cli_anything.railway'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-railway=cli_anything.railway:cli']},
)
