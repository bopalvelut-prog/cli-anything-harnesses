from setuptools import setup
setup(
    name='cli-anything-embassy',
    version='1.0.0',
    packages=['cli_anything.embassy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-embassy=cli_anything.embassy:cli']},
)
