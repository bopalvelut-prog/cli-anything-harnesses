from setuptools import setup
setup(
    name='cli-anything-artemis',
    version='1.0.0',
    packages=['cli_anything.artemis'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-artemis=cli_anything.artemis:cli']},
)
