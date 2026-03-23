from setuptools import setup
setup(
    name='cli-anything-teach',
    version='1.0.0',
    packages=['cli_anything.teach'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-teach=cli_anything.teach:cli']},
)
