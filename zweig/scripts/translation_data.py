# -*- coding: utf-8 -*-
"""Draft translation of Zweig, "Die Entdeckung Eldorados" (Sternstunden der Menschheit).

Used ONCE by scripts/make_paragraphs.py to create the per-paragraph YAML files.
After that, the YAML files are canonical and `translation_draft` in them is immutable;
edit `translation_final` in the YAML, never this file.
"""

TITLE_EN = "The Discovery of Eldorado"
DATELINE_EN = "J. A. Suter, California. January 1848"

# German heading -> English heading
SECTIONS = {
    "Der Europamüde": "Weary of Europe",
    "Der Marsch nach Kalifornien": "The March to California",
    "Neu-Helvetien": "New Helvetia",
    "Der verhängnisvolle Spatenstich": "The Fateful Stroke of the Spade",
    "Der Rush": "The Rush",
    "Der Prozeß": "The Lawsuit",
    "Das Ende": "The End",
}

# One entry per paragraph, in order. Each: (draft, annotations, ocr_corrections)
P = []

def para(draft, annotations=None, corrections=None):
    P.append((draft.strip(), annotations or [], corrections or []))

def note(span, body):
    return {"type": "note", "span": span, "body": body.strip()}

def quote(span, ref, body):
    return {"type": "quote", "span": span, "quote_library_ref": ref, "body": body.strip()}

def query(span, body):
    return {"type": "query", "span": span, "body": body.strip()}

# ── Der Europamüde ───────────────────────────────────────────────────────────

para("""
1834. A steamer bound for America is making its way from Le Havre to New York. In the very midst of the desperadoes, one among hundreds, Johann August Suter, native of Rynenberg near Basel, thirty-one years of age and in the utmost haste to put the ocean between himself and the courts of Europe, bankrupt, thief, forger of bills, has simply left his wife and three children in the lurch, procured himself a little money in Paris with a fraudulent passport, and is now in search of a new existence. On 7 July he lands in New York, and there for two years he plies every trade possible and impossible, turning packer, druggist, dentist, vendor of medicines, tavern-keeper. At length, settled after a fashion, he establishes himself in an inn, sells it again, and, following the magical drift of the age, moves on to Missouri. There he becomes a farmer, in a short time acquires a small property of his own, and might live in peace. But always there are people hurrying past his house, fur-traders, hunters, adventurers, and soldiers, they come from the West, they go to the West, and little by little this word West acquires a magical ring. First, so much is known, there are plains, plains with immense herds of buffalo, empty of men for days, for weeks on end, ridden through only by the Red Indians, then come mountains, high, unclimbed, then at last that other land of which no one knows anything certain and whose fabled riches are everywhere extolled, California, the still unexplored. A land flowing with milk and honey, free to any man who will take it – only far, infinitely far, and to be reached at peril of one’s life.
""", [
    note("Johann August Suter",
         "The historical figure is known in English as John Augustus Sutter. Zweig uses the German form of the name throughout and we keep it: the story is Zweig’s Suter, not the biographer’s Sutter (see DECISION-Z03)."),
    note("Rynenberg near Basel",
         "Zweig’s spelling. The family came from Rünenberg in the canton of Basel-Landschaft (Sutter himself was born across the border in Kandern, Baden). Kept as Zweig wrote it; Basel given in its modern form."),
    note("settled after a fashion",
         "Zweig writes *gesettlet*, a jocular German past participle made from the English ‘settle’. English cannot reproduce the joke, since the word is simply English; ‘after a fashion’ keeps a little of its irony."),
    note("magical drift of the age",
         "*magisch* is a leitmotif of the piece: the magical pull of the age, the magical ring of the word West, the lure of the magical name, and finally the magic word ‘Eldorado’. It is rendered ‘magical’ or ‘magic’ every time so that the chain survives."),
    note("Red Indians",
         "Zweig’s *Rothäute* (literally ‘redskins’). We give the interwar British idiom ‘Red Indians’, which keeps the period register and the 1927 outlook without sharpening the slur beyond the original. The editor may prefer the literal word."),
    quote("A land flowing with milk and honey", "bible-exodus-3-8",
          "Zweig echoes Luther’s Exodus 3:8 (*ein Land, darin Milch und Honig fließt*); the English is the Authorised Version phrase an English reader recognises."),
])

