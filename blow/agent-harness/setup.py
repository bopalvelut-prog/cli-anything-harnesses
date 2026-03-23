from setuptools import setup
setup(
    name='cli-anything-blow',
    version='1.0.0',
    packages=['cli_anything.blow'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-blow=cli_anything.blow:cli']},
)
