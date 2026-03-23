from setuptools import setup
setup(
    name='cli-anything-auspice',
    version='1.0.0',
    packages=['cli_anything.auspice'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-auspice=cli_anything.auspice:cli']},
)
