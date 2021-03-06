import numpy as np
import pandas as pd
import re

# Import plain-text transcriptions
one = "ANOTHER DREADFUL MASSACRE BY THE NATIVES OF THE MARQUESAS ISLANDS. ( From the Sydney Gazette, Nov. 8, 1815.) By the Governor Macquarrie are arrived Captain Fowler, and part of the crew of the Indian brig Matilda, which sailed from this colony in August, 1813, bound on a voyage to the Derwent and Eastern Islands, and from thence to China; but was cut off and plundered on the night of the 10th of April last, while lying at anchor in Duff's Bay, at the Island of Rooapoah, one of the Marquesas, on a sandal wood voyage. Five of the crew (Poomootoo men) had previously deserted, and joining with some of the Rooapoah natives, took the opportunity of a dark night, and the wind blowing fresh right on the land, to cut the vessel adrift; by which means she drove ashore through a heavy surf, and was soon bilged and filled with water. When the cannibal natives saw that it was impracticable to get the vessel afloat, they concurred universally in the design of putting the whole of her crew to death, which appears to have been a constant practise among the different natives towards one another, when their canoes happen to fall upon a strange shore, through stress of weather, or from any other accident. Captain Fowler had formed an intimacy with their Chief, or King, Nooahetu, who presided at the horrible tribunal that had devoted the unfortunate mariners to instant slaughter. He withheld his assent to the murder; but had no hesitation in permitting the plunder of the vessel. The crew were informed by such expressions as they could understand, as well as by gesticulations that accompanied their vehement debate on the occasion, that their lives were dependent on the issue; the good chief was opposed by many other Chiefs, who, though somewhat inferior in rank, were very far superior in number, supported by the common usages of the island, from which the exhibition of clemency appeared an insufferable deviation. He was seated, with his son by his side, on a mat in his own dwelling; he had been called to the supremacy of the island by the general wish of the people, as it was not a hereditary right, but an elective dignity. His people pressed their solicitations earnestly, and at length peremptorily demanded his assent to the sacrifice; which he for a length of time opposed by the force of words, which not seeming likely to prevail, he adopted a method which silenced the whole in an instant, and saved the lives of Captain Fowler and his crew. Finding that all his expostulations were defeated upon the principle of undeviating custom, he deliberately took up two ropes that were near him, and fixing one round the neck of his son, and the other round his own, called to the Chief next in command, who immediately approached him. His conference was short and decisive; he first pointed to the cord that encircled the neck of his son, and then to the other which he had entwined around his own. \"These strangers are doomed to death,\" said he, \"by my chiefs and my people: and it is not fit that I, who am their King, should live to see so vile a deed perpetrated. Let my child and myself be strangled before it is performed and then it never will be said that we sanctioned, even with our eye-sight, the destruction of these unoffending people.\" The magnanimity of such a conduct could not do less than produce, even in the mind of the unenlightened savage, a paroxysm of surprise, mingled with a sentiment of admiration in which the untaught man may possibly excel his fellow creature, whose conceptions are moulded by tenets calculated to guard him from the extremes of passion. For a moment the people looked wildly upon their King, whose person they adored, because that his principles were good, and his government just and mild. They saw the obedient chief, to whom the order of strangulation had been imparted, staring with horror and amazement at the change which a few moments had produced; the mandate that had proceeded from the King's own lips must be obeyed: and commanded to perform the dreadful office, he proceeded to obey–when a sudden shout from the multitude awed him to forbearance. \"The King! the King!\" from every lip burst forth:–\"What! kill the King! No, no, let all the strangers live–no man shall kill the King!\"–Thus were their lives preserved and the vessel plundered of every thing on board her. The floor of the Greenwich, which was burnt at Nooaheva, still remains, and is dry at low water. All her iron and copper have been taken out by the natives, who have a thorough knowledge of the use of these materials. That they are cannibals is well ascertained. They form distinct factions, and make war upon the ruling Chief; the rebels are denominated the Typees; and the opposite parties are horribly sanguinary towards each. Six of the adverse party were killed, and devoured by the rebels while Captain Fowler was among them, and the following detestable circumstance occurred on the occasion:–A native man belonging to Port Anna Maria, who was not tattooed, and in consequence prohibited from the eating of human flesh, on pain of death, impatient of the restraint, fell upon one of the murdered bodies, and darting his teeth into it in all the madness of a voracious fury, exhaled the crimson moisture, which had not yet coagulated. The Chief of Port Anna Maria, who is very friendly to Europeans, is named Ke-atta-nooe, the first part of the name implying the outrigger of a canoe, and the latter signifying great. The dress, of the men consists merely of a wrapper about the waist; the women are covered from the shoulders downwards to the ancles, and are generally fairer than the Taheitan women. The Chiefs have no distinguishing mark or ornament, but in the mode of wearing their hair; which the common orders wear tied up in a large knot on each side of the head, a stripe of which, extending from the forehead to the hollow of the neck, is kept shorn, which practice the Chiefs do not adopt. Captain Fowler supposes the worms to be more prevalent and destructive to the ships' bottoms there, than he has anywhere else witnessed; and to this cause attributes the caution of the natives in drawing up their largest canoes, some of which contain from 80 to 100 warriors. They are anxious after every kind of property carried among them for barter, and this is supposed their chief inducement for attacking vessels when they can do so with a probability of accomplishing their object. They have no knowledge of the use of muskets, and have none among them except a few at Port Anna Maria. A gentleman, at this time in Sydney, who resided among them about 15 years ago in a missionary capacity, describes them as a people constantly employing their thoughts on plunder, and devising schemes for taking advantage of strangers. Their population is very numerous; which he remarked to some of them, to whom he gave a description of Otaheite, observing, at the same time, that its inhabitants were less numerous:–\"Cannot we go and take them? What is there to hinder us?\"–was immediately demanded. This anecdote we notice as a specimen of their natural inclination to hostility, in which, all accounts respecting them correspond."