para("""
But Johann August Suter has the blood of an adventurer, it holds no lure for him to sit still and till his good land. One day, in the year 1837, he sells all that he has, fits out an expedition with wagons and horses and herds of buffalo, and sets out from Fort Independence into the unknown.
""")

# ── Der Marsch nach Kalifornien ──────────────────────────────────────────────

para("""
1838. Two officers, five missionaries, three women set out in buffalo-wagons into the infinite emptiness. Across plains and plains, and at last over the mountains, towards the Pacific Ocean. For three months they travel, to arrive at the end of October at Fort Vancouver. The two officers have left Suter before this, the missionaries go no farther, the three women have died on the way of privation.
""", [
    note("buffalo-wagons",
         "Zweig’s *Büffelwagen*. Historically these would have been ox-wagons, but the buffalo is one of Zweig’s recurring images of the West (the herds, the sixty buffalo that haul the steam-engine), so the word is kept."),
])

para("""
Suter is alone, in vain they seek to keep him at Vancouver, offer him a position – he refuses everything, the lure of the magical name is in his blood. In a wretched sailing-ship he crosses the Pacific, first to the Sandwich Islands, and, after endless difficulties along the coasts of Alaska, lands at a forsaken spot by the name of San Francisco. San Francisco – not the city of today, which after the earthquake shot up with redoubled growth to its millions – no, only a miserable fishing village, so called after the mission of the Franciscans, not even the capital of that obscure Mexican province of California which lies fallow, neglected, ungoverned and unflowering, in the most luxuriant zone of the new continent.
""", [
    note("Vancouver",
         "Zweig writes *Van Couver*, and *Neuyork*, *San Franzisko*, *Sakramento*, *Monte Rey*, *Le Hâvre*. All place-names are given silently in their standard English forms (DECISION-Z04). ‘Sandwich Islands’ is kept as the period name for Hawaii."),
])

para("""
Spanish disorder, aggravated by the absence of all authority, revolts, a want of beasts of burden and of men, a want of energy to take things in hand. Suter hires a horse and drives it down into the fertile valley of the Sacramento: a single day suffices to show him that here there is room not merely for a farm, for a great estate, but space for a kingdom. The next day he rides to Monterey, the wretched capital, presents himself to Governor Alvarado, and explains his intention of bringing the land under cultivation. He has brought Kanakas with him from the islands, means to have more of these diligent and industrious coloured men sent after him regularly, and undertakes to build settlements and to found a little realm, a colony, New Helvetia.
""", [
    note("Governor Alvarado",
         "Zweig misspells the name *Alverado*. Juan Bautista Alvarado was governor of Alta California from 1836 to 1842; the correct spelling is given silently, as with the place-names."),
    note("Kanakas",
         "*Kanaken*: the nineteenth-century word, in English as in German, for Pacific Islanders employed as labourers, and the word used in the English sources on Sutter. *Farbigen* is given literally as ‘coloured men’ to keep the 1927 register."),
])

para("""
‘Why New Helvetia?’ asks the Governor. ‘I am a Swiss and a republican,’ answers Suter.
""")

para("""
‘Good, do what you will, I give you a concession for ten years.’
""")

para("""
One sees: business is quickly concluded out there. A thousand miles from any civilisation, the energy of a single man fetches a different price from what it fetches at home.
""")

# ── Neu-Helvetien ────────────────────────────────────────────────────────────

para("""
1839. A caravan trundles slowly upstream along the banks of the Sacramento. In front Suter on horseback, rifle slung, behind him two or three Europeans, then a hundred and fifty Kanakas in short shirts, then thirty buffalo-wagons with provisions, seed, and ammunition, fifty horses, seventy-five mules, cows and sheep, then a short rearguard – that is the whole army that means to conquer itself a New Helvetia.
""")

para("""
Before them rolls a gigantic wave of fire. They set the forests alight, a more convenient method than clearing them. And scarcely has the vast blaze raced across the land when, upon the still-smoking stumps, they begin their work. Storehouses are built, wells dug, the soil, which needs no ploughing, sown, folds made for the endless herds; little by little new hands flow in from the neighbouring places, from the abandoned mission settlements.
""", [
    note("gigantic",
         "*gigantisch* recurs a dozen times in the piece (the wave of fire, the success, the enterprise, the dragon’s crop). Zweig’s insistence is deliberate and is kept, as with Szerb’s repetitions."),
])

