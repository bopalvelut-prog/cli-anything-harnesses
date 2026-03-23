from setuptools import setup
setup(
    name='cli-anything-export',
    version='1.0.0',
    packages=['cli_anything.export'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-export=cli_anything.export:cli']},
)
