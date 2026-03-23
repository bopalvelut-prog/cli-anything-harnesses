from setuptools import setup
setup(
    name='cli-anything-external',
    version='1.0.0',
    packages=['cli_anything.external'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-external=cli_anything.external:cli']},
)
