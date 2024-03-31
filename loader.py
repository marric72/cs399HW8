"""
    Load / normalize / shortens model data (google's model requires gensim)
    Does NOT load the model into memory, just pre-processes the data, line by line
    Author: Wolf Paulus, https://wolfpaulus.com
"""


def pre_process_data(in_file: str, out_file: str,
                     features: int = 300,
                     normalize: bool = True,
                     skip_1st: bool = True,
                     lines: int = 0) -> None:
    """
    Pre-process word vectors
    :param in_file: input file
    :param out_file: output file
    :param features: number of features defaults to 300
    :param normalize: normalize vectors defaults to True
    :param skip_1st: skip first line defaults to False
    :param lines: number of lines to process 0 for all
    :return: None
    """
    print(f"in_file={in_file}")
    print(f"out_file={out_file}")
    print(f"features={features}")
    print(f"normalize={normalize}")
    print(f"skip_1st={skip_1st}")
    print(f"lines={lines}")
    count=0
    line=" "
    with open(in_file, 'r') as f:
        max_len=0
        if skip_1st:
            line=f.readline()
        while (count < lines) or ((lines == 0) and line != ""):    
                    line=f.readline()
                    z=line.split(' ')
                    if len(z) > 0:
                        print("word is: ", z[0])
                    if max_len == 0:
                        max_len=len(z)
                        print(f"length of vector: {len(z)}")
                    else:
                        if (line != "") and (len(z) != max_len):
                            print("line=", line)
                            x=input("you need to normalize vector")
                            x=input("I know the L1 and L2 formulas")
                            x=input("but do not understand how those make vectors the same lengths so you can use dot product")
        f.close()           #TO-DO -figure this part out
        line=" "
        f=open(in_file, 'r')
        if skip_1st:
            line=f.readline()
            print(f"Skipping line: {line}")
            with open(out_file, 'w') as f2:
                line="   "
                #keep reading while you are less than requested lines
                #of if they requested all lines, stop at end of the file
                while (count < lines) or ((lines == 0) and line != ""):
                    line=f.readline()
                    f2.write(line)
                    count = count + 1

                
                    

            f2.close()
    f.close()
pre_process_data("short.txt", "outfile.txt", 2, True, True)
