from setuptools import setup
setup(
    name='cli-anything-embrace',
    version='1.0.0',
    packages=['cli_anything.embrace'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-embrace=cli_anything.embrace:cli']},
)
