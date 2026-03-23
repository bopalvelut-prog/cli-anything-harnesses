from setuptools import setup
setup(
    name='cli-anything-reference',
    version='1.0.0',
    packages=['cli_anything.reference'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-reference=cli_anything.reference:cli']},
)
