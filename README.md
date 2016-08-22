# Reprint Matrix Generator
A simple programme for converting plain-text transcriptions of reprints into a binary matrix for phylogenetic analysis

Input properly formatted (no un-escaped double quotation marks) plain-text transcriptions as "one", "two" and "three" and run programme to create a matrix

+ Rows listing all words or punctuation marks in the text files
+ Columns for each document analysed

Matrices built on the principle that each change, in order, is an 'edit' to the original text, and recorded. Current build, in essence, records identical word orders (1s) and notes 0s for word or punctuation omissions and adds new rows for additions.

Will "skip down" to correct row in the case of omitted text.

## Future Changes

+ Allow input of import files
+ Allow for automatic looping of each file (rather than creating instructions for each)

Suggestions and improvements welcome
