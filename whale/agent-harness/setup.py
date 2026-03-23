from setuptools import setup
setup(
    name='cli-anything-whale',
    version='1.0.0',
    packages=['cli_anything.whale'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-whale=cli_anything.whale:cli']},
)
