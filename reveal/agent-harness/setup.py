from setuptools import setup
setup(
    name='cli-anything-reveal',
    version='1.0.0',
    packages=['cli_anything.reveal'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-reveal=cli_anything.reveal:cli']},
)
