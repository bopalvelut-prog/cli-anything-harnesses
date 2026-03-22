from setuptools import setup
setup(
    name='cli-anything-strapi',
    version='1.0.0',
    packages=['cli_anything.strapi'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-strapi=cli_anything.strapi:cli']},
)
