from setuptools import setup
setup(
    name='cli-anything-cafe',
    version='1.0.0',
    packages=['cli_anything.cafe'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cafe=cli_anything.cafe:cli']},
)
