from setuptools import setup
setup(
    name='cli-anything-attention',
    version='1.0.0',
    packages=['cli_anything.attention'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-attention=cli_anything.attention:cli']},
)
