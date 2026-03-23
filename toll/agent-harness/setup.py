from setuptools import setup
setup(
    name='cli-anything-toll',
    version='1.0.0',
    packages=['cli_anything.toll'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-toll=cli_anything.toll:cli']},
)
