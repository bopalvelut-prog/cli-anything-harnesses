from setuptools import setup
setup(
    name='cli-anything-pop',
    version='1.0.0',
    packages=['cli_anything.pop'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pop=cli_anything.pop:cli']},
)
