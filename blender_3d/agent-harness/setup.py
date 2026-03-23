from setuptools import setup
setup(
    name='cli-anything-blender_3d',
    version='1.0.0',
    packages=['cli_anything.blender_3d'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-blender_3d=cli_anything.blender_3d:cli']},
)
