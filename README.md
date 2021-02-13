# school-stack
A program to analyze and allow people to get the most information out of a list of schools.

### Description
<div>
The purpose of this program is to provide a top-level command line interface to query
and analyze data about every school in the United States. Each command can have different
modifiers so the output can be completely customized depending on what the user is searching
for in terms of their target schools they wish to contact.
</div>

### Noteworthy Commands
Keep in mind, the arguments to each command is completely optional, an example to get the school with the most female students 
 would be:
> schools --sex=Female

| command | arguments                                                                                                                                                                                        | value of argument                                                                          | summary                                                                                                   |
|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| schools | minority=value <br> locationState=value <br> locationCity=value <br> locationZip=value free&reducedLunch=value <br> sex=value <br> hasWebsite=value <br> <from_row>:<to_row> | boolean <br> string <br> string <br> int <br> boolean <br> string <br> boolean <br> string | Displays information about any number of schools based on whichever modifiers are applied to the command. |
| info    | minority=value <br> locationState=value <br> locationCity=value <br> locationZip=value <br>                                                                                                      | boolean <br> string <br> string <br> int <br>                                              | Displays general information such as count, mean, standard deviation,  min, percentailes, and max values. |
| quit    | none                                                                                                                                                                                             |                                                                                            | Exits out of the program.                                                                                 |

### Libraries
- Pandas: https://pandas.pydata.org/
- Numpy: https://numpy.org/

