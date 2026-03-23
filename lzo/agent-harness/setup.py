from setuptools import setup
setup(
    name='cli-anything-lzo',
    version='1.0.0',
    packages=['cli_anything.lzo'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-lzo=cli_anything.lzo:cli']},
)
