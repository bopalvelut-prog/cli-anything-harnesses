from setuptools import setup
setup(
    name='cli-anything-litellm',
    version='1.0.0',
    packages=['cli_anything.litellm'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-litellm=cli_anything.litellm:cli']},
)
