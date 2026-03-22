from setuptools import setup
setup(
    name='cli-anything-scala',
    version='1.0.0',
    packages=['cli_anything.scala'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-scala=cli_anything.scala:cli']},
)
