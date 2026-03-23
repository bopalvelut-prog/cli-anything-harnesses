from setuptools import setup
setup(
    name='cli-anything-automq',
    version='1.0.0',
    packages=['cli_anything.automq'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-automq=cli_anything.automq:cli']},
)
