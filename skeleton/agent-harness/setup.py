from setuptools import setup
setup(
    name='cli-anything-skeleton',
    version='1.0.0',
    packages=['cli_anything.skeleton'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-skeleton=cli_anything.skeleton:cli']},
)
