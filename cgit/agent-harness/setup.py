from setuptools import setup
setup(
    name='cli-anything-cgit',
    version='1.0.0',
    packages=['cli_anything.cgit'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cgit=cli_anything.cgit:cli']},
)
