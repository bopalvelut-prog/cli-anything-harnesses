from setuptools import setup
setup(
    name='cli-anything-romantic',
    version='1.0.0',
    packages=['cli_anything.romantic'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-romantic=cli_anything.romantic:cli']},
)
