from setuptools import setup
setup(
    name='cli-anything-braco',
    version='1.0.0',
    packages=['cli_anything.braco'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-braco=cli_anything.braco:cli']},
)
