from setuptools import setup
setup(
    name='cli-anything-colony',
    version='1.0.0',
    packages=['cli_anything.colony'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-colony=cli_anything.colony:cli']},
)
