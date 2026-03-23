from setuptools import setup
setup(
    name='cli-anything-google_translate',
    version='1.0.0',
    packages=['cli_anything.google_translate'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-google_translate=cli_anything.google_translate:cli']},
)
