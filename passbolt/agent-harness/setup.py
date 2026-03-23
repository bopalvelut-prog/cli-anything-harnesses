from setuptools import setup
setup(
    name='cli-anything-passbolt',
    version='1.0.0',
    packages=['cli_anything.passbolt'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-passbolt=cli_anything.passbolt:cli']},
)
