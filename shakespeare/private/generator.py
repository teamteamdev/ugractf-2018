import random

plaintext = '''
ccdWHEN my love swears that she is made of truth, 
ddcI do believe her, though I know she lies, 
cdcThat she might think me some untutor'd youth, 
cdUnskilful in the world's false forgeries. 
ddThus vainly thinking that she thinks me young, 
cdAlthough I know my years be past the best, 
dccI smiling credit her false-speaking tongue, 
cddcOutfacing faults in love with love's ill rest. 
dddBut wherefore says my love that she is young? 
cAnd wherefore say not I that I am old? 
dO, love's best habit is a soothing tongue, 
cdcAnd age, in love, loves not to have years told. 
dcddTherefore I'll lie with love, and love with me, 
Since that our faults in love thus smother'd be. 

Two loves I have, of comfort and despair, 
That like two spirits do suggest me still; 
My better angel is a man right fair, 
My worser spirit a woman colour'd ill. 
To win me soon to hell, my female evil 
Tempteth my better angel from my side, 
And would corrupt my saint to be a devil, 
Wooing his purity with her fair pride. 
And whether that my angel be turn'd fiend, 
Suspect I may, yet not directly tell: 
For being both to me, both to each friend, 
I guess one angel in another's hell; 
The truth I shall not know, but live in doubt,
Till my bad angel fire my good one out. 

Did not the heavenly rhetoric of thine eye, 
'Gainst whom the world could not hold argument, 
Persuade my heart to this false perjury? 
Vows for thee broke deserve not punishment. 
A woman I forswore; but I will prove, 
Thou being a goddess, I forswore not thee: 
My vow was earthly, thou a heavenly love; 
Thy grace being gain'd cures all disgrace in me. 
My vow was breath, and breath a vapour is; 
Then, thou fair sun, that on this earth doth shine, 
Exhale this vapour vow; in thee it is: 
If broken, then it is no fault of mine. 
If by me broke, what fool is not so wise 
To break an oath, to win a paradise? 

Sweet Cytherea, sitting by a brook 
With young Adonis, lovely, fresh, and green, 
Did court the lad with many a lovely look, 
Such looks as none could look but beauty's queen. 
She told him stories to delight his ear; 
She showed him favors to allure his eye; 
To win his heart, she touch'd him here and there,
Touches so soft still conquer chastity. 
But whether unripe years did want conceit, 
Or he refused to take her figured proffer, 
The tender nibbler would not touch the bait, 
But smile and jest at every gentle offer: 
Then fell she on her back, fair queen, and toward: 
He rose and ran away; ah, fool too froward! 

If love make me forsworn, how shall I swear to love? 
O never faith could hold, if not to beauty vow'd: 
Though to myself forsworn, to thee I'll constant prove; 
Those thoughts, to me like oaks, to thee like osiers bow'd. 
Study his bias leaves, and makes his book thine eyes, 
Where all those pleasures live that art can comprehend. 
If knowledge be the mark, to know thee shall suffice; 
Well learned is that tongue that well can thee commend; 
All ignorant that soul that sees thee without wonder; 
Which is to me some praise, that I thy parts admire: 
Thine eye Jove's lightning seems, thy voice his dreadful 
thunder, 
Which, not to anger bent, is music and sweet fire. 
Celestial as thou art, O do not love that wrong, 
To sing heaven's praise with such an earthly tongue. 
'''.upper()

alp = 'abcdefghijklmnopqrstuvwxyz'
key = list(alp)
random.shuffle(key)
alp = alp.upper()

for i in range(len(alp)):
    plaintext = plaintext.replace(alp[i],key[i])

print(plaintext)