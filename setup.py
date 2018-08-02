from setuptools import setup

setup(name='zoldyck',
      version='1.0',
      description='is Universal Package for making Chatbots easy .this version 1.0, and it include only facebook messenger',
      url='https://github.com/AmienKhaled/zoldyck',
      author='Amien Khaled Amien',
      author_email='amin.khaled33@gmail.com',
      license='MIT',
      packages=['zoldyck'],
      install_requires=[
          'moviepy',
		  'SpeechRecognition',
		  'requests',
      ],
      python_requires='>=3',
	  include_package_data=True,
	  zip_safe=False)

