from setuptools import setup
setup(
    name='cli-anything-thunder',
    version='1.0.0',
    packages=['cli_anything.thunder'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-thunder=cli_anything.thunder:cli']},
)
