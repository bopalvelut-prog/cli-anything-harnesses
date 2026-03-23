from setuptools import setup
setup(
    name='cli-anything-jose',
    version='1.0.0',
    packages=['cli_anything.jose'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-jose=cli_anything.jose:cli']},
)
