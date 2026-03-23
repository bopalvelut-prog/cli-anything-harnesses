from setuptools import setup
setup(
    name='cli-anything-pagoda',
    version='1.0.0',
    packages=['cli_anything.pagoda'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pagoda=cli_anything.pagoda:cli']},
)
