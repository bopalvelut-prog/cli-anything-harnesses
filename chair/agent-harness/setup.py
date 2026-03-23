from setuptools import setup
setup(
    name='cli-anything-chair',
    version='1.0.0',
    packages=['cli_anything.chair'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-chair=cli_anything.chair:cli']},
)
