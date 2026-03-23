from setuptools import setup
setup(
    name='cli-anything-adobe_sign',
    version='1.0.0',
    packages=['cli_anything.adobe_sign'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-adobe_sign=cli_anything.adobe_sign:cli']},
)
