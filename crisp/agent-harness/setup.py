from setuptools import setup
setup(
    name='cli-anything-crisp',
    version='1.0.0',
    packages=['cli_anything.crisp'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-crisp=cli_anything.crisp:cli']},
)
