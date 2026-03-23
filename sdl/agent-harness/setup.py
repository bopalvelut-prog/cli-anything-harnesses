from setuptools import setup
setup(
    name='cli-anything-sdl',
    version='1.0.0',
    packages=['cli_anything.sdl'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sdl=cli_anything.sdl:cli']},
)
