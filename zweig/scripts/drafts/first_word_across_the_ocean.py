# -*- coding: utf-8 -*-
"""Draft translation of Zweig, "Das Erste Wort über den Ozean" (Sternstunden der Menschheit).

Used ONCE by scripts/make_paragraphs.py to create the per-paragraph YAML files.
After that, the YAML files are canonical and `translation_draft` in them is immutable;
edit `translation_final` in the YAML, never this file.
"""
from drafting import Draft, note, quote, query

D = Draft(
    slug="first-word-across-the-ocean",
    source_file="das-erste-wort-ueber-den-ozean.txt",
    source_url="https://projekt-gutenberg.org/authors/stefan-zweig/books/sternstunden-der-menschheit/chapter/11/",
    title_en="The First Word Across the Ocean",
    dateline_en="Cyrus W. Field, 28 July 1858",
    order=2,
    first_published="1943, in the enlarged edition of Sternstunden der Menschheit (Stockholm: Bermann-Fischer), to be verified",
    blurb="A retired merchant who has never seen a cable sets out to join Europe and America by telegraph, and is cheered and cursed within a single month.",
    rights="This chapter does not appear to have been in the 1927 first edition; it seems to have been first published in the enlarged edition of 1943. If so, it is in the public domain in the UK and EU but may remain in copyright in the United States until the end of 2038. This is being checked.",
    sections={
        "Der neue Rhythmus": "The New Rhythm",
        "Die Vorbereitung": "The Preparations",
        "Der erste Start": "The First Departure",
        "Mißgeschick": "Mischance",
        "Noch einmal Mißgeschick": "Mischance Again",
        "Die dritte Fahrt": "The Third Voyage",
        "Das große Hosianna": "The Great Hosanna",
        "Das große Crucifige": "The Great *Crucifige*",
        "Sechs Jahre Schweigen": "Six Years of Silence",
    },
)
para = D.para

# ── Der neue Rhythmus ────────────────────────────────────────────────────────

para("""
Through all the thousands and perhaps hundreds of thousands of years since that singular creature called man first trod the earth, no greater measure of earthly locomotion had been known than the gallop of the horse, the rolling wheel, the rowed or sailing ship. All the abundance of technical progress within that narrow space lit by consciousness which we call world history had brought about no perceptible acceleration in the rhythm of movement. The armies of Wallenstein advanced scarcely more swiftly than the legions of Caesar, the armies of Napoleon pressed forward no more rapidly than the hordes of Genghis Khan, the corvettes of Nelson crossed the sea only a little faster than the raiding boats of the Vikings and the merchantmen of the Phoenicians. A Lord Byron on his Childe Harold voyage covers no more miles in a day than Ovid on his way into poetic exile, Goethe in the eighteenth century travels no more comfortably or speedily than the Apostle Paul at the beginning of the millennium. The countries lie as far apart from one another in space and time in the age of Napoleon as under the Roman Empire; the resistance of matter still prevails over the human will.
""", [
    note("covers no more miles",
         "Zweig moves from the past (*hatte gegolten*, *kamen*) into his habitual historical present in mid-paragraph, with Byron. The shift is his and is kept: from here the whole story is told in the present."),
    note("Genghis Khan",
         "Zweig’s *Cäsar*, *Dschingis-Khan*, *Ovidius*, *Magalhães* and *Stevenson* are given in their standard English forms (Caesar, Genghis Khan, Ovid, Magellan, Stephenson), as with the place-names (DECISION-Z03, Z04)."),
])

para("""
Only the nineteenth century fundamentally alters the measure and rhythm of earthly speed. In its first and second decades nations and countries draw closer to one another more swiftly than formerly in thousands of years; by the railway, by the steamboat, the day’s journeys of former times are accomplished in a single day, hours of travel hitherto endless in quarters of an hour and in minutes. But however triumphantly contemporaries may feel these new accelerations by the railway and the steamboat, these inventions still lie within the bounds of the comprehensible. For these vehicles only increase fivefold, tenfold, twentyfold the speeds hitherto known; the outward eye and the inward sense can still follow them and explain the apparent miracle to themselves. Wholly unforeseen in their effects, however, appear the first achievements of electricity, which, a Hercules already in the cradle, overthrows all previous laws and shatters every accepted measure. We who come later shall never be able to feel again the astonishment of that generation at the first achievements of the electric telegraph, the immense and enthusiastic amazement that the very same small, scarcely perceptible electric spark which yesterday could barely crackle an inch from the Leyden jar to the knuckle should all at once have gained the demonic power to leap over countries, mountains, and whole continents. That the thought scarcely thought to its end, the word still wet upon the page, can in the same second be received, read, and understood thousands of miles away, and that the invisible current which vibrates between the two poles of the tiny voltaic pile can be stretched across the whole earth from one end to the other. That the toy apparatus of the physics room, yesterday barely able to draw a few scraps of paper to itself by the rubbing of a glass disc, could be raised to millions and thousands of millions of times the strength and speed of human muscle, bringing messages, moving trains, lighting streets and houses, and, like Ariel, floating invisibly through the air. Only through this discovery has the relation of space and time undergone the most decisive change since the creation of the world.
""", [
    quote("a Hercules already in the cradle", "hercules-cradle-serpents",
          "The infant Hercules strangling the two serpents sent by Hera: the classical emblem of prodigious strength shown at birth."),
    note("That the thought scarcely thought to its end",
         "The two sentences beginning ‘That…’ are grammatically dependent on the ‘amazement’ of the sentence before. Zweig sets them off as free-standing exclamations; the fragments are kept rather than joined."),
    quote("like Ariel, floating invisibly through the air", "shakespeare-tempest-ariel",
          "Ariel, the airy spirit of *The Tempest*, Prospero’s invisible and instantaneous messenger. An allusion only; no line is quoted."),
    note("thousands of millions",
         "*Milliardenfachen*. ‘Thousands of millions’ is the British usage of the period for the German *Milliarde*; ‘billions’ would have been ambiguous in 1940s England."),
])

