from setuptools import setup
setup(
    name='cli-anything-fall',
    version='1.0.0',
    packages=['cli_anything.fall'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-fall=cli_anything.fall:cli']},
)
