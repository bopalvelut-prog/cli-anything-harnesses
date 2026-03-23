from setuptools import setup
setup(
    name='cli-anything-headscale',
    version='1.0.0',
    packages=['cli_anything.headscale'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-headscale=cli_anything.headscale:cli']},
)
