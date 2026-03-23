from setuptools import setup
setup(
    name='cli-anything-logback',
    version='1.0.0',
    packages=['cli_anything.logback'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-logback=cli_anything.logback:cli']},
)
