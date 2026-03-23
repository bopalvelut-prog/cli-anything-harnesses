from setuptools import setup
setup(
    name='cli-anything-nail',
    version='1.0.0',
    packages=['cli_anything.nail'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nail=cli_anything.nail:cli']},
)
