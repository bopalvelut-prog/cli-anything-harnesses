from setuptools import setup
setup(
    name='cli-anything-universal',
    version='1.0.0',
    packages=['cli_anything.universal'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-universal=cli_anything.universal:cli']},
)
