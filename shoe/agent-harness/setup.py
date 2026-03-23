from setuptools import setup
setup(
    name='cli-anything-shoe',
    version='1.0.0',
    packages=['cli_anything.shoe'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-shoe=cli_anything.shoe:cli']},
)
