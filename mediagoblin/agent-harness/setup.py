from setuptools import setup
setup(
    name='cli-anything-mediagoblin',
    version='1.0.0',
    packages=['cli_anything.mediagoblin'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mediagoblin=cli_anything.mediagoblin:cli']},
)
