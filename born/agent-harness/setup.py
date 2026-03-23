from setuptools import setup
setup(
    name='cli-anything-born',
    version='1.0.0',
    packages=['cli_anything.born'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-born=cli_anything.born:cli']},
)
