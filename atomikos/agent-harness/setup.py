from setuptools import setup
setup(
    name='cli-anything-atomikos',
    version='1.0.0',
    packages=['cli_anything.atomikos'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-atomikos=cli_anything.atomikos:cli']},
)
