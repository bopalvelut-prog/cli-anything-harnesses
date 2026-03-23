from setuptools import setup
setup(
    name='cli-anything-supporter',
    version='1.0.0',
    packages=['cli_anything.supporter'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-supporter=cli_anything.supporter:cli']},
)
