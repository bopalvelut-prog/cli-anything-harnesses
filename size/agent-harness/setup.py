from setuptools import setup
setup(
    name='cli-anything-size',
    version='1.0.0',
    packages=['cli_anything.size'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-size=cli_anything.size:cli']},
)
