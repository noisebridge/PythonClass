Model Training and Serialization
================================

I recommend installing dependent packages in a python virtual environment

	$ virturalenv sklearn
	$ source sklearn/bin/activate

Begin by install requist python dependencies

	$ pip install -r train/requirements.txt

This demo currently requires a pre-release installation of sklearn2pmml and scikit-learn

	$ pip install --upgrade git+https://github.com/scikit-learn/scikit-learn.git 
	$ pip install --upgrade git+https://github.com/jpmml/sklearn2pmml.git

Once the dependencies are satified, wget the MNIST data

	$ ./get_data.sh
