from setuptools import setup
setup(
    name='cli-anything-complex',
    version='1.0.0',
    packages=['cli_anything.complex'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-complex=cli_anything.complex:cli']},
)
