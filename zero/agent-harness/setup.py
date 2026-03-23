from setuptools import setup
setup(
    name='cli-anything-zero',
    version='1.0.0',
    packages=['cli_anything.zero'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-zero=cli_anything.zero:cli']},
)