two = "ANOTHER DREADFUL MASSACRE BY THE NATIVESOF THE MARQUESAS ISLANDS. (From the Sydney Gazette, Nov. 8. 1815) By the Governor Macquarrie, are arrived Captain Fowler, and part of the crew of the Indian brig Matilda, which sailed from this colony in August 1813, bound on a voyage to the Derwent and Eastern Islands, and from thence to China, but was cut off and plundered, on the night of the 10th of April last, while lying at anchor in Duff's Bay, at the Island of Rooapoah, one of the Marquesas, on a sandal-wood voyage. Five of the crew (Poomootoo men) had previously deserted, and joining with some of the Rooapoah natives, took the opportunity of a dark night, and the wind blowing fresh right on the land, to cut the vessel adrift, by which means she drove on shore through a heavy surf, and was soon bilged and filled with water. When the cannibal natives saw that it was impracticable to get the vessel afloat, they concurred universally in the design of putting the whole of her crew to death; which appears to have been a constant practise among the different natives towards one another, when their canoes happen to fall upon a strange shore, through stress of weather, or from any other accident. Captain Fowler had formed an intimacy with their chief, or king, Nooahetu, who presided at the horrible tribunal that had devoted the unfortunate mariners to instant slaughter. He withheld his assent to the murder; but had no hesitation in permitting the plunder of the vessel– The crew were informed by such expressions as they could understand, as well as by gesticulations that accompanied their vehement debate on the occasion, that their lives were dependent on the issue; the good chief was opposed to many other chiefs, who, though somewhat inferior in rank, were very far superior in number, supported by the common usages of the island, from which the exhibition of clemency appeared an insufferable deviation. He was seated, with his son by his side, on a mat in his own dwelling; he had been called to the supremacy of the island by the general wish of the people, as it was not a hereditary right, but an elective dignity. His people pressed their solicitations earnestly, and at length peremptorily demanded his assent to the sacrifice; which he for a length of time opposed by the force of words, which not seeming likely to prevail, he adopted a method which silenced the whole in an instant, and saved the lives of Capt. Fowler and his crew. Finding that all his expostulations were defeated, on the principle of undeviating custom, he deliberately took up two ropes that were near him, and fixing one round the neck of his son, and the other round his own, called to the chief next in command, who immediately approached him. His conference was short and decisive: he first pointed to the cord that encircled the neck of his son, and then to the other which he had entwined around his own. \"These strangers are doomed to death,\" said he, \"by my chiefs and my people: and it is not fit that I, who am their King, should live to see so vile a deed perpetrated. Let my child and myself be strangled before it is performed and then it never will be said that we sanctioned, even with our eye-sight, the destruction of these unoffending people.\" The magnanimity of such a conduct could not do less than produce, even in the mind of the unenlightened savage, a paroxysm of surprise, mingled with a sentiment of admiration in which the untaught man may possibly excel his fellow - creature, whose conceptions are moulded by tenets calculated to guard him from the extremes of passion. For a moment the people looked wildly upon their king, whose person they adored, because that his principles were good, and his government just and mild. They saw the obedient chief, to whom the order of strangulation had been imparted, staring with horror and amazement at the change which a few moments had produced; The mandate which had proceeded from the King's own lips must be obeyed; and, commanded to perform the dreadful office, he proceeded to obey when a sudden shout from the multitude awed him to forbearance. \"The King! the King!\" from every lip burst forth–'What! kill the King! No, no, let all the strangers live–no man shall kill the King!\" Thus were their lives preserved, and the vessel plundered of every thing on board her. The floor of the Greenwich, which was burnt at Noorheva, still remains, and is dry at low water. All her iron and copper have been taken out by the natives, who have a thorough knowledge of the use of these materials. That they are cannibals is well ascertained. They form distinct factions, and make war upon the ruling chief. The rebels are denominated the typees; and the opposite parties are horribly sanguinary towards each other. Six of the adverse party were killed and devoured by the rebels while Captain Fowler was among them, and the following detestable circumstance occurred on the occasion: A native man belonging to Port Anna Maria, who was not tattooed, and in consequence prohibited from the eating of human flesh, on pain of death, impatient of the restraint, fell upon one of the murdered bodies, and darting his teeth into it in all the madness of a voracious fury, exhaled the crimson moisture, which had not yet coagulated. The chief of Port Anna Maria, who is very friendly to Europeans, is named Ke-atta-nooe, the first part of the name implying the outrigger of a canoe, and the latter signifying great. The dress of the men consists merely of a wrapper about the waist; the women are covered from the shoulders downwards to the ancles, and are generally fairer than the Taheitan women. The chiefs have no distinguishing mark or ornament, but in the mode of wearing their hair; which the common orders wear tied up in a large knot on each side of the head, a stripe of which, extending from the forehead to the hollow of the neck, is kept shorn, which practice the chiefs do not adopt. Captain Fowler supposes the worms to be more prevalent and destructive to the ship's bottoms there than he has any where else witnessed; and to this cause attributes the caution of the natives in drawing up their largest canoes, some of which contain from 80 to 100 warriors. They are anxious after every kind of property carried among them for barter, and this is supposed their chief inducement for attacking vessels, when they can do so with a probability of accomplishing their object.– They have no knowledge of the use of muskets, and have none among them except a few at Port Anna Maria. A gentleman, at this time in Sydney, who resided among them about fifteen years ago in a Missionary capacity, describes them as a people constantly employing their thoughts on plunder, and devising schemes for taking advantage of strangers. Their population is very numerous; which he remarked to some of them, to whom he gave a description of Otaheite, observing at the same time, that its inhabitants were less numerous:–\" Can't we go and take them?- What is there to hinder us?\" was immediately demanded. This anecdote we notice as a specimen of their natural inclination to hostility, in which, all accounts respecting them correspond."

