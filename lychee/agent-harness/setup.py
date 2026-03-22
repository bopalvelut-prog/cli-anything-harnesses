from setuptools import setup
setup(
    name='cli-anything-lychee',
    version='1.0.0',
    packages=['cli_anything.lychee'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-lychee=cli_anything.lychee:cli']},
)
