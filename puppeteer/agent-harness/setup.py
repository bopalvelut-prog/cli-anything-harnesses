from setuptools import setup
setup(
    name='cli-anything-puppeteer',
    version='1.0.0',
    packages=['cli_anything.puppeteer'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-puppeteer=cli_anything.puppeteer:cli']},
)
