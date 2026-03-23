from setuptools import setup
setup(
    name='cli-anything-song',
    version='1.0.0',
    packages=['cli_anything.song'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-song=cli_anything.song:cli']},
)
