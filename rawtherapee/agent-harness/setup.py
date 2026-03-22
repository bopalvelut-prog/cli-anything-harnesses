from setuptools import setup
setup(
    name='cli-anything-rawtherapee',
    version='1.0.0',
    packages=['cli_anything.rawtherapee'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rawtherapee=cli_anything.rawtherapee:cli']},
)
