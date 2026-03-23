from setuptools import setup
setup(
    name='cli-anything-suddenly',
    version='1.0.0',
    packages=['cli_anything.suddenly'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-suddenly=cli_anything.suddenly:cli']},
)
