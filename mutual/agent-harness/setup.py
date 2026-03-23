from setuptools import setup
setup(
    name='cli-anything-mutual',
    version='1.0.0',
    packages=['cli_anything.mutual'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mutual=cli_anything.mutual:cli']},
)
