from setuptools import setup
setup(
    name='cli-anything-everyone',
    version='1.0.0',
    packages=['cli_anything.everyone'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-everyone=cli_anything.everyone:cli']},
)
