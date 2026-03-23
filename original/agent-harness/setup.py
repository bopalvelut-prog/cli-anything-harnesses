from setuptools import setup
setup(
    name='cli-anything-original',
    version='1.0.0',
    packages=['cli_anything.original'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-original=cli_anything.original:cli']},
)
