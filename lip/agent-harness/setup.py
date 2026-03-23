from setuptools import setup
setup(
    name='cli-anything-lip',
    version='1.0.0',
    packages=['cli_anything.lip'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-lip=cli_anything.lip:cli']},
)
