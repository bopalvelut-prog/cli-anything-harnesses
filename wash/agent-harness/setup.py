from setuptools import setup
setup(
    name='cli-anything-wash',
    version='1.0.0',
    packages=['cli_anything.wash'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wash=cli_anything.wash:cli']},
)
