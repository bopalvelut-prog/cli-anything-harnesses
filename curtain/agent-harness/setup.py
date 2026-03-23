from setuptools import setup
setup(
    name='cli-anything-curtain',
    version='1.0.0',
    packages=['cli_anything.curtain'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-curtain=cli_anything.curtain:cli']},
)
