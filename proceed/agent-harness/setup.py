from setuptools import setup
setup(
    name='cli-anything-proceed',
    version='1.0.0',
    packages=['cli_anything.proceed'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-proceed=cli_anything.proceed:cli']},
)
