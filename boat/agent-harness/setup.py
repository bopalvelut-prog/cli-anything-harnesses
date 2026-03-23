from setuptools import setup
setup(
    name='cli-anything-boat',
    version='1.0.0',
    packages=['cli_anything.boat'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-boat=cli_anything.boat:cli']},
)
