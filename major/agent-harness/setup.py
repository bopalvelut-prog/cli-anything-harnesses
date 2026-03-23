from setuptools import setup
setup(
    name='cli-anything-major',
    version='1.0.0',
    packages=['cli_anything.major'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-major=cli_anything.major:cli']},
)
