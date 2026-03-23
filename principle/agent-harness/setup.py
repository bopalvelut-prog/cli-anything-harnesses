from setuptools import setup
setup(
    name='cli-anything-principle',
    version='1.0.0',
    packages=['cli_anything.principle'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-principle=cli_anything.principle:cli']},
)
