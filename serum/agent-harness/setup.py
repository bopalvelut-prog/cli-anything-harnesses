from setuptools import setup
setup(
    name='cli-anything-serum',
    version='1.0.0',
    packages=['cli_anything.serum'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-serum=cli_anything.serum:cli']},
)
