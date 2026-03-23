from setuptools import setup
setup(
    name='cli-anything-unfortunately',
    version='1.0.0',
    packages=['cli_anything.unfortunately'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-unfortunately=cli_anything.unfortunately:cli']},
)
