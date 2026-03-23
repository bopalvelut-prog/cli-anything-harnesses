from setuptools import setup
setup(
    name='cli-anything-scholarship',
    version='1.0.0',
    packages=['cli_anything.scholarship'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-scholarship=cli_anything.scholarship:cli']},
)
