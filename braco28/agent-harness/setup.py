from setuptools import setup
setup(
    name='cli-anything-braco28',
    version='1.0.0',
    packages=['cli_anything.braco28'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-braco28=cli_anything.braco28:cli']},
)
