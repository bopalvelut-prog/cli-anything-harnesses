from setuptools import setup
setup(
    name='cli-anything-bunch',
    version='1.0.0',
    packages=['cli_anything.bunch'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bunch=cli_anything.bunch:cli']},
)
