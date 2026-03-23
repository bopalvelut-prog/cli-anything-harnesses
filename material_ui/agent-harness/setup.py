from setuptools import setup
setup(
    name='cli-anything-material_ui',
    version='1.0.0',
    packages=['cli_anything.material_ui'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-material_ui=cli_anything.material_ui:cli']},
)
