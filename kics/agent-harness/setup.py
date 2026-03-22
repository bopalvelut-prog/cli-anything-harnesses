from setuptools import setup
setup(
    name='cli-anything-kics',
    version='1.0.0',
    packages=['cli_anything.kics'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kics=cli_anything.kics:cli']},
)
