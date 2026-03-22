from setuptools import setup
setup(
    name='cli-anything-rails',
    version='1.0.0',
    packages=['cli_anything.rails'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rails=cli_anything.rails:cli']},
)
