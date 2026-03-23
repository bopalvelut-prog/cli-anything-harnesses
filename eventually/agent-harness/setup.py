from setuptools import setup
setup(
    name='cli-anything-eventually',
    version='1.0.0',
    packages=['cli_anything.eventually'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-eventually=cli_anything.eventually:cli']},
)