three = "DREADFUL MASSACRE BY THE NATIVES OF THE MARQUESAS ISLANDS. [ From the Sydney Gazette, Nov. 8. 1815.] By the Governor Macquarrie are arrived Captain Fowler, and part of the crew of the India brig Matilda, which sailed from this Colony in August 1813, bound on a voyage to the Derwent and Eastern Islands, and from thence to China; but was cut off and plundered on the night of the 10th of April last, while lying at anchor in Duff's Bay, at the Island of Rooapoah, one of the Marquessas, on a sandal-wood voyage. Five of the crew (Poomootoo men) had previously deserted, and joining with some of the Rooapoah natives, took the opportunity of a dark night, and the wind blowing fresh right on the land, to cut the vessel adrift; by which means she drove ashore through a heavy surf, and was soon bilged and filled with water. When the cannibal natives saw that it was impracticable to get the vessel afloat, they concurred universally in the design of putting the whole of her crew to death; which appears to have been a constant practise among the different natives towards one another, when their canoes happen to fall upon a strange land, through stress of weather, or from any other accident. Captain Fowler had formed an intimacy with their Chief, or King, Nooahetu, who presided at the horrible tribunal that had devoted the unfortunate mariners to instant slaughter. He withheld his assent to the murder; but had no hesitation in permitting the plunder of the vessel. The crew were informed by such expressions as they could understand, as well as by the gesticulations that accompanied their vehement debate on the occasion, that their lives were dependent on the issue; the good Chief was opposed by many other Chiefs, who, though somewhat inferior in rank, were very far superior in number, supported by the common usages of the island, from which the exhibition of clemency appeared an insufferable deviation. He was seated, with his son by his side, on a mat in his own dwelling; he had been called to the supremacy of the island by the general wish of the people, as it was not a hereditary right, but an elective dignity. His people pressed their solicitations earnestly , and at length peremptorily demanded his assent to the sacrifice; which he for a length of time opposed by the force of words, which not seeming likely to prevail, he adopted a method which silenced the whole in an instant, and saved the lives of Captain Fowler and his crew. Finding that all his expostulations were defeated, on the principle of undeviating custom, he deliberately took up two ropes that were near him, and fixing one round the neck of his son, and the other round his own, called to the Chief next in command, who immediately approached him. His conference was short and decisive–he first pointed to the cord that encircled the neck of his son, and then to the other which he had entwined round his own. \"These strangers are doomed to death,\" said he, \"by my chiefs and my people: and it is not fit that I, who am their King, should live to see so vile a deed perpetrated.– Let my child and myself be strangled before it is performed; and then it never will be said that we sanctioned, even with our eyesight, the destruction of these unoffending people.\" The magnanimity of such a conduct could not do less than produce, even in the mind of the unenlightened savage, a paroxysm of surprise, mingled with a sentiment of admiration, in which the untaught man may possibly excel his fellow-creature, whose conceptions are moulded by tenets calculated to guard him from the extremes of passion. For a moment the people looked wildly upon their King, whose person they adored, because that his principles were good, and his government just and mild. They saw the obedient Chief, to whom the order of strangulation had been imparted, staring with horror and amazement at the change which a few moments had produced; the mandate, which had proceeded from the King's own lips must be obeyed; and, commanded to perform the dreadful office, he proceeded to obey– when a sudden shout from the multitude awed him to forbearance. \"The King! the King!\" from every lip burst forth– 'What! kill the King! No, no, let all the strangers live–no man shall kill the King!\" Thus were their lives preserved, and the vessel plundered of every thing on board her. The floor of the Greenwich, which was burnt at Nooaheva, still remains, and is dry at low water. All her iron and copper have been taken out by the natives, who have a thorough knowledge of the use of these materials. That they are cannibals is well ascertained. They form distinct factions, and make war upon the ruling Chief. The rebels are denominated the Typees; and the opposite parties are horribly sanguinary towards each.– Six of the adverse party were killed and devoured by the rebels while Captain Fowler was among them, and the following detestable circumstance occurred on the occasion:–A native man belonging to Port Anna Maria, who was not tattooed, and in consequence prohibited from the eating of human flesh, on pain of death, impatient of the restraint, fell upon one of the murdered bodies, and darting his teeth into it in all the madness of a voracious fury, exhaled the crimson moisture, which had not yet coagulated."

