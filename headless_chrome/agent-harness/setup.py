from setuptools import setup
setup(
    name='cli-anything-headless_chrome',
    version='1.0.0',
    packages=['cli_anything.headless_chrome'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-headless_chrome=cli_anything.headless_chrome:cli']},
)
