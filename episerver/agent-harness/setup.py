from setuptools import setup
setup(
    name='cli-anything-episerver',
    version='1.0.0',
    packages=['cli_anything.episerver'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-episerver=cli_anything.episerver:cli']},
)
