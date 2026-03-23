from setuptools import setup
setup(
    name='cli-anything-puppetboard',
    version='1.0.0',
    packages=['cli_anything.puppetboard'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-puppetboard=cli_anything.puppetboard:cli']},
)
