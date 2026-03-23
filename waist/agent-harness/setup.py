from setuptools import setup
setup(
    name='cli-anything-waist',
    version='1.0.0',
    packages=['cli_anything.waist'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-waist=cli_anything.waist:cli']},
)
