class Logic:
    def readingxml():
        with open('urls.xml','r') as file:
            for lines in file:
                print(lines.strip())
                
a = Logic
a.readingxml()