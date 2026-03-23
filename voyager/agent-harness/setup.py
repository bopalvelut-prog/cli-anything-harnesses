from setuptools import setup
setup(
    name='cli-anything-voyager',
    version='1.0.0',
    packages=['cli_anything.voyager'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-voyager=cli_anything.voyager:cli']},
)