para("""
This year of world significance, 1837, when for the first time the telegraph makes simultaneous what had hitherto been isolated human experience, is seldom so much as mentioned in our school-books, which unhappily still think it more important to tell of the wars and victories of individual generals and nations than of the true triumphs of mankind, true because shared. And yet no date in modern history can be compared, in the range of its psychological effect, with this change in the value of time. The world is changed since it became possible to know in Paris, at the same moment, what is happening in Amsterdam, Moscow and Naples and Lisbon in that same minute. Only one last step remains to be taken, and then the other continents too will be drawn into that magnificent connection, and a common consciousness of all mankind created.
""", [
    note("true because shared",
         "*den wahrhaften, weil gemeinsamen Triumphen*: Zweig’s compressed antithesis between national and common history, the pacifist thread that returns in the last sentence of the piece. Kept as a pointed afterthought rather than smoothed."),
])

para("""
But Nature still resists this final union, still sets an obstacle in its way, still for two decades all those countries that are divided from one another by the sea remain cut off. For while on the telegraph poles, thanks to the insulating porcelain bells, the spark leaps onward unhindered, water draws the electric current into itself. A line through the sea is impossible so long as no means has been invented of insulating the copper and iron wires completely in the wet element.
""")

para("""
Happily, in times of progress one invention lends another a helping hand. A few years after the introduction of the land telegraph, gutta-percha is discovered to be the proper substance for insulating electric lines in water; and now a beginning can be made with joining the most important country beyond the Continent, England, to the European telegraph network. An engineer by the name of Brett lays the first cable at the very spot where Blériot, in later days, will be the first to fly across the Channel in an aeroplane. A clumsy mishap still prevents immediate success, for a fisherman at Boulogne, who thinks he has found a particularly fat eel, tears up the cable already laid. But on 13 November 1851 the second attempt succeeds. With this England is joined, and thereby Europe for the first time truly Europe, a being that lives through all the events of the age simultaneously with a single brain, a single heart.
""")

para("""
So immense a success within so few years – for what is a decade but the blink of an eye in the history of mankind? – must naturally awaken a boundless courage in that generation. Everything that is attempted succeeds, and everything with dreamlike swiftness. Only a few years, and England in its turn is joined by telegraph to Ireland, Denmark to Sweden, Corsica to the mainland, and already men are feeling their way towards bringing Egypt, and with it India, into the network. One continent, however, and the most important of all, seems condemned to permanent exclusion from this chain that is to span the world: America. For how is one to span the Atlantic Ocean or the Pacific, neither of which in its endless breadth allows of any intermediate station, with a single wire? In those childhood years of electricity all the factors are still unknown. The depth of the sea is not yet measured, the geological structure of the ocean is not yet more than vaguely known, it is still wholly untried whether a wire laid at such a depth could bear the pressure of such infinitely towering masses of water. And even were it technically possible to bed so endless a cable securely in such depths, where is there a ship of such size that it could take into itself the iron and copper burden of two thousand miles of wire? Where are the dynamos of such power that they could send an electric current unbroken across a distance which a steamer still needs at least two or three weeks to traverse? Every precondition is lacking. It is not yet known whether magnetic currents may not circle in the depths of the ocean that could deflect the electric current, there is as yet no adequate insulation, no proper measuring apparatus, as yet only the first laws are known of electricity, which has only just opened its eyes from its hundred years’ sleep of unconsciousness. ‘Impossible! Absurd!’ the learned therefore cry, vehemently waving it away, as soon as the plan of spanning the ocean is so much as mentioned. ‘Later, perhaps,’ say the boldest among the engineers. Even to Morse, the man to whom the telegraph owes its greatest perfection so far, the plan seems an incalculable hazard. But he adds prophetically that, should it succeed, the laying of the transatlantic cable would be ‘the great feat of the Century’.
""", [
    note("dynamos",
         "An anachronism of Zweig’s: the cables of the 1850s were worked by batteries and induction coils. Kept as written (DECISION-Z05)."),
    quote("‘the great feat of the Century’", "morse-great-feat",
          "Zweig quotes Morse in English and follows it with his own German gloss (*die ruhmreichste Tat des Jahrhunderts*). In English the gloss would merely repeat the quotation, so it is omitted (DECISION-Z09). Zweig’s capital C is kept."),
])

para("""
For a miracle, or anything miraculous, to be accomplished, the first precondition is always one man’s faith in that miracle. The naive courage of one who will not be taught can give the creative impulse precisely where the learned hesitate, and, as so often, here too a simple accident sets the grandiose undertaking in motion. An English engineer by the name of Gisborne, who in the year 1854 means to lay a cable from New York to the easternmost point of America, Newfoundland, so that news from the ships can be taken up a few days earlier, has to stop in the middle of the work because his funds are exhausted. So he travels to New York to find financiers there. There, by pure chance, that father of so many glorious things, he comes upon a young man, Cyrus W. Field, a clergyman’s son, who has had such great and such rapid success in business that he has already been able to retire into private life with a large fortune while still young. This idle man, too young and too energetic for lasting inactivity, Gisborne seeks to win for the completion of the cable from New York to Newfoundland. Now Cyrus W. Field – one is almost tempted to say: fortunately! – is no engineer, no expert. He understands nothing of electricity, he has never seen a cable. But the clergyman’s son has a passionate faith in his blood, the American an energetic daring. And where the professional engineer Gisborne looks only to the immediate goal of joining New York to Newfoundland, the young man, so quick to enthusiasm, at once sees farther. Why not then go straight on and join Newfoundland to Ireland by a submarine cable? And with an energy resolved to overcome every obstacle – thirty-one times in these years that man crossed the ocean and back between the two continents – Cyrus W. Field sets to work at once, iron-willed in his resolve to stake from this moment everything he has within him and about him on this deed. With this the decisive ignition has taken place by which an idea gains explosive force in reality. The new, the wonder-working electric force has allied itself with the other strongest dynamic element of life: the human will. A man has found his life’s task, and a task its man.
""", [
    note("This idle man, too young and too energetic for lasting inactivity, Gisborne seeks to win",
         "Zweig fronts the object (*Diesen Unbeschäftigten … sucht Gisborne … zu gewinnen*). The inversion is kept, as English of the period allows it and it keeps Field at the head of the sentence."),
    note("thirty-one times",
         "*einunddreißigmal*. Later (p31) Zweig has Field cross ‘for the thirtieth time’. The inconsistency is his and is kept."),
])

