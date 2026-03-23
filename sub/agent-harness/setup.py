from setuptools import setup
setup(
    name='cli-anything-sub',
    version='1.0.0',
    packages=['cli_anything.sub'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sub=cli_anything.sub:cli']},
)
