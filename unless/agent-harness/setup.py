from setuptools import setup
setup(
    name='cli-anything-unless',
    version='1.0.0',
    packages=['cli_anything.unless'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-unless=cli_anything.unless:cli']},
)