para("""
The success is gigantic. The crops yield five hundred per cent at once. The barns are bursting, soon the herds are counted in thousands, and notwithstanding the continual difficulties in the country, the expeditions against the natives, who again and again venture raids upon the flourishing colony, New Helvetia unfolds to a tropical, gigantic greatness. Canals, mills, trading-posts are established, ships ply up and down the rivers, Suter supplies not only Vancouver and the Sandwich Islands but every sailing-ship that puts in at California, he plants fruit, the fruit of California so famous and so much admired today. And behold! it thrives, and so he sends for vines from France and from the Rhine, and after a few years they cover wide tracts of land. For himself he builds houses and sumptuous farms, has a Pleyel piano brought from Paris, a hundred and eighty days’ journey, and a steam-engine from New York, drawn by sixty buffalo across the whole continent. He has credit and balances with the greatest banking-houses of England and France, and now, forty-five years old, at the height of his triumph, he remembers that fourteen years ago he left a wife and three children somewhere in the world. He writes to them and invites them to come to him, into his principality. For now he feels the fullness in his fists, he is lord of New Helvetia, one of the richest men in the world, and will remain so. At last the United States, too, wrest the neglected colony from Mexico’s hands. Now all is secured and safe. A few years more, and Suter is the richest man in the world.
""", [
    note("And behold! it thrives",
         "*Sieh da! es gedeiht*, with the lower-case continuation after the exclamation, as Zweig punctuates it. ‘Behold’ is the one slightly elevated word in the passage, matching the narrator’s mock-biblical wonder."),
    note("the fullness in his fists",
         "*die Fülle in den Fäusten*: the alliteration is kept."),
    note("Suter is the richest man in the world",
         "The refrain ‘the richest man in the world’ (*der reichste Mann der Welt*) structures the whole piece and is reversed three times. It is rendered identically on every occurrence, in Zweig’s present tense."),
])

# ── Der verhängnisvolle Spatenstich ──────────────────────────────────────────

para("""
1848, in January. Suddenly James W. Marshall, his carpenter, comes bursting excitedly into Johann August Suter’s house: he must speak to him without fail. Suter is astonished, for only yesterday he sent Marshall up to his farm at Coloma to set up a new sawmill there. And now the man has come back without leave, stands before him trembling with excitement, presses him into his room, locks the door, and draws from his pocket a handful of sand with a few yellow grains in it. Yesterday, while digging, he had noticed this curious metal; he believed it was gold, but the others had laughed at him. Suter grows grave, takes the grains, and makes the assay: it is gold. He resolves to ride up to the farm with Marshall first thing the next day, but the master carpenter is the first to be seized by the terrible fever that will soon shake the world: that very night, in the midst of a storm, he rides back, impatient for certainty.
""", [
    note("makes the assay",
         "*macht die Scheideprobe*: the parting test that separates gold from silver with acid. ‘Assay’ is the period English term."),
])

para("""
The next morning Colonel Suter is at Coloma; they dam the mill-race and examine the sand. One need only take a sieve and shake it a little to and fro, and the grains of gold remain, gleaming, on the black mesh. Suter gathers the few white men about him, takes their word of honour to keep silent until the sawmill is finished, and then rides back to his farm, grave and resolute. Tremendous thoughts move him: within the memory of man, gold has never lain so easily to hand, so openly in the earth, and this earth is his, is Suter’s property. A decade seems to have been leapt over in a single night: he is the richest man in the world.
""", [
    note("mill-race",
         "Zweig’s *Kanal*. The channel in question is the race of the sawmill under construction, where the gold was in fact found; ‘canal’ would mislead."),
])

# ── Der Rush ─────────────────────────────────────────────────────────────────

