from setuptools import setup
setup(
    name='cli-anything-fulcio',
    version='1.0.0',
    packages=['cli_anything.fulcio'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-fulcio=cli_anything.fulcio:cli']},
)
