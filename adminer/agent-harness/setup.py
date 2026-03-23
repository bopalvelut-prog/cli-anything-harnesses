from setuptools import setup
setup(
    name='cli-anything-adminer',
    version='1.0.0',
    packages=['cli_anything.adminer'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-adminer=cli_anything.adminer:cli']},
)
