from setuptools import setup
setup(
    name='cli-anything-braco31',
    version='1.0.0',
    packages=['cli_anything.braco31'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-braco31=cli_anything.braco31:cli']},
)
