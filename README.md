# pylearn_spark
Learning Pyspark.

## How to set up spark locally
Your system should have java and scala already installed. 
`$ java -version`

`$ scala -version` 
# spark_basics
Learning the basics of pySpark

## How to set up spark locally
Your system should have java and scala already installed. 
`$ java -version`

`$ scala -version` 

Should return the version values.

* Download Spark from [here](https://spark.apache.org/downloads.html) 
* Extarct the tar `tar xvf spark-<whatever version you use>.tgz`
* Move to usr/local `sudo mv spark-<version> /usr/local/spark`
* Add path in .bashrc `export PATH = $PATH:/usr/local/spark/bin`
* source .bashrc
* TO verfiy the setup run `$spark-shell`. if spark is installed successfully then you will see the scala prompt

To run simple pySpark commands check [here](http://spark.apache.org/docs/latest/quick-start.html)

Should return the version values.

* Download Spark from [here](https://spark.apache.org/downloads.html) 
* Extarct the tar `tar xvf spark-<whatever version you use>.tgz`
* Move to usr/local `sudo mv spark-<version> /usr/local/spark`
* Add path in .bashrc `export PATH = $PATH:/usr/local/spark/bin`
* source .bashrc
* TO verfiy the setup run `$spark-shell`. if spark is installed successfully then you will see the scala prompt

To run simple pySpark commands check [here](http://spark.apache.org/docs/latest/quick-start.html)

## To run our spark-sumbit job

NOTE: Make sure to set the input path properly in the WordCount.py file
NOTE: Make sure to call the WordCount.py from correct path

* `cd /usr/local/spark`
* `bin/spark-submit ~/spark_basics/WordCount.py`

## To increase the size of java-heap
* `cd /usr/local/spark`
* open the conf/spark-defaults.conf file
* Add this line `spark.driver.memory <memory value e.g 15g>`
