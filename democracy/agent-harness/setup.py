from setuptools import setup
setup(
    name='cli-anything-democracy',
    version='1.0.0',
    packages=['cli_anything.democracy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-democracy=cli_anything.democracy:cli']},
)
