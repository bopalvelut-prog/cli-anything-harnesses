from setuptools import setup
setup(
    name='cli-anything-guide',
    version='1.0.0',
    packages=['cli_anything.guide'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-guide=cli_anything.guide:cli']},
)
