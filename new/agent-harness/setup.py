from setuptools import setup
setup(
    name='cli-anything-new',
    version='1.0.0',
    packages=['cli_anything.new'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-new=cli_anything.new:cli']},
)
