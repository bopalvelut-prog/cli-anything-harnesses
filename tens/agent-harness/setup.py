from setuptools import setup
setup(
    name='cli-anything-tens',
    version='1.0.0',
    packages=['cli_anything.tens'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tens=cli_anything.tens:cli']},
)
