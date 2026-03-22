from setuptools import setup
setup(
    name='cli-anything-lemmy',
    version='1.0.0',
    packages=['cli_anything.lemmy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-lemmy=cli_anything.lemmy:cli']},
)
