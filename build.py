import os
import sys
from setuptools import Extension, setup
from setuptools.dist import Distribution
from setuptools.command.build_ext import build_ext

class BuildExt(build_ext):
    def run(self):
        build_ext.run(self)

def build(setup_kwargs):
    print("Starting build process...")
    
    # Define the C extension module
    base64c_module = Extension(
        'base64c.base64c',
        sources=[os.path.join('base64c', 'base64c.c')],
        extra_compile_args=['-O3', '-msse2'] if sys.platform != "darwin" else ['-O3']
    )

    # Create a distribution with our extension module
    dist = Distribution({'name': 'base64c', 'ext_modules': [base64c_module]})
    
    # Ensure the build_ext command is available
    dist.cmdclass['build_ext'] = BuildExt

    # Build the extension
    cmd = BuildExt(dist)
    cmd.ensure_finalized()
    cmd.run()

    # Specify the correct directory for the built extension
    build_dir = os.path.abspath(cmd.build_lib)
    
    print(f"Extension built in: {build_dir}")
    print(f"Files in build directory: {os.listdir(build_dir)}")

    # Update setup_kwargs
    setup_kwargs.update({
        'ext_modules': [base64c_module],
        'cmdclass': {'build_ext': BuildExt},
        'package_data': {'base64c': ['*.so', '*.pyd']},
        'include_package_data': True,
    })

    print("Build process completed.")

if __name__ == "__main__":
    setup(
        name='base64c',
        version='0.0.5',
        packages=['base64c'],
        package_dir={'base64c': 'src/base64c'},
        ext_modules=[Extension('base64c.base64c', sources=[os.path.join('base64c', 'base64c.c')])],
        cmdclass={'build_ext': BuildExt},
    )
    print("Setup completed when run directly.")