para("""
The richest man? No – the poorest, the most wretched, the most disappointed beggar on this earth. Within eight days the secret is betrayed, a woman – always a woman! – has told it to some passer-by and given him a few grains of gold. And what now follows is without precedent. At once all Suter’s men leave their work, the smiths run from the forge, the shepherds from the flocks, the vine-dressers from the vines, the soldiers abandon their rifles, all are as if possessed and run with hastily fetched sieves and saucepans to the sawmill, to shake gold out of the sand. Overnight the whole country is deserted, the milch-cows, which no one milks, bellow and die, the herds of buffalo break their folds and trample into the fields, where the grain rots on the stalk, the dairies stand idle, the barns fall in, the vast wheelwork of the gigantic enterprise stands still. Telegraphs flash the golden promise over lands and seas. And already people are coming up from the towns, from the harbours, sailors desert their ships, government officials their posts, in long, endless columns they come streaming from the east, from the west, on foot, on horseback, and by wagon, the Rush, the human swarm of locusts, the gold-diggers. An unbridled, brutal horde, knowing no law but that of the fist, no command but that of the revolver, pours over the flourishing colony. To them everything is ownerless, no one dares to stand up to these desperadoes. They slaughter Suter’s cows, they pull down his barns to build themselves houses, they trample his fields, they steal his machines – overnight Johann August Suter has become a pauper, like King Midas, stifled in his own gold.
""", [
    note("the Rush",
         "Zweig uses the English word (*der Rush*) as his section title and here, as Szerb uses ‘thrill’ (cf. Szerb DECISION-004). In English the borrowing is invisible, so it is capitalised to keep its force as a name."),
    note("Telegraphs flash",
         "An anachronism of Zweig’s (there was no telegraph to California in 1848); kept as written."),
    quote("like King Midas, stifled in his own gold", "ovid-metamorphoses-xi-midas",
          "Allusion to Midas, whose touch turned even his food to gold (Ovid, *Metamorphoses* XI). Zweig’s *erstickt* (‘stifled, smothered’) is his own sharpening of the myth."),
])

para("""
And ever more violent grows this unexampled storm after gold; the news has gone out into the world, from New York alone a hundred ships set sail, from Germany, from England, from France, from Spain, in 1848, 1849, 1850, 1851, enormous hordes of adventurers come over. Some sail round Cape Horn, but that is too long for the most impatient, and so they choose the more dangerous way across the Isthmus of Panama. A company, swift to resolve, briskly builds a railway across the Isthmus, at which thousands of labourers perish of fever, only so that the impatient may be spared three or four weeks and reach the gold the sooner. Across the continent move enormous caravans, people of all races and tongues, and all of them grub about in Johann August Suter’s property as though on their own ground. On the soil of San Francisco, which belongs to him by sealed act of the government, a city grows with the speed of a dream, strangers sell one another his land and soil, and the name New Helvetia, his realm, vanishes behind the magic word: Eldorado, California.
""")

para("""
Johann August Suter, bankrupt once more, stares as if paralysed at this gigantic crop of dragon’s teeth. At first he tries to dig with the rest and, with his servants and companions, to exploit the riches himself, but all of them desert him. So he withdraws altogether from the gold district, to a secluded farm near the mountains, away from the accursed river and the unholy sand, to his farm the Hermitage. There his wife at last reaches him with the three children, now grown, but scarcely has she arrived when she dies of the exhaustion of the journey. Yet three sons are there now, eight arms, and with them Johann August Suter takes up farming; once more, now with his three sons, he works his way up, quietly, tenaciously, and turns to account the fantastic fertility of this soil. Once more he harbours and hides a great design.
""", [
    quote("gigantic crop of dragon’s teeth", "ovid-metamorphoses-iii-cadmus",
          "*Drachensaat*, ‘dragon’s sowing’: Cadmus sows the teeth of the slain dragon and a crop of armed men springs up and turns on itself (Ovid, *Metamorphoses* III). ‘Dragon’s teeth’ is the form in which the figure is current in English."),
    note("the Hermitage",
         "Zweig’s *Eremitage*, following Cendrars’s *L’Ermitage*. Sutter’s farm on the Feather River was in fact called Hock Farm; Zweig’s name is kept and given in English."),
    note("harbours and hides",
         "*birgt und verbirgt*: Zweig’s play on the simple and prefixed verb. ‘Harbours and hides’ keeps a pairing of sound in place of the etymological one."),
])

# ── Der Prozeß ───────────────────────────────────────────────────────────────

