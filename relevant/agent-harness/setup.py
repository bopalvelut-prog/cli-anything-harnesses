from setuptools import setup
setup(
    name='cli-anything-relevant',
    version='1.0.0',
    packages=['cli_anything.relevant'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-relevant=cli_anything.relevant:cli']},
)