# Tokenize
sone = re.sub('\s\s',' ',re.sub(r'([\"\.\(\),;])', r' \1 ', one))
stwo = re.sub('\s\s',' ',re.sub(r'([\"\.\(\),;])', r' \1 ', two))
sthree = re.sub('\s\s',' ',re.sub(r'([\"\.\(\),;])', r' \1 ', three))


# List-ify and create manifest of lists
l1 = sone.split()
l2 = stwo.split()
l3 = sthree.split()
documentlist = ["l1","l2","l3"]

# Create a new table with one column, characters, using document 1
table = pd.DataFrame(l1)
table.columns = ['characters']


# for each subsequent document, create a new column labeled with list name
for document in documentlist:
    table[document] = 0

# Input data for list 1
docnum = 0
rownum = 0
docrownum = 0
rowcount = len(table.index) + 1

for character in l1:
    rowcount = len(table.index) + 1
    if rowcount >= rownum:

        # if its the same, add 1 to next column
        if l1[docrownum] == table.iat[rownum,0]:
            table.set_value(rownum, "l1", 1)
            rownum +=1
            docrownum +=1

        # else check if the string pick up later on
        else:

            characterlist = table['characters'].tolist()

            # if it does exist
            if l1[docrownum] in characterlist:

                # create a newrow index number
                newrow = table[table['characters'] == l1[docrownum]].index.tolist()

                # check to see if new row is above old row
                if int(newrow[0]) < rownum:
                    tabletop = table[0:rownum]
                    tablebottom = table[rownum:]
                    table.set_value(rownum, "l1", 1)
                    frames = [tabletop, tablebottom]
                    table = pd.concat(frames)
                    table = table.reset_index(drop=True)
                    rownum +=1
                    docrownum +=1

                # if it isn't, continue
                else:

                    # check to see if either row is at the end of the list
                    if int(newrow[0]) < len(table) -1 and docrownum < len(l1) -1:

                        # check to see if its a true serial match
                        nextdocrownum = docrownum + 1
                        nextrownum = int(newrow[0])
                        nextrownum = nextrownum +1
                        nextword = table.iat[nextrownum,0]

                        if l1[nextdocrownum] == nextword:
                            # if it is, skip down to that row and continue
                            table.set_value(newrow, "l1", 1)
                            rownum = int(newrow[0])
                            rownum +=1
                            docrownum +=1

                        # if it isn't, append a new row with the word
                        else:
                            tabletop = table[0:rownum]
                            tablebottom = table[rownum:]
                            table.loc[rownum]=[l1[rownum],1,0,0]
                            frames = [tabletop, tablebottom]
                            table = pd.concat(frames)
                            table = table.reset_index(drop=True)
                            rownum +=1
                            docrownum +=1

                    else:
                        # check to see if they are both the same last character
                        if int(newrow[0]) == len(table) -1 and docrownum == len(l1) -1:
                            rownum = int(newrow[0])
                            if l1[docrownum] == table.iat[rownum,0]:
                                table.set_value(rownum, "l1", 1)
                                rownum +=1
                                docrownum +=1

                        else:
                            tabletop = table[0:rownum]
                            tablebottom = table[rownum:]
                            tabletop.loc[rownum]=[l1[rownum],1,0,0]
                            frames = [tabletop, tablebottom]
                            table = pd.concat(frames)
                            table = table.reset_index(drop=True)
                            rownum +=1
                            docrownum +=1

            # if it doesn't exist, append a new row with the word
            else:
                tabletop = table[0:rownum]
                tablebottom = table[rownum:]
                tabletop.loc[rownum]=[l1[rownum],1,0,0]
                frames = [tabletop, tablebottom]
                table = pd.concat(frames)
                table = table.reset_index(drop=True)
                rownum +=1
                docrownum +=1

