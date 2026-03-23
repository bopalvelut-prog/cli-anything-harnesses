from setuptools import setup
setup(
    name='cli-anything-outdoor',
    version='1.0.0',
    packages=['cli_anything.outdoor'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-outdoor=cli_anything.outdoor:cli']},
)
