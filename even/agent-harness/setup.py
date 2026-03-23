from setuptools import setup
setup(
    name='cli-anything-even',
    version='1.0.0',
    packages=['cli_anything.even'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-even=cli_anything.even:cli']},
)
