from setuptools import setup
setup(
    name='cli-anything-bagel',
    version='1.0.0',
    packages=['cli_anything.bagel'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bagel=cli_anything.bagel:cli']},
)
