from setuptools import setup
setup(
    name='cli-anything-autogen',
    version='1.0.0',
    packages=['cli_anything.autogen'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-autogen=cli_anything.autogen:cli']},
)
