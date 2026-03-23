from setuptools import setup
setup(
    name='cli-anything-president',
    version='1.0.0',
    packages=['cli_anything.president'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-president=cli_anything.president:cli']},
)