# ── Die Vorbereitung ─────────────────────────────────────────────────────────

para("""
With improbable energy Cyrus W. Field sets to work. He gets in touch with all the experts, besieges the governments for the concessions, conducts a campaign on both continents to raise the necessary money, and so strong is the driving force that goes out from this wholly unknown man, so compelling his inner conviction, so mighty the faith in electricity as a new miraculous power, that the founding capital of three hundred and fifty thousand pounds is fully subscribed in England within a few days. It is enough to call together the richest merchants of Liverpool, Manchester, and London to found the Telegraph Construction and Maintenance Company, and the money flows in. But the names of Thackeray and of Lady Byron, who wish to further the work with no thought of business and purely from moral enthusiasm, are also to be found among the subscribers; nothing so illustrates the optimism about everything technical and mechanical that animated England in the age of Stephenson, Brunel, and the other great engineers as that a single appeal suffices to make so enormous a sum available, *à fonds perdu*, for a wholly fantastic enterprise.
""", [
    note("Telegraph Construction and Maintenance Company",
         "Zweig’s name for the company. The company of 1856 was the Atlantic Telegraph Company; the Telegraph Construction and Maintenance Company was formed only in 1864 and made the cable of 1865–6. Kept as written (DECISION-Z05)."),
    note("*à fonds perdu*",
         "Zweig’s French (‘without hope of return’), kept and italicised under the rule for foreign fragments."),
])

para("""
For the approximate cost of laying the cable is very nearly the only thing in this undertaking that can be reliably reckoned. For the actual technical execution there is no precedent whatever. Nothing in the nineteenth century had yet been conceived and planned on comparable dimensions. For how compare this spanning of a whole ocean with the bridging of that narrow strip of water between Dover and Calais? There it had been enough to pay out thirty or forty miles from the open deck of an ordinary paddle-steamer, and the cable ran out at its leisure like the anchor from its windlass. In laying the Channel cable one could calmly wait for a particularly still day, one knew the depth of the sea-bed exactly, remained constantly within sight of one shore or the other and so beyond the reach of any dangerous accident; the connection could comfortably be made within a single day. But during a crossing that requires at the very least three weeks of continuous steaming, a coil a hundred times longer and a hundred times heavier cannot remain on open deck exposed to all the inclemencies of the weather. No ship of that time, moreover, is large enough to take this gigantic cocoon of iron, copper, and gutta-percha into its hold, none powerful enough to bear the load. Two ships at least are needed, and these principal ships must in turn be accompanied by others, so that the shortest course may be held exactly and help given in case of mishap. The English government, it is true, provides for the purpose the *Agamemnon*, one of its largest warships, which had fought as flagship before Sebastopol, and the American government the *Niagara*, a frigate of five thousand tons (at that time the most enormous dimensions). But both ships must first be specially rebuilt, so that each can stow within itself one half of the endless chain that is to bind two continents together. The chief problem, of course, remains the cable itself. Unimaginable demands are made upon this gigantic umbilical cord between two continents. For this cable must on the one hand be firm and unbreakable as a steel hawser and at the same time remain elastic, so that it can easily be paid out. It must withstand every pressure, survive every strain, and yet run off smoothly like a silken thread. It must be massive and yet not too bulky, solid on the one hand and yet on the other so exact as to let the faintest electric wave vibrate across two thousand miles. The smallest crack, the tiniest unevenness at any single point of this giant rope can destroy the transmission along this fortnight’s journey.
""", [
    note("the *Agamemnon*",
         "Zweig puts ships’ names in quotation marks (»Agamemnon«). English convention italicises them (DECISION-Z08)."),
])

para("""
But they venture it! Day and night now the factories spin, the demonic will of this one man drives every wheel onward. Whole mines of iron and copper are consumed for this one cord, whole forests of rubber trees must bleed to make the gutta-percha sheath over so vast a distance. And nothing illustrates more palpably the enormous proportions of the undertaking than that three hundred and sixty-seven thousand miles of single wire are spun into this one cable, thirteen times as much as would suffice to girdle the whole earth, and enough to join the earth to the moon in a single line. Since the building of the Tower of Babel mankind, in the technical sense, has dared nothing more grandiose.
""", [
    quote("Since the building of the Tower of Babel", "bible-genesis-11-babel",
          "Genesis 11:1–9. Zweig invokes Babel without its moral, as the first great collective work of human hands; the irony of the comparison (Babel ends in the confusion of tongues) anticipates the last sentence of the piece."),
])

# ── Der erste Start ──────────────────────────────────────────────────────────

para("""
For a year the machines hum, the wire unceasingly winds itself like a thin, flowing thread out of the factories into the bellies of the two ships, and at last, after thousands upon thousands of revolutions, one half of the cable lies coiled in each ship. Built, too, and already installed are the new, ponderous machines which, fitted with brakes and reversing gear, are to lower the cable into the depths of the ocean without a break for a week, two weeks, three weeks on end. The best electricians and engineers, Morse himself among them, are assembled on board, to check constantly with their instruments throughout the laying whether the electric current falters; reporters and draughtsmen have joined the fleet to describe with word and pen this most exciting voyage since Columbus and Magellan.
""", [
    note("with word and pen",
         "*mit Wort und Schrift*, literally ‘with word and writing’, a doublet that sits oddly with the draughtsmen. ‘Word and pen’ keeps the pairing without inventing Zweig’s probable *Wort und Bild*."),
])

