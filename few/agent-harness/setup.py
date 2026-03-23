from setuptools import setup
setup(
    name='cli-anything-few',
    version='1.0.0',
    packages=['cli_anything.few'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-few=cli_anything.few:cli']},
)
