from setuptools import setup
setup(
    name='cli-anything-triton',
    version='1.0.0',
    packages=['cli_anything.triton'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-triton=cli_anything.triton:cli']},
)
