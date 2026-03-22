from setuptools import setup
setup(
    name='cli-anything-brevo',
    version='1.0.0',
    packages=['cli_anything.brevo'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-brevo=cli_anything.brevo:cli']},
)
