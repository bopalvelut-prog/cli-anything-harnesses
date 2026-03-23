from setuptools import setup
setup(
    name='cli-anything-martini',
    version='1.0.0',
    packages=['cli_anything.martini'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-martini=cli_anything.martini:cli']},
)
