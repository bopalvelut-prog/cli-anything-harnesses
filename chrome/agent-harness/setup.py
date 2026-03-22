from setuptools import setup
setup(
    name='cli-anything-chrome',
    version='1.0.0',
    packages=['cli_anything.chrome'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-chrome=cli_anything.chrome:cli']},
)
