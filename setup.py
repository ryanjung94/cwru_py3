from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='cwru_py3',
      version='0.1',
      description='Case Western Reserve University Bearing Data',
      long_description=readme(),
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Topic :: Scientific/Engineering :: Information Analysis',
      ],
      keywords='cwru bearing fault diagnosis dataset via python3',
      url='https://github.com/94JuHo/cwru_py3',
      author='Juho Jung',
      author_email='jjs1005k@gmail.com',
      license='MIT',
      packages=['cwru_py3'],
      install_requires=[
          'numpy',
          'scipy',
      ],
      include_package_data=True,
      test_suite='tests',
      zip_safe=False)
