from setuptools import setup
setup(
    name='cli-anything-glad',
    version='1.0.0',
    packages=['cli_anything.glad'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-glad=cli_anything.glad:cli']},
)
