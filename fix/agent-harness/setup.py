from setuptools import setup
setup(
    name='cli-anything-fix',
    version='1.0.0',
    packages=['cli_anything.fix'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-fix=cli_anything.fix:cli']},
)
