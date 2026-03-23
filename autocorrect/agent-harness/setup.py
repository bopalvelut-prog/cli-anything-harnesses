from setuptools import setup
setup(
    name='cli-anything-autocorrect',
    version='1.0.0',
    packages=['cli_anything.autocorrect'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-autocorrect=cli_anything.autocorrect:cli']},
)
