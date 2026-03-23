from setuptools import setup
setup(
    name='cli-anything-flesh',
    version='1.0.0',
    packages=['cli_anything.flesh'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-flesh=cli_anything.flesh:cli']},
)
