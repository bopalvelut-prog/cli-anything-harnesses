from setuptools import setup
setup(
    name='cli-anything-pkg',
    version='1.0.0',
    packages=['cli_anything.pkg'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pkg=cli_anything.pkg:cli']},
)