para("""
At last all is ready for departure, and whereas hitherto the doubters had held the upper hand, the public interest of all England now turns passionately to the undertaking. On 5 August 1857 hundreds of little boats and ships circle the cable fleet in the little Irish harbour of Valentia, to share in the moment of world history when one end of the cable is carried ashore by boats and made fast in the firm earth of Europe. Of itself the farewell takes on the form of a great solemnity. The government has sent representatives, speeches are made, in a moving address the priest asks God’s blessing on the bold undertaking. ‘O Eternal God,’ he begins, ‘who alone spreadest out the heavens, and rulest the raging of the sea; thou whom the winds and the waves obey, look down in mercy upon thy servants . . . Lay thy command upon every hindrance, remove every obstacle that might hold us back from the accomplishment of this important work.’ And then from the shore and from the sea thousands of hands and hats wave. Slowly the land fades into dusk. One of the boldest dreams of mankind is trying to become reality.
""", [
    query("‘O Eternal God,’ he begins",
          "No English original of this prayer has been traced. It was spoken in English at Valentia in August 1857 and should survive in contemporary reports (e.g. *The Times*, or Field’s own history of the cable). Until it is found, Zweig’s German is translated fresh in the language of the Authorised Version, whose phrases it echoes: Job 9:8 (‘which alone spreadeth out the heavens’), Psalm 89:9 (‘thou rulest the raging of the sea’), Matthew 8:27 (‘even the winds and the sea obey him’). Please check."),
])

# ── Mißgeschick ──────────────────────────────────────────────────────────────

para("""
Originally it had been planned that the two great ships, the *Agamemnon* and the *Niagara*, each of which carries one half of the cable, should sail together to a point calculated in advance in the middle of the ocean, and that only there should the two halves be joined. Then the one ship was to steer west towards Newfoundland, the other east towards Ireland. But it seemed too rash to hazard the whole precious cable on this first attempt at once; and so it was thought better to lay the first stretch from the mainland, so long as it was not yet certain whether submarine telegraphic transmission over such distances would work properly at all.
""")

para("""
Of the two ships, the task has fallen to the *Niagara* of laying the cable from the mainland to the middle of the sea. Slowly, cautiously, the American frigate steers onward, like a spider continually leaving the thread behind it out of its enormous body. Slowly, regularly, the paying-out machine rattles on board – it is the old sound, familiar to every seaman, of an anchor cable running down off the windlass. And after a few hours the men on board pay no more heed to this regularly grinding noise than to the beating of their own hearts.
""")

para("""
On, on, farther out to sea, constantly, constantly the cable going down behind the keel. Not in the least adventurous does this adventure seem. Only in a special cabin the electricians sit and listen, constantly exchanging signals with the Irish mainland. And wonderful to tell: although the coast has long since passed from sight, transmission over the submarine cable works as clearly as if one were communicating from one European city to another. Already the shallow waters are left behind, already the so-called deep-sea plateau that rises beyond Ireland is partly crossed, and still the metal cord runs down behind the keel as regularly as sand from the hour-glass, at once giving and receiving messages.
""", [
    note("Not in the least adventurous does this adventure seem",
         "*Gar nicht abenteuerlich scheint dieses Abenteuer*: the inversion is kept to preserve the play of *abenteuerlich* and *Abenteuer*."),
])

para("""
Already three hundred and thirty-five miles have been laid, more, that is, than ten times the distance from Dover to Calais, already five days, five nights of first uncertainty have been survived, already on the sixth evening, 11 August, Cyrus W. Field, after many hours of work and excitement, takes to his bed for a well-earned rest. Then suddenly – what has happened? – the rattling noise stops. And as a sleeper starts up in a moving train when the engine unexpectedly halts, as the miller starts awake in his bed when the mill-wheel suddenly stands still, so in an instant everyone on the ship is awake and rushes on deck. The first glance at the machine shows: the paying-out gear is empty. The cable has suddenly slipped from the winch; it was impossible to catch the torn end in time, and still more impossible is it now to find the lost end in the depths and haul it up again. The dreadful thing has happened. A small technical fault has destroyed the work of years. As vanquished men those who set out so boldly return to England, where the sudden silence of all signs and signals has already prepared people for bad news.
""")

# ── Noch einmal Mißgeschick ──────────────────────────────────────────────────

para("""
Cyrus Field, the one man unshaken, hero and merchant at once, draws up the balance. What has been lost? Three hundred miles of cable, some hundred thousand pounds of the share capital and, what perhaps weighs on him still more, a whole, an irreplaceable year. For only in summer can the expedition hope for favourable weather, and this time the season is already too far advanced. On the other side of the ledger stands a small gain. A good deal of practical experience has been won in this first attempt. The cable itself, which has proved serviceable, can be wound up and stowed for the next expedition. Only the paying-out machines, which were to blame for the fatal break, have to be altered. So another year passes in waiting and preparation. Not until 10 June 1858 can the same ships put out again, with fresh courage and laden with the old cable. And since the electrical transmission of signals worked without fault on the first voyage, they have gone back to the old plan of beginning the laying from the middle of the ocean towards both sides. The first days of this new voyage pass without event. Only on the seventh day, after all, is the laying, and with it the real work, to begin at the point calculated in advance. Until then everything is, or seems, a pleasure cruise. The machines stand idle, the sailors can still rest and enjoy the friendly weather, the sky is cloudless and the sea still, perhaps all too still.
""", [
    note("On the other side of the ledger",
         "*Auf dem andern Blatt*, literally ‘on the other page’. The book-keeping image follows from ‘draws up the balance’ (*macht Bilanz*) and from ‘hero and merchant at once’."),
])

