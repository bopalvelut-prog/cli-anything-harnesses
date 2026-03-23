from setuptools import setup
setup(
    name='cli-anything-platform',
    version='1.0.0',
    packages=['cli_anything.platform'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-platform=cli_anything.platform:cli']},
)
