import os

def main():
    i = 0
    for filename in os.listdir(os.getcwd() + '/table_images'):
        dst = str(i) + ".png"
        src = os.getcwd() + "/table_images/" + filename
        dst = os.getcwd() + "/table_images_rename/" + dst
        print(src,dst)
        os.rename(src,dst)
        i = i+1
    
if __name__ == '__main__':
    main()