para("""
But on the third day the captain of the *Agamemnon* feels a secret unease. A glance at the barometer has shown him with what alarming speed the column of mercury is falling. A storm of a particular kind must be approaching, and indeed on the fourth day a gale breaks loose such as even the most seasoned sailors have seldom known on the Atlantic. This hurricane strikes most fatefully of all the English cable ship, the *Agamemnon*. In herself an excellent vessel, which had stood the hardest tests on every sea and in war as well, the flagship of the English navy ought to be equal even to this foul weather. But unhappily the ship has been entirely rebuilt for the cable-laying, so as to be able to hold the enormous load. It was not possible here, as in a cargo ship, to distribute the weight evenly over the hold on every side; instead the whole weight of the enormous coil bears down in the middle, and only a part has been stowed right forward, which has the still worse consequence that with every rise and fall the pendulum swing is doubled. So the storm can play the most dangerous game with its victim; to right and to left, fore and aft, the ship is heaved up to an angle of forty-five degrees, breakers flood the deck, everything is smashed. And a fresh calamity – at one of the most terrible shocks, which shake the ship from keel to masthead, the bunker of coal heaped upon the deck gives way. In a black hail the whole mass crashes like a fall of rock upon the sailors, already bleeding and exhausted. Some are injured in the fall, others scalded in the galley by the overturning coppers. One sailor goes mad in the ten days’ storm, and already there is thought of the last resort: throwing part of the fatal cable load overboard. Fortunately the captain is unwilling to take this responsibility upon himself, and he is proved right. After unspeakable trials the *Agamemnon* survives the ten days’ storm and, though badly delayed, is able to find the other ships again at the agreed place in the middle of the ocean where the cable-laying is to begin.
""", [
    note("the overturning coppers",
         "*Kessel* in the galley: the great cooking cauldrons, called ‘coppers’ at sea, not the ship’s boilers."),
])

para("""
But only now does it appear how badly the precious and delicate freight of wires, a thousandfold entwined, has suffered from the incessant pitching. In some places the strands have become tangled, the gutta-percha sheath is chafed or torn. With little confidence a few attempts are made to lay the cable nevertheless, but they produce only the loss of some two hundred miles of cable, which vanish uselessly in the sea. For the second time the flag must be struck, and they return home without glory instead of in triumph.
""")

# ── Die dritte Fahrt ─────────────────────────────────────────────────────────

para("""
With pale faces, already informed of the bad news, the shareholders in London await their leader and misleader, Cyrus W. Field. Half the share capital has been squandered on these two voyages and nothing proved, nothing achieved; one can understand that most of them now said: Enough! The chairman advises that they should save what could be saved. He would vote for taking the rest of the unused cable off the ships and selling it, at a loss if need be, but then drawing a line under this wild plan of spanning the ocean. The vice-chairman supports him and sends in his resignation in writing, to make it plain that he wishes to have nothing further to do with this absurd undertaking. But the tenacity and idealism of Cyrus W. Field are not to be shaken. Nothing is lost, he declares. The cable itself has stood the test brilliantly, and there is enough still on board to renew the attempt; the fleet is assembled, the crews engaged. The very unusual storm of the last voyage now gives hope of a spell of fine, windless days. Only courage, courage once more! Now or never is the chance to venture the last.
""", [
    note("leader and misleader",
         "*Führer und Verführer*: the rhyme on the simple and prefixed noun is reproduced."),
])

para("""
Ever more uncertainly the shareholders look at one another: are they to entrust the last of the paid-up capital to this fool? But since a strong will in the end always carries the hesitant along with it, Cyrus W. Field forces through the new departure. On 17 July 1858, five weeks after the second unlucky voyage, the fleet leaves the English harbour for the third time.
""")

para("""
And now the old experience is confirmed once more, that the decisive things almost always succeed in secret. This time the departure takes place wholly unnoticed; no boats, no barques circle the ships with good wishes, no crowd gathers on the shore, no festive farewell dinner is given, no speeches are made, no priest calls down the aid of God. As though bound on a piratical enterprise, shyly and silently, the ships put out. But the sea awaits them kindly. Precisely on the appointed day, 28 July, eleven days after leaving Queenstown, the *Agamemnon* and the *Niagara* are able to begin the great work at the appointed place in the middle of the great ocean.
""")

para("""
A strange spectacle – stern to stern the ships turn towards each other. Between them the ends of the cable are now joined. Without any formality, indeed without the men on board even paying the proceedings any great attention (they are already so worn out by the unsuccessful attempts), the iron and copper rope sinks between the two ships into the deep, down to the lowest floor of the ocean, never yet sounded by any lead. Then one more greeting from deck to deck, from flag to flag, and the English ship steers for England, the American for America. As they draw away from each other, two wandering points in the endless ocean, the cable keeps them constantly connected – for the first time since the memory of man two ships can speak with each other across wind and wave and space and distance, invisibly. Every few hours the one reports by electric signal from the depths of the ocean the miles it has covered, and each time the other confirms that it too, thanks to the excellent weather, has made the same distance. So passes one day and a second, a third, a fourth. On 5 August the *Niagara* can at last report that she sees the American coast before her in Trinity Bay, Newfoundland, after laying no less than one thousand and thirty miles of cable, and the *Agamemnon*, which has likewise bedded some thousand miles safely in the deep, can triumph in turn that she has the Irish coast in sight. For the first time the human word now passes from land to land, from America to Europe. But only these two ships, the few hundred men in their wooden shells, know that the deed is done. The world does not yet know it, having long since forgotten this adventure. No one awaits them on the shore, not in Newfoundland, not in Ireland: but in the one second in which the new ocean cable is joined to the land cable, all mankind will know of its tremendous common victory.
""")

