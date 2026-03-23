from setuptools import setup
setup(
    name='cli-anything-ultimately',
    version='1.0.0',
    packages=['cli_anything.ultimately'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ultimately=cli_anything.ultimately:cli']},
)
