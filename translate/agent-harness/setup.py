from setuptools import setup
setup(
    name='cli-anything-translate',
    version='1.0.0',
    packages=['cli_anything.translate'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-translate=cli_anything.translate:cli']},
)
