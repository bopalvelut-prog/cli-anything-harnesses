from setuptools import setup
setup(
    name='cli-anything-elder',
    version='1.0.0',
    packages=['cli_anything.elder'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-elder=cli_anything.elder:cli']},
)
