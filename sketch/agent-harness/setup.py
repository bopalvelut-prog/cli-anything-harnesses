from setuptools import setup
setup(
    name='cli-anything-sketch',
    version='1.0.0',
    packages=['cli_anything.sketch'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sketch=cli_anything.sketch:cli']},
)
