from setuptools import setup
setup(
    name='cli-anything-eclair',
    version='1.0.0',
    packages=['cli_anything.eclair'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-eclair=cli_anything.eclair:cli']},
)