# if it doesn't have any more rows in original character list, add new rows with new characters
    else:
        tabletop.loc[rownum]=[l1[rownum],1,0,0]
        table = table.reset_index(drop=True)
        rownum +=1
        docrownum +=1

# Clean up
tabletop = table[0:rownum]
tablebottom = table[rownum:]
tablebottom["l1"] = 0
frames = [tabletop, tablebottom]
table = pd.concat(frames)
table = table.reset_index(drop=True)


# Input data for list 2
docnum = 0
rownum = 0
docrownum = 0
rowcount = len(table.index) + 1

for character in l2:
    rowcount = len(table.index) + 1
    if rowcount >= rownum:

        # if its the same, add 1 to next column
        if l2[docrownum] == table.iat[rownum,0]:
            table.set_value(rownum, "l2", 1)
            rownum +=1
            docrownum +=1

        # else check if the string pick up later on
        else:

            characterlist = table['characters'].tolist()

            # if it does exist
            if l2[docrownum] in characterlist:

                # create a newrow index number
                newrow = table[table['characters'] == l2[docrownum]].index.tolist()

                # check to see if new row is above old row
                if int(newrow[0]) < rownum:
                    tabletop = table[0:rownum]
                    tablebottom = table[rownum:]
                    table.set_value(rownum, "l2", 1)
                    frames = [tabletop, tablebottom]
                    table = pd.concat(frames)
                    table = table.reset_index(drop=True)
                    rownum +=1
                    docrownum +=1

                # if it isn't, continue
                else:

                    # check to see if either row is at the end of the list
                    if int(newrow[0]) < len(table) -1 and docrownum < len(l2) -1:

                        # check to see if its a true serial match
                        nextdocrownum = docrownum + 1
                        nextrownum = int(newrow[0])
                        nextrownum = nextrownum +1
                        nextword = table.iat[nextrownum,0]

                        if l2[nextdocrownum] == nextword:
                            # if it is, skip down to that row and continue
                            table.set_value(newrow, "l2", 1)
                            rownum = int(newrow[0])
                            rownum +=1
                            docrownum +=1

                        # if it isn't, append a new row with the word
                        else:
                            tabletop = table[0:rownum]
                            tablebottom = table[rownum:]
                            table.loc[rownum]=[l2[rownum],0,1,0]
                            frames = [tabletop, tablebottom]
                            table = pd.concat(frames)
                            table = table.reset_index(drop=True)
                            rownum +=1
                            docrownum +=1

                    else:
                        # check to see if they are both the same last character
                        if int(newrow[0]) == len(table) -1 and docrownum == len(l2) -1:
                            rownum = int(newrow[0])
                            if l2[docrownum] == table.iat[rownum,0]:
                                table.set_value(rownum, "l2", 1)
                                rownum +=1
                                docrownum +=1

                        else:
                            tabletop = table[0:rownum]
                            tablebottom = table[rownum:]
                            tabletop.loc[rownum]=[l2[rownum],0,1,0]
                            frames = [tabletop, tablebottom]
                            table = pd.concat(frames)
                            table = table.reset_index(drop=True)
                            rownum +=1
                            docrownum +=1

            # if it doesn't exist, append a new row with the word
            else:
                tabletop = table[0:rownum]
                tablebottom = table[rownum:]
                tabletop.loc[rownum]=[l2[rownum],0,1,0]
                frames = [tabletop, tablebottom]
                table = pd.concat(frames)
                table = table.reset_index(drop=True)
                rownum +=1
                docrownum +=1

