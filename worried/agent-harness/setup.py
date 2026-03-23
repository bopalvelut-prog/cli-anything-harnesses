from setuptools import setup
setup(
    name='cli-anything-worried',
    version='1.0.0',
    packages=['cli_anything.worried'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-worried=cli_anything.worried:cli']},
)
