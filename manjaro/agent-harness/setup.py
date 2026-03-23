from setuptools import setup
setup(
    name='cli-anything-manjaro',
    version='1.0.0',
    packages=['cli_anything.manjaro'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-manjaro=cli_anything.manjaro:cli']},
)
