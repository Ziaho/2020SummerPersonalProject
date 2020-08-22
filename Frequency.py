from split import splitArticles
import make_matrix_voca

list_title = splitArticles('title', '\n') # Get title that '\n' has been removed to compare frequency
list_contents = splitArticles('contents', '\n') # Get contents that '\n' has been removed to compare frequency

f = open("matrix.txt", 'r', encoding='utf-8')
list_matrix = [] # 'empty matrix list' for make full matrix list
matrix = f.read()
for i in range(0, make_matrix_voca.row):
    temp1 = list(matrix.split('\n')) # Split by matrix row
    temp2 = list(temp1[i].split(',')) # Split by matrix column
    list_matrix.append(temp2)
f.close()

g = open("voca.txt", 'r', encoding='utf-8')
list_voca = g.read()
list_voca = list_voca.split('\n')
g.close()

# Function for getting titles of an articles in which a particular word appears most frequently
def get_FrequencyTitle(word):
    try:
        index = list_voca.index(word) # Return particular word's index
    except:
        print(word + "is not in vocabulary")
    frequency = [] # 'empty list' for make list which a particular word appears most frequently
    global list_matrix
    for i in range(0, make_matrix_voca.row): # Generate a two-dimensional list with an [index, frequency] list as an element
        temp = [i, (int(list_matrix[i][index]))] # temp = [index, frequency]
        frequency.append(temp)
    frequency = sorted(frequency, key = lambda x: x[1], reverse=True) # Sort frequency in descending order
    frequency = frequency[0:20] # In order to use only the top 20 articles
    indices = [i[0] for i in frequency] # Index is expressed in frequency[0] -> i[0] for i in frequency
    rank_title = [] # To make a list of the titles of articles
    for i in indices:
        rank_title.append(list_title[i])
    return rank_title # Return list of titles for 20 articles with particular word appears most frequently

# Function for getting words of an articles in which a particular word appears most frequently
def get_FrequencyWord(index):
    frequency = [] # 'empty list' for make list which includes word appears most frequently
    for i in range(0, make_matrix_voca.col): # Generate a two-dimensional list with an [index, frequency] list as an element
        temp = [i, (int(list_matrix[index][i]))] # temp = [index, frequency]
        frequency.append(temp)
    frequency = sorted(frequency, key = lambda x: x[1], reverse=True) # Sort frequency in descending order
    frequency = frequency[0:5] # In order to use only the top 5 words
    indices = [i[0] for i in frequency] # Index is expressed in frequency[0] -> i[0] for i in frequency
    rank_word = [] # To make a list of the words
    for i in indices:
        rank_word.append(list_voca[i])
    return rank_word # Return list of words that appear most frequently