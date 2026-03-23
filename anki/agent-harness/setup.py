from setuptools import setup
setup(
    name='cli-anything-anki',
    version='1.0.0',
    packages=['cli_anything.anki'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-anki=cli_anything.anki:cli']},
)
