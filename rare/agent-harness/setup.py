from setuptools import setup
setup(
    name='cli-anything-rare',
    version='1.0.0',
    packages=['cli_anything.rare'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rare=cli_anything.rare:cli']},
)
