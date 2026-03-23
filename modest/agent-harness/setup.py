from setuptools import setup
setup(
    name='cli-anything-modest',
    version='1.0.0',
    packages=['cli_anything.modest'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-modest=cli_anything.modest:cli']},
)
