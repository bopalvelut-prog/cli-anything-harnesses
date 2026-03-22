from setuptools import setup
setup(
    name='cli-anything-drupal',
    version='1.0.0',
    packages=['cli_anything.drupal'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-drupal=cli_anything.drupal:cli']},
)
