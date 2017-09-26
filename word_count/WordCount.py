from pyspark import SparkContext

text_file = "/home/smasud/spark-application/input.txt"
sc = SparkContext("local", "Word Count")
text_data = sc.textFile(text_file).cache()

words = text_data.flatMap(lambda line: line.split())
count_each_word = words.map(lambda word: (word, 1))
word_counts = count_each_word.reduceByKey(lambda a, b: a+b)

print(word_counts.collect())

sc.stop()
