from setuptools import setup
setup(
    name='cli-anything-right',
    version='1.0.0',
    packages=['cli_anything.right'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-right=cli_anything.right:cli']},
)
