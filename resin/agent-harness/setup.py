from setuptools import setup
setup(
    name='cli-anything-resin',
    version='1.0.0',
    packages=['cli_anything.resin'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-resin=cli_anything.resin:cli']},
)
