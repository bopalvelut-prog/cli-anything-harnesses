from setuptools import setup
setup(
    name='cli-anything-shed',
    version='1.0.0',
    packages=['cli_anything.shed'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-shed=cli_anything.shed:cli']},
)
