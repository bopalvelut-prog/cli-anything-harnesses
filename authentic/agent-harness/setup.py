from setuptools import setup
setup(
    name='cli-anything-authentic',
    version='1.0.0',
    packages=['cli_anything.authentic'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-authentic=cli_anything.authentic:cli']},
)
