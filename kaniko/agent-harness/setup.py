from setuptools import setup
setup(
    name='cli-anything-kaniko',
    version='1.0.0',
    packages=['cli_anything.kaniko'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kaniko=cli_anything.kaniko:cli']},
)
