from setuptools import setup
setup(
    name='cli-anything-infrastructure',
    version='1.0.0',
    packages=['cli_anything.infrastructure'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-infrastructure=cli_anything.infrastructure:cli']},
)
