from setuptools import setup
setup(
    name='cli-anything-grade',
    version='1.0.0',
    packages=['cli_anything.grade'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-grade=cli_anything.grade:cli']},
)
