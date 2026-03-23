from setuptools import setup
setup(
    name='cli-anything-prism',
    version='1.0.0',
    packages=['cli_anything.prism'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-prism=cli_anything.prism:cli']},
)
