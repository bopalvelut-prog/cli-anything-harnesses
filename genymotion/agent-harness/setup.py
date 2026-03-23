from setuptools import setup
setup(
    name='cli-anything-genymotion',
    version='1.0.0',
    packages=['cli_anything.genymotion'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-genymotion=cli_anything.genymotion:cli']},
)