para("""
1850. California has been admitted into the Union of the United States. Under their stern discipline, after riches, order at last comes to the gold-possessed land. Anarchy is tamed, the law regains its rights.
""")

para("""
And now Johann August Suter suddenly comes forward with his claims. The whole of the ground, so he demands, on which the city of San Francisco is built belongs to him by every right. The State is bound to make good the damage he has suffered by the theft of his property, of all the gold extracted from his soil he claims his share. A lawsuit begins, of dimensions such as mankind had never known before. Johann August Suter sues 17,221 farmers who have settled on his plantations and calls upon them to quit the stolen land, he demands 25 million dollars from the State of California for having simply appropriated the roads, canals, bridges, dams, and mills he built, he demands 25 million dollars from the Union as compensation for property destroyed, and in addition his share of the gold extracted. He has had his elder son, Emil, study law in Washington in order to conduct the case, and he uses the enormous revenues of his new farms solely to feed this costly lawsuit. For four years he drives it through every court.
""", [
    note("his elder son",
         "Zweig writes *älteren* (‘elder’) of three sons; the comparative is kept rather than silently corrected to ‘eldest’."),
])

para("""
On 15 March 1855 judgement is at last pronounced. The incorruptible Judge Thompson, the highest official in California, recognises Johann August Suter’s rights to the land as entirely justified and inviolable.
""")

para("""
On this day Johann August Suter has reached his goal. He is the richest man in the world.
""")

# ── Das Ende ─────────────────────────────────────────────────────────────────

para("""
The richest man in the world? No, and again no, the poorest beggar, the unhappiest, the most broken of men. Once more Fate deals him one of those murderous blows, but this time one that lays him low for ever. At the news of the judgement a storm breaks loose in San Francisco and throughout the country. Tens of thousands band together, all the threatened owners, the mob of the streets, the rabble ever eager for plunder, they storm the Palace of Justice and burn it down, they hunt for the judge to lynch him, and they set out, an immense multitude, to plunder the whole of Johann August Suter’s possessions. His eldest son, hard pressed by the bandits, shoots himself, the second is murdered, the third flees and is drowned on the way home. A wave of fire sweeps over New Helvetia, Suter’s farms are burnt down, his vines trampled, his furniture, his collections, his money carried off, and with pitiless fury the vast estate is made a wilderness. Suter himself escapes by a hair’s breadth.
""", [
    note("A wave of fire",
         "*Feuerwoge*, the same word as the ‘gigantic wave of fire’ with which Suter cleared the land in 1839; the echo is deliberate and the same English is used."),
    note("His eldest son, hard pressed by the bandits, shoots himself",
         "Here, as throughout the last two sections, Zweig follows Cendrars’s novel rather than the historical record (Sutter’s wife and sons did not die as described). The translation renders Zweig and does not correct him; the departures are a matter for an introduction, not for the text."),
])

para("""
From this blow Johann August Suter never recovered. His work is annihilated, his wife, his children are dead, his mind is deranged: one idea alone still flickers confusedly in the dulled brain: his right, the lawsuit.
""", [
    note("his right, the lawsuit",
         "*das Recht* (right, justice, law) runs through the close: ‘his right’ here, ‘he wants only his rights’, ‘justice has not been done’, and finally ‘the one right of a great destiny’. English must divide the word between ‘right’ and ‘justice’; ‘right’ is kept wherever the sense allows, so that the last sentence still lands on it."),
])

