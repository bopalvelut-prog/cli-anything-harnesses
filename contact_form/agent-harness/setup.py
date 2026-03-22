from setuptools import setup
setup(
    name='cli-anything-contact_form',
    version='1.0.0',
    packages=['cli_anything.contact_form'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-contact_form=cli_anything.contact_form:cli']},
)
