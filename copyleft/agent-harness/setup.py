from setuptools import setup
setup(
    name='cli-anything-copyleft',
    version='1.0.0',
    packages=['cli_anything.copyleft'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-copyleft=cli_anything.copyleft:cli']},
)