para("""
For twenty-five years more an old, feeble-minded, shabbily dressed man wanders about the Palace of Justice in Washington. In every office there they know the ‘General’ in the dirty frock-coat and the tattered shoes who demands his billions. And again and again there are lawyers, adventurers, and sharpers who wheedle from him the last of his pension and drive him afresh into litigation. He himself wants no money, he hates the gold that has made him poor, that has murdered three of his children, that has destroyed his life. He wants only his rights, and he champions them with the querulous bitterness of the monomaniac. He petitions the Senate, he petitions Congress, he entrusts himself to all manner of helpers who, rigging the affair out with pomp, put him into a ridiculous general’s uniform and drag the unfortunate man as a figure of fun from office to office, from Congressman to Congressman. This goes on for twenty years, from 1860 to 1880, twenty miserable years of beggary. Day after day he haunts the Capitol, the scorn of every official, the sport of every street-urchin, he to whom the richest land on earth belongs, and on whose land and soil the second capital of the giant realm stands and grows by the hour. But they let the troublesome man wait. And there, on the steps of the Capitol, on the afternoon of 17 July 1880, the heart-seizure that releases him at last strikes him down – they carry away a dead beggar. A dead beggar, but one with a statement of claim in his pocket that secures to him and his heirs, by every earthly law, the title to the greatest fortune in the history of the world.
""", [
    note("For twenty-five years more",
         "Zweig says twenty-five years here and ‘twenty years, from 1860 to 1880’ a few lines later. The inconsistency is his and is kept."),
    note("the Palace of Justice in Washington",
         "*Justizpalast*, a Continental institution transplanted by Zweig to San Francisco and Washington alike. It is kept as ‘Palace of Justice’ in both places, since the European colouring is part of his America; *Kongreßpalast* is given as ‘the Capitol’, which is unambiguous."),
    note("the scorn of every official, the sport of every street-urchin",
         "*Spott aller Beamten, Spiel aller Gassenjungen*: the alliteration is kept."),
    note("17 July 1880",
         "So Zweig, after Cendrars. Sutter in fact died in a Washington hotel on 18 June 1880, Congress having adjourned without acting on his petition. Not corrected (see the note on p21)."),
])

para("""
No one has yet claimed Suter’s inheritance, no descendant has entered his claim. Still San Francisco stands, still a whole country stands, on another man’s ground. Still no justice has been done here, and only an artist, Blaise Cendrars, has given the forgotten Johann August Suter at least the one right of a great destiny, the right to the wondering remembrance of posterity.
""", [
    quote("Blaise Cendrars", "cendrars-l-or",
          "Zweig’s acknowledgement of his source: Cendrars’s novel *L’Or* (1925), translated into English in 1926 as *Sutter’s Gold*. Zweig’s chapter is largely a condensation of it, including its departures from history."),
])

QUOTE_LIBRARY = [
    {
        "id": "bible-exodus-3-8",
        "type": "allusion",
        "author": "Bible",
        "work": "Exodus",
        "locus": "3:8",
        "original_language": "de",
        "original": "ein Land, darin Milch und Honig fließt (Luther)",
        "zweig_rendering": "Ein Land, wo Milch und Honig fließt",
        "english_used": "a land flowing with milk and honey",
        "english_provenance": "Authorised Version (1611)",
        "used_in": ["discovery-of-eldorado-p01"],
    },
    {
        "id": "ovid-metamorphoses-xi-midas",
        "type": "allusion",
        "author": "Ovid",
        "work": "Metamorphoses",
        "locus": "XI.85–145",
        "original_language": "la",
        "original": "(the golden touch of Midas)",
        "zweig_rendering": "wie König Midas, erstickt im eigenen Gold",
        "english_used": "like King Midas, stifled in his own gold",
        "english_provenance": "Fresh translation of Zweig; allusion only, no text quoted",
        "used_in": ["discovery-of-eldorado-p14"],
    },
    {
        "id": "ovid-metamorphoses-iii-cadmus",
        "type": "allusion",
        "author": "Ovid",
        "work": "Metamorphoses",
        "locus": "III.95–130",
        "original_language": "la",
        "original": "(Cadmus sows the dragon’s teeth)",
        "zweig_rendering": "diese gigantische Drachensaat",
        "english_used": "this gigantic crop of dragon’s teeth",
        "english_provenance": "Fresh translation of Zweig; the English idiom ‘dragon’s teeth’ used for the figure",
        "used_in": ["discovery-of-eldorado-p16"],
    },
    {
        "id": "cendrars-l-or",
        "type": "allusion",
        "author": "Blaise Cendrars",
        "work": "L’Or: La merveilleuse histoire du général Johann August Suter",
        "locus": "passim",
        "original_language": "fr",
        "original": "(the novel as a whole: Zweig’s principal source)",
        "zweig_rendering": "nur ein Künstler, Blaise Cendrars",
        "english_used": "only an artist, Blaise Cendrars",
        "english_provenance": "English translation: Sutter’s Gold, trans. Henry Longan Stuart (1926). Not quoted.",
        "used_in": ["discovery-of-eldorado-p24"],
    },
]
