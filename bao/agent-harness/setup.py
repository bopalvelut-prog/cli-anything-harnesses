from setuptools import setup
setup(
    name='cli-anything-bao',
    version='1.0.0',
    packages=['cli_anything.bao'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bao=cli_anything.bao:cli']},
)
