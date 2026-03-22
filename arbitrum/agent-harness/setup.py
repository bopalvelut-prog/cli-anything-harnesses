from setuptools import setup
setup(
    name='cli-anything-arbitrum',
    version='1.0.0',
    packages=['cli_anything.arbitrum'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-arbitrum=cli_anything.arbitrum:cli']},
)
