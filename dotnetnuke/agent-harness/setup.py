from setuptools import setup
setup(
    name='cli-anything-dotnetnuke',
    version='1.0.0',
    packages=['cli_anything.dotnetnuke'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dotnetnuke=cli_anything.dotnetnuke:cli']},
)
