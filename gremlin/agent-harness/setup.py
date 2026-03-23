from setuptools import setup
setup(
    name='cli-anything-gremlin',
    version='1.0.0',
    packages=['cli_anything.gremlin'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gremlin=cli_anything.gremlin:cli']},
)
