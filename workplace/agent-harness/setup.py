from setuptools import setup
setup(
    name='cli-anything-workplace',
    version='1.0.0',
    packages=['cli_anything.workplace'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-workplace=cli_anything.workplace:cli']},
)
