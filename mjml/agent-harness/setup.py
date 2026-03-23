from setuptools import setup
setup(
    name='cli-anything-mjml',
    version='1.0.0',
    packages=['cli_anything.mjml'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mjml=cli_anything.mjml:cli']},
)
