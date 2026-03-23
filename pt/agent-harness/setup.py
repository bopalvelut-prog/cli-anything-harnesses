from setuptools import setup
setup(
    name='cli-anything-pt',
    version='1.0.0',
    packages=['cli_anything.pt'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pt=cli_anything.pt:cli']},
)
