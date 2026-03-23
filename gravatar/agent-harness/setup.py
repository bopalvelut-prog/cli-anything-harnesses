from setuptools import setup
setup(
    name='cli-anything-gravatar',
    version='1.0.0',
    packages=['cli_anything.gravatar'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gravatar=cli_anything.gravatar:cli']},
)
