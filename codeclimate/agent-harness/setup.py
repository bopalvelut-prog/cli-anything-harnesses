from setuptools import setup
setup(
    name='cli-anything-codeclimate',
    version='1.0.0',
    packages=['cli_anything.codeclimate'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-codeclimate=cli_anything.codeclimate:cli']},
)
