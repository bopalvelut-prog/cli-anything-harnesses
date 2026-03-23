from setuptools import setup
setup(
    name='cli-anything-reverse',
    version='1.0.0',
    packages=['cli_anything.reverse'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-reverse=cli_anything.reverse:cli']},
)
