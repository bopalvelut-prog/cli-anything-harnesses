from setuptools import setup
setup(
    name='cli-anything-pdf',
    version='1.0.0',
    packages=['cli_anything.pdf'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pdf=cli_anything.pdf:cli']},
)
