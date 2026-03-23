from setuptools import setup
setup(
    name='cli-anything-assent',
    version='1.0.0',
    packages=['cli_anything.assent'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-assent=cli_anything.assent:cli']},
)
