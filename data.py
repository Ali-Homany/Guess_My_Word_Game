import os
from word import  Word_Manager

def learn_word(word: str) -> None:
    num_letters = len(word)
    dataset_folder = 'Dataset'
    file_names = os.listdir(dataset_folder)
    desired_file = None
    for file_name in file_names:
        if f"word_dataset_length_{len(word)}" in file_name:
            desired_file = file_name
            break
    with open(dataset_folder + "/" + desired_file, 'r') as readable_file:
        is_new_word = word not in readable_file.read()
    if is_new_word:
        with open(dataset_folder + "/" + desired_file, 'a') as file:
            file.write(word + '\n')
        size = int(desired_file.split('size_')[1].split('.')[0])
        new_name = dataset_folder + "/" + desired_file.replace(f"size_{size}", f"size_{size+1}")
        os.rename(dataset_folder + "/" + desired_file, new_name)
    

def filter_words(dataset: list[str], positions: list[int], letter: str) -> list[str]:
    word_length = len(dataset[0])
    pattern_list = Word_Manager.getPattern(letter=letter, positions=positions, word_length=word_length)
    filtered_dataset = [word for word in dataset if Word_Manager.isPattern(word=word, compiled_pattern=pattern_list)]
    return filtered_dataset


def read_dataset_for_length(num_letters: int) -> list[str]:
    dataset_folder = 'Dataset'
    file_names = os.listdir(dataset_folder)
    desired_file = None
    for file_name in file_names:
        if f"word_dataset_length_{num_letters}" in file_name:
            desired_file = file_name
            break
    with open(dataset_folder + "/" + desired_file, 'r') as file:
        words = file.readlines()
    return [word.strip() for word in words]