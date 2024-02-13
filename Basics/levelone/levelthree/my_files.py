def main():
    
    #TODO: write file
    # file = open("lco.txt", "a+")
    # for i in range(20):
    #     file.write("This is python code %d \n" %(i))
    # file.close
    
    #TODO: read file
    # file = open("lco.txt", "r")
    # if file.mode == 'r':
    #     filecontent = file.read()
    #     print(filecontent)
    
    #TODO: exception
    
    try: 
        myfile = open("lco.txt", "r")
        print("success in reading")
        
    except IOError:
        print("File does not exist")
        
    print("Task done")
    
if __name__ == "__main__":
    main()