# ── Das große Hosianna ───────────────────────────────────────────────────────

para("""
Precisely because this flash of joy comes down out of a perfectly clear sky, it kindles so tremendously. Almost in the same hour, in the first days of August, the old and the new continent learn the news of the work accomplished; the effect is indescribable. In England the usually so deliberate *Times* writes in a leading article: ‘Since the discovery of Columbus, nothing has been done in any degree comparable to the vast enlargement which has thus been given to the sphere of human activity.’ And the City is in the liveliest excitement. But shadowy and shy this proud joy of England seems, compared with the hurricane of enthusiasm in America, as soon as the news is transmitted there. At once business comes to a standstill, the streets are flooded with people asking, clamouring, debating. Overnight a wholly unknown man, Cyrus W. Field, has become the national hero of an entire people. He is emphatically set beside Franklin and Columbus; the whole city, and behind it a hundred others, quakes and resounds with the eagerness to see the man who by his resolution has consummated ‘the marriage of young America and the Old World’. But the enthusiasm has not yet reached its highest pitch, for so far nothing has arrived but the bare report that the cable is laid. But can it also speak? Has the deed, the real deed, succeeded? A grandiose spectacle – a whole city, a whole country waits and listens for a single word, for the first word across the ocean. It is known that the Queen of England will be the first of all to send her message, her congratulations; every hour it is awaited more impatiently. But days and days go by, because by an unlucky chance it is just the cable to Newfoundland that is out of order, and it is not until 16 August that Queen Victoria’s message reaches New York, in the evening hours.
""", [
    quote("‘Since the discovery of Columbus", "times-1858-columbus",
          "Zweig quotes *The Times* in English and then translates it into German. The English is given once, as Zweig gives it; the German repetition is omitted (DECISION-Z09)."),
    note("‘the marriage of young America and the Old World’",
         "Zweig quotes this phrase in German, presumably from the American press of August 1858. No English original has been traced, so it is translated fresh."),
    note("for the first word across the ocean",
         "The title phrase (*das erste Wort über den Ozean*) arrives here, two-thirds of the way through; the English title is chosen so that the two coincide."),
])

para("""
The longed-for news comes too late, of course, for the newspapers to print the official text; it can only be posted up at the telegraph offices and newspaper offices, and immense crowds at once mass before them. Bruised, their clothes torn, the newspaper boys have to fight their way through the throng. In the theatres, in the restaurants the message is proclaimed. Thousands who cannot yet grasp that the telegraph outruns the fastest ship by days storm down to the harbour at Brooklyn to greet the heroic ship of this peaceful victory, the *Niagara*. The next day, 17 August, the newspapers rejoice in headlines as thick as a fist: ‘The cable in perfect working order’, ‘Everybody crazy with joy’, ‘Tremendous Sensation throughout the city’, ‘Now’s the time for an universal jubilee’. Triumph without equal: since the beginning of all thought on earth, a thought has swung across the ocean at its own speed. And already a hundred guns thunder from the Battery to announce that the President of the United States has answered the Queen. Now no one any longer dares to doubt; in the evening New York and all the other cities blaze with tens of thousands of lights and torches. Every window is illuminated, and it scarcely spoils the joy that the dome of the City Hall catches fire in the process. For the very next day brings a new festival. The *Niagara* has arrived; Cyrus W. Field, the great hero, is here! In triumph the remainder of the cable is carried through the city and the crew are feasted. Day after day now, in every city from the Pacific Ocean to the Gulf of Mexico, the demonstrations are repeated, as though America were celebrating for the second time the festival of its discovery.
""", [
    note("The longed-for news comes too late",
         "Zweig holds the subject to the end (*Zu spät freilich … kommt die ersehnte Nachricht*). Reproduced in English the inversion sounds like costume prose, so the sentence is recast in normal order: the one deliberate departure from the periodic-sentence rule in this piece."),
    note("‘Now’s the time for an universal jubilee’",
         "The headlines are in English in Zweig and are kept exactly as he gives them, including ‘an universal’ and the capitals."),
])

para("""
But still it is not enough, not nearly enough! The true triumphal procession is to be grander still, the most magnificent the new continent has ever seen. The preparations take two weeks, but then, on 31 August, a whole city celebrates a single man, Cyrus W. Field, as scarcely any victor has been celebrated by his people since the days of the emperors and the Caesars. On this glorious autumn day a procession is made ready so long that it needs six hours to pass from one end of the city to the other. The regiments march ahead with banners and flags through the beflagged streets, the musical societies, the glee clubs, the choral unions, the fire brigades, the schools, the veterans follow in an endless train. Everyone who can march marches, everyone who can sing sings, everyone who can cheer cheers. In a carriage and four, like a triumphant general of antiquity, Cyrus W. Field is driven along, in another the commander of the *Niagara*, in a third the President of the United States; the mayors, the officials, the professors behind. Speeches, banquets, torchlight processions follow one another without a pause, the church bells ring, the cannon thunder, again and again the cheering surges round the new Columbus, the uniter of the two worlds, the conqueror of space, the man who in this hour has become the most famous and most idolised man in America, Cyrus W. Field.
""", [
    note("But still it is not enough, not nearly enough!",
         "*Aber noch nicht genug und genug!* An idiomatic intensifying doubling, rendered by repetition rather than literally."),
    note("the glee clubs",
         "*Liedertafeln* and *Sängerbünde*: the German male-voice choirs, which were in fact numerous in New York in 1858. Given their English equivalents rather than kept in German, since they are ordinary German nouns in Zweig, not foreign fragments."),
])

# ── Das große Crucifige ──────────────────────────────────────────────────────

