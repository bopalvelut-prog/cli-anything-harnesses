from setuptools import setup
setup(
    name='cli-anything-jack',
    version='1.0.0',
    packages=['cli_anything.jack'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-jack=cli_anything.jack:cli']},
)
