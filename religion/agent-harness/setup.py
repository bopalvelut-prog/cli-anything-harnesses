from setuptools import setup
setup(
    name='cli-anything-religion',
    version='1.0.0',
    packages=['cli_anything.religion'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-religion=cli_anything.religion:cli']},
)
