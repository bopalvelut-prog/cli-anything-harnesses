from setuptools import setup
setup(
    name='cli-anything-flight',
    version='1.0.0',
    packages=['cli_anything.flight'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-flight=cli_anything.flight:cli']},
)