para("""
Thousands and millions of voices clamour and cheer on this day. Only one, and the most important, remains strangely dumb throughout the celebration – the electric telegraph. Perhaps in the midst of the cheering Cyrus W. Field already suspects the terrible truth, and how horrible it must be for him to be the only one to know that on this very day the Atlantic cable has ceased to work, that after only confused and scarcely legible signals had come through in the last few days, the wire has finally rattled out its life and drawn its last, dying breath. Of this gradual failure no one in all America yet knows or suspects anything except the few men who check the reception of messages in Newfoundland, and even they hesitate for days and days, in the face of the boundless enthusiasm, to give the rejoicing crowds the bitter news. Soon, however, it is noticed that the messages arrive so sparsely. America had expected that now, hour after hour, tidings would flash across the ocean – instead only now and then some vague and unverifiable report. Before long a rumour is whispered about that in their zeal and impatience to obtain better transmission they had sent too strong electric charges and so ruined the cable, inadequate as it was. There is still hope of remedying the fault. But soon it can no longer be denied that the signals have grown ever more stammering, ever more unintelligible. Just after that morning-after of the festival, on 1 September, no clear tone, no pure vibration comes across the sea any more.
""", [
    note("that morning-after of the festival",
         "*katzenjämmerlichen Festmorgen*: *Katzenjammer* is the hangover, and Zweig means both the city’s and the cable’s. ‘Morning-after’ keeps the double sense."),
])

para("""
Now there is nothing people forgive less than to be sobered in an honest enthusiasm and to see themselves treacherously disappointed by a man from whom they had expected everything. Scarcely has the rumour proved true that the much-vaunted telegraph has failed than the stormy wave of jubilation, recoiling, hurls itself as malignant bitterness against the guiltless culprit, Cyrus W. Field. He has deceived a city, a country, a world; he had known long since of the failure of the telegraph, it is asserted in the city, but selfishly he had let himself be fêted and meanwhile used the time to sell off his own shares at an enormous profit. Even more malignant slanders appear, among them the strangest of all, which asserts peremptorily that the Atlantic telegraph had never worked properly at all; all the reports had been swindle and humbug, and the Queen of England’s telegram composed beforehand and never sent by the ocean telegraph. Not a single message, the rumour runs, had in all that time really come across the sea intelligibly, and the directors had merely brewed up imaginary dispatches out of guesses and broken signals. A real scandal breaks out. Precisely those who yesterday had cheered the loudest now rage the most. A whole city, a whole country is ashamed of its overheated and premature enthusiasm. Cyrus W. Field is chosen as the victim of this anger; he who only yesterday was held a national hero and demigod, the brother of Franklin and the descendant of Columbus, must hide from his former friends and admirers like a criminal. A single day has made everything, a single day has destroyed everything. Immeasurable is the defeat, lost the capital, squandered the confidence, and like the legendary Midgard Serpent the useless cable lies in the unfathomable depths of the ocean.
""", [
    note("the guiltless culprit",
         "*dem unschuldig Schuldigen*: Zweig’s oxymoron, kept."),
    quote("like the legendary Midgard Serpent", "edda-midgard-serpent",
          "Jörmungandr, the serpent of Norse myth that lies coiled round the world at the bottom of the sea, tail in mouth: an exact image for a cable lying round half the globe on the ocean floor."),
])

# ── Sechs Jahre Schweigen ────────────────────────────────────────────────────

para("""
For six years the forgotten cable lies useless in the ocean, for six years the old, cold silence reigns again between the two continents which for one hour of world history had beaten pulse to pulse. America and Europe, which had been close for the space of a breath, of a few hundred words, are again divided, as for thousands of years, by an insurmountable distance. The boldest plan of the nineteenth century, yesterday all but a reality, has become once more a legend, a myth. Naturally no one thinks of renewing the half-successful work; the terrible defeat has paralysed all energies, stifled all enthusiasm. In America the Civil War between the North and the South diverts all interest, in England committees still sit now and then, but they need two years to establish laboriously the bare assertion that a submarine cable would be possible in principle. But from this academic opinion to the actual deed is a road that no one thinks of treading; for six years all work rests as completely as the forgotten cable on the floor of the sea.
""", [
    note("the Civil War between the North and the South",
         "Zweig writes *zwischen Nord- und Südamerika*, ‘between North and South America’, a plain slip. Rendered as he must have meant it, on the same footing as the silent correction of misspelt names (DECISION-Z03)."),
])

para("""
But six years, though only a fleeting moment within the vast space of history, mean a thousand years in so young a science as electricity. Every year, every month brings new discoveries in this field. Ever more powerful, ever more precise become the dynamos, ever more manifold their application, ever more exact the instruments. Already the telegraph network spans the interior of every continent, already the Mediterranean is crossed, already Africa and Europe are joined; and so from year to year the plan of spanning the Atlantic Ocean imperceptibly loses more and more of the fantastic that had clung to it so long. Inevitably the hour must come that renews the attempt; all that is lacking is the man to pour new energy into the old plan.
""")

para("""
And suddenly the man is there, and behold, it is the old one, the same, with the same faith and the same confidence, Cyrus W. Field, risen again from silent banishment and spiteful contempt. For the thirtieth time he has crossed the ocean, and he appears again in London; he succeeds in furnishing the old concessions with a new capital of six hundred thousand pounds. And now at last the long-dreamed-of giant ship is at hand that can take the enormous freight into itself alone, the famous *Great Eastern*, with her twenty-two thousand tons and four funnels, built by Isambard Brunel. And wonder upon wonder: in this year, 1865, she lies idle, because she too was planned too boldly ahead of her time; within two days she can be bought and fitted out for the expedition.
""", [
    note("risen again",
         "*auferstanden*. With the section titles ‘The Great Hosanna’ and ‘The Great *Crucifige*’ (‘Crucify him!’, John 19:6 in the Vulgate), Zweig lays the shape of the Passion over Field’s story: Palm Sunday, Good Friday, Resurrection. *Crucifige* is kept in Latin as a foreign fragment; ‘risen’ is chosen for its Easter sense."),
    note("Isambard Brunel",
         "Zweig writes *Isambar*. Corrected silently (DECISION-Z03). The *Great Eastern* in fact had five funnels; Zweig’s four is kept (DECISION-Z05)."),
])

