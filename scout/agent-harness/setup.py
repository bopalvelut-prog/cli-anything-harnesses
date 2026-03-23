from setuptools import setup
setup(
    name='cli-anything-scout',
    version='1.0.0',
    packages=['cli_anything.scout'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-scout=cli_anything.scout:cli']},
)
