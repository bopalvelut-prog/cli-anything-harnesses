from setuptools import setup
setup(
    name='cli-anything-center',
    version='1.0.0',
    packages=['cli_anything.center'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-center=cli_anything.center:cli']},
)
