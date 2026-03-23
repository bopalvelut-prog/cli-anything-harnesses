from setuptools import setup
setup(
    name='cli-anything-court',
    version='1.0.0',
    packages=['cli_anything.court'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-court=cli_anything.court:cli']},
)
