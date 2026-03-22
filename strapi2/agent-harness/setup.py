from setuptools import setup
setup(
    name='cli-anything-strapi2',
    version='1.0.0',
    packages=['cli_anything.strapi2'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-strapi2=cli_anything.strapi2:cli']},
)
