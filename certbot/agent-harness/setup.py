from setuptools import setup
setup(
    name='cli-anything-certbot',
    version='1.0.0',
    packages=['cli_anything.certbot'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-certbot=cli_anything.certbot:cli']},
)
