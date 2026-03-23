from setuptools import setup
setup(
    name='cli-anything-tan',
    version='1.0.0',
    packages=['cli_anything.tan'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tan=cli_anything.tan:cli']},
)
