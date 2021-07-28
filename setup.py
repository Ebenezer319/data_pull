from setuptools import setup
import pathlib



def readme():
    this_directory = pathlib.Path(__file__).parent.resolve()
    long_description = (this_directory / 'README.md').read_text(encoding='utf-8')
    
    return long_description


setup(name='data_pull',
      version='1.0.0',
      description='Data Extract',
      long_description=readme(),
      long_description_content_type = 'text/markdown',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'Topic :: CSV Extraction :: File Manipulation',
      ],
      url='https://github.com/Ebenezer319/data_pull',
      author='CSV Extractors',
      packages=['data_pull'],
      install_requires=[
          'numpy',
          'pandas'
      ],
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3'],
      entry_points={
          'console_scripts': ['data-pull=data_pull.data_pull:DataPull'],
      },
      include_package_data=True,
      zip_safe=False)
