# -*- coding: utf-8 -*-

"""
    script to extract and structure data obtained from an SVG file JSON.
"""
__author__ = "Giovanni Cadiz Brombley"
__version__ = "1.1"
__date__ = "2017-10-12"
__email__ = "giovannicadiz@gmail.com"
__status__ = "Production"


def array():
    try:
        while True:

            # Enter the name file
            fHand = input("Enter the file or Press Enter to exit - ")
            split = fHand.split('.')
            split = split[0].strip()
            nameOut = (split+'_out'+'.json')
            if len(fHand) < 1:
                break

            else:
                file = open(fHand)
                words = '"m '
                wordsM = '"M '
                wordsM8 = '"M8 '
                arr = []
                count = 0
                json = []
                com = '"'

                # Enter the name PREF
                pref = input("Enter the PREF (example 'flc') - ").lower()
                if len(pref) < 1:
                    pref = 'Null'

                else:
                    pref = pref

                # Enter the name path_style
                path_style = input("Enter the path_style (example 'f2f2f2') - ").lower()
                if len(path_style) < 1:
                    path_style = 'Null'
                else:
                    path_style = '$' + path_style

                for i in file:
                    i = i.strip()
                    if (words in i) or (wordsM in i) or (wordsM8 in i):
                        count += 1
                        arr.append(
                            {"data_id": pref + str(count), "seat_path": str(i[3:-1]), "path_style:": path_style})

                # show to screen
                for n in arr:
                    n = str(n).replace("'", com)
                    print(n)
                print("\n########################################################################")
                print("TOTAL seat_path : ", count)
                print("Output File     : ",nameOut)
                print("########################################################################\n")

                # save in file
                json.append(arr)
                for x in json:
                    x = str(x).replace("'", com)
                    saveFile = open(nameOut, 'a')
                    saveFile.write(str(x))
                    saveFile.close()

    except Exception as e:
        print("\nFailed !!!!!!! ","\n", str(e))


if __name__ == '__main__':

    array()

