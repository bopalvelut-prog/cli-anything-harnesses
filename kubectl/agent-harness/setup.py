from setuptools import setup
setup(
    name='cli-anything-kubectl',
    version='1.0.0',
    packages=['cli_anything.kubectl'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kubectl=cli_anything.kubectl:cli']},
)
