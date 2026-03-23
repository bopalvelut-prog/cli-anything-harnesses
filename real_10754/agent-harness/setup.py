from setuptools import setup
setup(
    name='cli-anything-real_10754',
    version='1.0.0',
    packages=['cli_anything.real_10754'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-real_10754=cli_anything.real_10754:cli']},
)
