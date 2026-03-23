from setuptools import setup
setup(
    name='cli-anything-tall',
    version='1.0.0',
    packages=['cli_anything.tall'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tall=cli_anything.tall:cli']},
)
