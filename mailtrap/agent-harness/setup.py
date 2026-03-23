from setuptools import setup
setup(
    name='cli-anything-mailtrap',
    version='1.0.0',
    packages=['cli_anything.mailtrap'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mailtrap=cli_anything.mailtrap:cli']},
)
