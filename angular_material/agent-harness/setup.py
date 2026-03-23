from setuptools import setup
setup(
    name='cli-anything-angular_material',
    version='1.0.0',
    packages=['cli_anything.angular_material'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-angular_material=cli_anything.angular_material:cli']},
)