para("""
Now everything is easy that before was immeasurably hard. On 23 July 1865 the mammoth ship leaves the Thames with a new cable. Even though the first attempt fails, even though two days from the goal the laying miscarries through a break and the insatiable ocean once more swallows six hundred thousand pounds sterling, engineering is by now too sure of its business to be discouraged. And when on 13 July 1866 the *Great Eastern* sets out for the second time, the voyage becomes a triumph; clear and distinct, this time, the cable speaks across to Europe. A few days later the old, lost cable is found; two strands now bind the Old and the New World into one common world. The miracle of yesterday has become the commonplace of today, and from this moment the earth has, as it were, a single heartbeat; hearing itself, seeing itself, understanding itself, mankind now lives simultaneously from one end of the earth to the other, divinely omnipresent through its own creative power. And it would now be gloriously united for all time thanks to its victory over space and time, were it not confounded again and again by the fatal delusion of ceaselessly destroying this grandiose unity and of annihilating itself with the very means that have given it power over the elements.
""", [
    note("the old, lost cable is found",
         "The cable recovered and completed in 1866 was the broken cable of 1865, not that of 1858. Kept as Zweig wrote it (DECISION-Z05)."),
    note("were it not confounded again and again",
         "The closing conditional (*herrlich wäre sie … verwirrte sie nicht*) is kept as one sentence ending on ‘the elements’. *verwirrte* (‘confounded’) recalls Babel (p10), where the Lord confounded the language of the builders."),
])

D.library = [
    {"id": "hercules-cradle-serpents", "type": "allusion", "author": "Classical myth",
     "work": "The infant Hercules and the serpents", "locus": "Pindar, *Nemean* I; Theocritus, *Idyll* 24",
     "original_language": "grc", "original": "(the infant Hercules strangles two serpents)",
     "zweig_rendering": "ein Herkules schon in der Wiege",
     "english_used": "a Hercules already in the cradle",
     "english_provenance": "Fresh translation of Zweig; allusion only", "used_in": ["first-word-across-the-ocean-p02"]},
    {"id": "shakespeare-tempest-ariel", "type": "allusion", "author": "William Shakespeare",
     "work": "The Tempest", "locus": "passim", "original_language": "en",
     "original": "(Ariel, Prospero’s spirit of the air)",
     "zweig_rendering": "wie Ariel unsichtbar die Luft durchschwebend",
     "english_used": "like Ariel, floating invisibly through the air",
     "english_provenance": "Fresh translation of Zweig; allusion only", "used_in": ["first-word-across-the-ocean-p02"]},
    {"id": "morse-great-feat", "type": "quotation", "author": "Samuel F. B. Morse",
     "work": "(attributed remark on the Atlantic cable)", "locus": "untraced",
     "original_language": "en", "original": "the great feat of the Century",
     "zweig_rendering": "»the great feat of the Century«, die ruhmreichste Tat des Jahrhunderts",
     "english_used": "the great feat of the Century",
     "english_provenance": "As quoted in English by Zweig; original source not traced", "used_in": ["first-word-across-the-ocean-p06"]},
    {"id": "bible-genesis-11-babel", "type": "allusion", "author": "Bible", "work": "Genesis",
     "locus": "11:1–9", "original_language": "de", "original": "(the Tower of Babel)",
     "zweig_rendering": "Seit dem Turmbau von Babel",
     "english_used": "Since the building of the Tower of Babel",
     "english_provenance": "Standard English name of the episode (Authorised Version)", "used_in": ["first-word-across-the-ocean-p10", "first-word-across-the-ocean-p32"]},
    {"id": "valentia-prayer-1857", "type": "quotation", "author": "Unnamed clergyman at Valentia",
     "work": "Prayer at the departure of the cable fleet", "locus": "5 August 1857",
     "original_language": "en", "original": "(English original not yet traced)",
     "zweig_rendering": "O ewiger Gott, der du allein die Himmel ausbreitest …",
     "english_used": "O Eternal God, who alone spreadest out the heavens …",
     "english_provenance": "Fresh translation in Authorised Version idiom (Job 9:8, Psalm 89:9, Matthew 8:27); QUERY open", "used_in": ["first-word-across-the-ocean-p12"]},
    {"id": "times-1858-columbus", "type": "quotation", "author": "The Times (leading article)",
     "work": "The Times, London", "locus": "August 1858", "original_language": "en",
     "original": "Since the discovery of Columbus, nothing has been done in any degree comparable to the vast enlargement which has thus been given to the sphere of human activity.",
     "zweig_rendering": "(quoted in English, then translated into German)",
     "english_used": "Since the discovery of Columbus, nothing has been done in any degree comparable to the vast enlargement which has thus been given to the sphere of human activity.",
     "english_provenance": "As quoted in English by Zweig; date of the leader to be verified", "used_in": ["first-word-across-the-ocean-p24"]},
    {"id": "edda-midgard-serpent", "type": "allusion", "author": "Snorri Sturluson",
     "work": "Prose Edda (Gylfaginning)", "locus": "ch. 34", "original_language": "non",
     "original": "(Jörmungandr, the World Serpent, lying in the ocean round the earth)",
     "zweig_rendering": "wie die sagenhafte Midgardschlange",
     "english_used": "like the legendary Midgard Serpent",
     "english_provenance": "Standard English name", "used_in": ["first-word-across-the-ocean-p28"]},
]
