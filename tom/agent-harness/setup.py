from setuptools import setup
setup(
    name='cli-anything-tom',
    version='1.0.0',
    packages=['cli_anything.tom'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tom=cli_anything.tom:cli']},
)
