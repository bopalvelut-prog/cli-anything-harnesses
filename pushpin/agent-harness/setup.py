from setuptools import setup
setup(
    name='cli-anything-pushpin',
    version='1.0.0',
    packages=['cli_anything.pushpin'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pushpin=cli_anything.pushpin:cli']},
)
