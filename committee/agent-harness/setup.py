from setuptools import setup
setup(
    name='cli-anything-committee',
    version='1.0.0',
    packages=['cli_anything.committee'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-committee=cli_anything.committee:cli']},
)
