from setuptools import setup
setup(
    name='cli-anything-victory',
    version='1.0.0',
    packages=['cli_anything.victory'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-victory=cli_anything.victory:cli']},
)
