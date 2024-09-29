from setuptools import setup, Extension
import platform
import sys
import os

# Determine the appropriate compiler flags based on the platform
extra_compile_args = ['-O3']  # Optimize for speed using -O3

# Add architecture-specific optimizations
machine = platform.machine().lower()

if machine in ('x86_64', 'amd64', 'i386', 'i686'):
    extra_compile_args.append('-msse2')  # Use SSE2 for x86 architectures
elif 'ppc' in machine or 'powerpc' in machine:
    extra_compile_args.extend(['-mvsx', '-mcpu=power8'])  # Use VSX for PowerPC architectures

# For macOS, specify the minimum deployment target
if sys.platform == 'darwin':
    extra_compile_args.append('-mmacosx-version-min=10.9')

# Define the C extension module
base64c_module = Extension(
    'base64c.base64c',  # This ensures the .so file is placed in the base64c directory
    sources=[os.path.join('base64c', 'base64c.c')],  # Path to the C source file
    extra_compile_args=extra_compile_args
)

# Read the README file for the long description
with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

# Setup configuration
setup(
    name='base64c',
    version='0.0.5',
    description='Fast Base64 encoding/decoding with SSE2 and VSX optimizations',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Oscar Bahamonde',
    author_email="oscar.bahamonde@indiecloud.co",
    url='https://github.com/obahamonde/base64c',
    ext_modules=[base64c_module],
    packages=['base64c'],
    package_dir={'base64c': 'src/base64c'},  # Specify the directory for Python package
    include_package_data=True,
    options={'bdist_wheel': {'universal': True}},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: C',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
    python_requires='>=3.8',
    extras_require={
        'dev': ['pytest', 'pyright', 'isort', 'black'],
    }
)