from setuptools import setup
setup(
    name='cli-anything-chief',
    version='1.0.0',
    packages=['cli_anything.chief'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-chief=cli_anything.chief:cli']},
)
