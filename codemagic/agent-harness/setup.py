from setuptools import setup
setup(
    name='cli-anything-codemagic',
    version='1.0.0',
    packages=['cli_anything.codemagic'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-codemagic=cli_anything.codemagic:cli']},
)
