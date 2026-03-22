from setuptools import setup
setup(
    name='cli-anything-iftop',
    version='1.0.0',
    packages=['cli_anything.iftop'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-iftop=cli_anything.iftop:cli']},
)
