from setuptools import setup
setup(
    name='cli-anything-empire',
    version='1.0.0',
    packages=['cli_anything.empire'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-empire=cli_anything.empire:cli']},
)
