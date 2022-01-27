from paddlenlp import Taskflow

if __name__ == "__main__":
    seg = Taskflow("word_segmentation")
    res = seg("第十四届全运会在西安举办")
    print(res)


