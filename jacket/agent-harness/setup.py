from setuptools import setup
setup(
    name='cli-anything-jacket',
    version='1.0.0',
    packages=['cli_anything.jacket'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-jacket=cli_anything.jacket:cli']},
)
