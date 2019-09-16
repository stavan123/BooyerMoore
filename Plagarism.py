import sys
import re
import os
dir = input ("Enter the directory")
text1 = input ("Enter the pattern file")
if os.path.isdir(dir) == 0:
    print("The directory does not exist")
    sys.exit(0)
for textfile in os.listdir(dir):
    if textfile[0] == "." :
        continue

    print("Checking ",textfile)

    text2 = open(os.path.join(dir,textfile)).read()
    pattern_file    = ''.join(open(text1).readlines())

    sentences = re.split(r'[\.\?!]', pattern_file)
    countermatched = 0
    countertotal = 0

    for pat in sentences:
        pat = pat.strip()

        if len(pat) > 0:
            countertotal += 1
            patternstartpos = 0
            found = 0

            while patternstartpos + len(pat) <= len(text2):

                j = patternstartpos + len(pat)

                for i in range(0, len(pat))[::-1]:


                    if pat[i].lower() == text2[j - 1].lower():
                        j = j - 1

                        if j == patternstartpos:
                            found = 1
                            break
                        else:
                            continue


                    else:


                        if pat[0:i].rfind(text2[j - 1]) == -1:
                            patternstartpos = patternstartpos + len(pat)
                            break


                        else:
                            patternstartpos = patternstartpos + len(pat) - pat[0:i].rfind(text2[j - 1]) - 1
                            break


                if found == 1:
                    countermatched = countermatched + 1
                    break

    print("Match percentage = %s%%" % (countermatched * 100 / countertotal))
    if (countermatched * 100 / countertotal) >= 70:
        print("The input file is appears to be plagiarised. %s%% of its content matches with the file %s." % (
        (countermatched * 100 / countertotal), textfile))


