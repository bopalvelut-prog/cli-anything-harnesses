from setuptools import setup
setup(
    name='cli-anything-veteran',
    version='1.0.0',
    packages=['cli_anything.veteran'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-veteran=cli_anything.veteran:cli']},
)
