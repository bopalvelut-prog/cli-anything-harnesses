from setuptools import setup
setup(
    name='cli-anything-wish',
    version='1.0.0',
    packages=['cli_anything.wish'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wish=cli_anything.wish:cli']},
)
