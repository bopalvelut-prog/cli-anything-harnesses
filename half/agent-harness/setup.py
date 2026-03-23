from setuptools import setup
setup(
    name='cli-anything-half',
    version='1.0.0',
    packages=['cli_anything.half'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-half=cli_anything.half:cli']},
)