# if it doesn't have any more rows in original character list, add new rows with new characters
    else:
        tabletop.loc[rownum]=[l2[rownum],0,1,0]
        table = table.reset_index(drop=True)
        rownum +=1
        docrownum +=1

# Clean up
tabletop = table[0:rownum]
tablebottom = table[rownum:]
tablebottom["l2"] = 0
frames = [tabletop, tablebottom]
table = pd.concat(frames)
table = table.reset_index(drop=True)

# Input data for list 3
docnum = 0
rownum = 0
docrownum = 0
rowcount = len(table.index) + 1

for character in l3:
    rowcount = len(table.index) + 1
    if rowcount >= rownum:

        # if its the same, add 1 to next column
        if l3[docrownum] == table.iat[rownum,0]:
            table.set_value(rownum, "l3", 1)
            rownum +=1
            docrownum +=1

        # else check if the string pick up later on
        else:

            characterlist = table['characters'].tolist()

            # if it does exist
            if l3[docrownum] in characterlist:

                # create a newrow index number
                newrow = table[table['characters'] == l3[docrownum]].index.tolist()

                # check to see if new row is above old row
                if int(newrow[0]) < rownum:
                    tabletop = table[0:rownum]
                    tablebottom = table[rownum:]
                    table.set_value(rownum, "l3", 1)
                    frames = [tabletop, tablebottom]
                    table = pd.concat(frames)
                    table = table.reset_index(drop=True)
                    rownum +=1
                    docrownum +=1

                # if it isn't, continue
                else:

                    # check to see if either row is at the end of the list
                    if int(newrow[0]) < len(table) -1 and docrownum < len(l3) -1:

                        # check to see if its a true serial match
                        nextdocrownum = docrownum + 1
                        nextrownum = int(newrow[0])
                        nextrownum = nextrownum +1
                        nextword = table.iat[nextrownum,0]

                        if l3[nextdocrownum] == nextword:
                            # if it is, skip down to that row and continue
                            table.set_value(newrow, "l3", 1)
                            rownum = int(newrow[0])
                            rownum +=1
                            docrownum +=1

                        # if it isn't, append a new row with the word
                        else:
                            tabletop = table[0:rownum]
                            tablebottom = table[rownum:]
                            table.loc[rownum]=[l3[rownum],0,0,1]
                            frames = [tabletop, tablebottom]
                            table = pd.concat(frames)
                            table = table.reset_index(drop=True)
                            rownum +=1
                            docrownum +=1

                    else:
                        # check to see if they are both the same last character
                        if int(newrow[0]) == len(table) -1 and docrownum == len(l3) -1:
                            rownum = int(newrow[0])
                            if l3[docrownum] == table.iat[rownum,0]:
                                table.set_value(rownum, "l3", 1)
                                rownum +=1
                                docrownum +=1

                        else:
                            tabletop = table[0:rownum]
                            tablebottom = table[rownum:]
                            tabletop.loc[rownum]=[l3[rownum],0,0,1]
                            frames = [tabletop, tablebottom]
                            table = pd.concat(frames)
                            table = table.reset_index(drop=True)
                            rownum +=1
                            docrownum +=1

            # if it doesn't exist, append a new row with the word
            else:
                tabletop = table[0:rownum]
                tablebottom = table[rownum:]
                tabletop.loc[rownum]=[l3[rownum],0,0,1]
                frames = [tabletop, tablebottom]
                table = pd.concat(frames)
                table = table.reset_index(drop=True)
                rownum +=1
                docrownum +=1

# if it doesn't have any more rows in original character list, add new rows with new characters
    else:
        tabletop.loc[rownum]=[l3[rownum],0,0,1]
        table = table.reset_index(drop=True)
        rownum +=1
        docrownum +=1

# Clean up
tabletop = table[0:rownum]
tablebottom = table[rownum:]
tablebottom["l3"] = 0
frames = [tabletop, tablebottom]
table = pd.concat(frames)
table = table.reset_index(drop=True)

# Create CSV matrix
table.to_csv('matrix.csv')

