from setuptools import setup
setup(
    name='cli-anything-fantasy',
    version='1.0.0',
    packages=['cli_anything.fantasy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-fantasy=cli_anything.fantasy:cli']},
)
