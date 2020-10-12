from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

current_id = 31
lastSearch = ""
meta = []
pokemon = [
    {
    "id":1,
    "name":"Bulbasaur",
    "picture":"https://vignette.wikia.nocookie.net/pokemon/images/2/21/001Bulbasaur.png/revision/latest?cb=20140328190757",
    "description":'''Bulbasaur resembles a small, squatting dinosaur that
                walks on four legs, but bears three claws on each of its
                feet and has no tail. It also has large, red eyes and very
                sharp teeth. Its skin is a light, turquoise color with dark,
                green spots. It has three claws on all four of its legs.
                Its most notable feature, however, is the aforementioned
                bulb on its back, which according to its entry in the
                Pokédex, was planted there at birth. Bulbasaur has a
                bulb on its back that grows steadily larger as it matures.
                This bulb contains a seed which uses photosynthesis to supply
                Bulbasaur with energy. Its bulb is also used to store the energy
                that the seed absorbs, which can be used when it is necessary.
                It is assumed that when a Bulbasaur collects enough energy in
                its bulb, it will evolve into an Ivysaur. Bulbasaur often rests
                in bright places so its bulb can absorb sunlight.
                It can be seen napping in bright sunlight.
                While it sleeps, the seed on its back catches the rays and
                uses the energy to grow.''',
    "Pokedex":"001",
    "Abilities": [{"name":"Overgrow", "delete":False}, {"name":"Chlorohyll", "delete":False}]
    },
    {
    "id":2,
    "name":"Charmander",
    "picture":"https://vignette.wikia.nocookie.net/pokemon/images/7/73/004Charmander.png/revision/latest?cb=20140724195345",
    "description":'''Charmander is a small, bipedal, dinosaur-like Pokémon.
                Most of its body is colored orange, while its underbelly
                is a pale light-yellow color. Charmander, like its
                evolved forms, has a flame that constantly burns on the
                end of its tail. However, If the flame on Charmander's
                tail goes out, Charmander is known to die.
                The power of its flame attacks can be gauged by the
                size of the flame on its tail. Charmander is easily
                the most mild-mannered and well-behaved of its evolution line.
                Its feelings and emotions can be read by the flame on the
                tip of its tail. It flares up in a fury when Charmander
                is angry. If it growls that means it's angry or is about
                to attack. Charmander doesn't do well with impatient people.
                It doesn't appreciate being rushed, and most of the time,
                will not allow it. It is a sweet Pokémon, but is feisty
                nonetheless. Charmander doesn't enjoy accepting favors,
                because it feels it owes something in return. It is extremely
                loyal to its loved ones, and knows a good thing when it sees it.
                It will treat those in its life accordingly. Charmander is
                rarely found in the wild since it's a Starter Pokémon.
                Sometimes they gather in extremely hot areas such as active
                volcanoes or in craggy mountains and in caves along the coast
                of the Sevii Islands.''',
    "Pokedex":"004",
    "Abilities": [{"name":"Blaze", "delete":False}, {"name":"Solar Power", "delete":False}]
    },
    {
    "id":3,
    "name":"Squirtle",
    "picture":"https://vignette.wikia.nocookie.net/pokemon/images/3/39/007Squirtle.png/revision/latest?cb=20140328191525",
    "description":'''Squirtle is a small, light-blue Pokémon with an
                appearance similar to a turtle. With its aerodynamic
                shape and grooved surface, Squirtle's shell helps it wade
                through the water very quickly. It also offers protection
                in battle. Like turtles, Squirtle has a shell that covers
                its body with holes that allow its limbs, tail, and head to
                be exposed. Unlike a turtle, Squirtle is ordinarily bipedal.
                Its shell is highly sturdy, and it can hide within its shell
                to protect itself from physical attacks. Squirtle is usually
                well behaved, yet it has an underlying rebellious streak.
                It likes to be open with only a limited number of people
                and won’t advertise its secrets. It prefers to stay within
                a close knit group, but can still enjoy making new friends.
                Other Pokémon may regard it as difficult and hard to get
                along with, but only if they have previously gotten on its
                bad side.''',
    "Pokedex":"007",
    "Abilities": [{"name":"Torrent", "delete":False}, {"name":"Rain Dish", "delete":False}]
    },
    {
    "id":4,
    "name":"Caterpie",
    "picture":"https://vignette.wikia.nocookie.net/pokemon/images/5/5d/010Caterpie.png/revision/latest?cb=20140328191737",
    "description":'''Caterpie is a worm-like Pokémon that is mainly green
                in color with a tan underside. Just below its head are
                four, tiny legs that are used only for movement. On top
                of its head is a red, "y-shaped" antenna, which can be
                used to produce an odor used in self-defense, in case
                something tries to hurt it. Caterpie has the ability
                Shield Dust, which negates all status effects that are
                side effects of other moves. When threatened, it can release
                a strong odor from its antenna, which it uses to ward off
                predators. A ravenous Caterpie can quickly gobble up leaves
                that are much bigger than itself. Caterpie evolves into
                Metapod starting at level 7, which evolves into Butterfree
                starting at level 10.''',
    "Pokedex":"010",
    "Abilities": [{"name":"Shield Dust", "delete":False}, {"name":"Run Away", "delete":False}]
    },

    {
    "id":5,
    "name":"Weedle",
    "picture":"https://vignette.wikia.nocookie.net/pokemon/images/d/df/013Weedle.png/revision/latest?cb=20140328191838",
    "description":'''Weedle is a small, insect-like Pokémon appearing
                as a brown caterpillar with large stingers on both
                its tail and head. Across Weedle's underside are small,
                pink nubs which it uses to move. On its head, Weedle has
                two beady, black eyes above a large, pink nose. Weedle
                has the ability Shield Dust, which will block any side
                effect caused by an opposing attack. With its great scent
                it can smell the leaves it likes best. Weedle's sense of
                smell is excellent. With its large red nose, it can sniff
                out the leaves it likes best. Weedle has a large stinger
                on its head. This stinger, according to the Pokédex,
                measures around two inches and is very toxic.
                Furthermore, the Pokédex states that Weedle is
                brightly colored, so as to ward off any potential
                predators. Weedle evolves into Kakuna once it reaches
                level 7, which can then further evolve at level 10 into
                Beedrill.''',
    "Pokedex":"013",
    "Abilities": [{"name":"Shield Dust", "delete":False}, {"name":"Run Away", "delete":False}]
    },
    {
    "id":6,
    "name":"Pidgey",
    "picture":"https://vignette.wikia.nocookie.net/pokemon/images/5/55/016Pidgey.png/revision/latest?cb=20140328192030",
    "description":'''Pidgey resembles a small, plump-bodied bird.
                It is brown in color, with a cream-colored throat
                and belly. The tips of its wings share the same color.
                Both its feet and beak are a pinkish-gray color.
                Its plumage is fairly nondescript, particularly compared
                to its evolutions, Pidgeotto and Pidgeot. It has black
                markings around its eyes and a small crest of brown and
                cream feathers above its eyes. It resembles other small
                flying-type Pokémon, such as Starly, Taillow, and Spearow.
                However, due to the fact that this Pokémon tend to be
                unique to a region, with the exception of Spearow, it is
                likely that they are a result of convergent evolution.
                When on the ground, Pidgey flaps its wings to kick up
                sand and dust that blinds its opponents. It has an
                excellent sense of direction and homing instincts. It
                can locate its nest even when far removed from familiar
                surroundings. These skills enable it to be easily trained
                to deliver messages. Pidgey are shown to be prey for
                Pokémon such as Meowth. Their eggs are often the victim
                of hungry Ekans. Pidgey evolves into Pidgeotto starting
                at level 18, and from Pidgeotto, evolves into Pidgeot
                starting at level 36.''',
    "Pokedex":"016",
    "Abilities": [{"name":"Keen Eye", "delete":False}, {"name":"Tangled Feet", "delete":False}, {"name":"Big Pecks", "delete":False}]
    },
    {
    "id":7,
    "name":"Rattata",
    "picture":"https://vignette.wikia.nocookie.net/pokemon/images/4/46/019Rattata.png/revision/latest?cb=20140328192134",
    "description":'''Rattata is mouse-like, with large incisors and
                a whisker on both sides. Female Rattata have shorter
                whiskers than the males. The fur of a normal variant
                is purple, with a white or cream colored underside:
                the fur of an Alolan variant is black with dark cram
                underside. Rattata have red eyes, with no obvious pupils.
                The tail is long, and curled slightly at the tip. Rattata
                have three-toed paws, which are the same color as its
                underbelly. Rattata's teeth grow very quickly and they
                can survive almost anywhere. It's happy to nest just
                about anywhere. They also utilize their teeth so they
                can use attacks such as Super Fang and Bite.
                Rattata is always on the alert. Even while asleep,
                Rattata constantly moves its ears to listen around.
                Rattata evolves into Raticate starting at level 20.''',
    "Pokedex":"019",
    "Abilities": [{"name":"Run Away", "delete":False}, {"name":"Guts", "delete":False}, {"name":"Hustle", "delete":False}]
    },
    {
    "id":8,
    "name":"Spearow",
    "picture":"https://vignette.wikia.nocookie.net/pokemon/images/8/8b/021Spearow.png/revision/latest?cb=20140328192232",
    "description":'''Spearow are an avian species of Pokémon
                characterized by its short stature, brown body, and
                pale red wings. Its underbelly is beige while possessing
                a dark brown plumage on its head. Spearow's rear is black
                and its tail feathers are a shade of brown. Like all
                birds, it is equipped with talons used for manipulating
                objects or self-defense. They are noted for being frail,
                for which they make up for with their "Mirror Move"
                ability. Eggs laid by Spearow are known to be prey for
                hungry Ekans, which are known to be able to swallow them
                whole. Spearow prey on insects, and sometimes Sunkern,
                in grassy areas by flushing them out with their stubby
                wings, and plucking at them with their beaks. Spearow
                are very territorial, constantly buzzing about and
                calling with a loud cry that can be heard from half a
                mile away. This cry serves to scare away predators and
                to keep in touch with other Spearow, though the latter
                is reserved as an alarm to its kind.''',
    "Pokedex":"021",
    "Abilities": [{"name":"Keen Eye", "delete":False}, {"name":"Sniper", "delete":False}]
    },
    {
    "id":9,
    "name":"Ekans",
    "picture":"https://vignette.wikia.nocookie.net/pokemon/images/f/fa/023Ekans.png/revision/latest?cb=20140328192338",
    "description":'''Ekans is a snake-like Pokémon with purple and
                yellow coloring. Its underside leading to its tail
                is yellow, and it has a yellow rattle at the tip of
                its tail. Ekans have large, yellow eyes with slit,
                reptilian pupils. Across its neck is a large, yellow band.
                Ekans, like real snakes, have the ability to unhinge
                their jaws. Ekans also share other characteristics with
                snakes, such as using its tongue to test the air for the
                presence of prey and shedding its skin. An Ekans will
                lose its rattle once it evolves into Arbok. Ekans often
                live in tall grassy areas where they slither with great
                stealth. Ekans is also known to prey on Pokémon such as
                Pidgey, Spearow, and their eggs. Though often associated
                as a land Pokémon, they are capable of swimming long
                distances. When threatened in the wild, it will rattle
                its tail, flick its tongue to get its surroundings,
                and might use the move Glare to scare the opponent and
                have a possible getaway.''',
    "Pokedex":"023",
    "Abilities": [{"name":"Intimidate", "delete":False}, {"name":"Shed Skin", "delete":False}, {"name":"Unnerve", "delete":False}]
    },
    {
    "id":10,
    "name":"Pikachu",
    "picture":"https://vignette.wikia.nocookie.net/pokemon/images/0/0d/025Pikachu.png/revision/latest?cb=20140328192412",
    "description":'''Pikachu are small, chubby, and incredibly cute
                mouse-like Pokémon. They are almost completely covered
                by yellow fur. They have long yellow ears that are tipped
                with black. A Pikachu's back has two brown stripes, and
                its large tail is notable for being shaped like a
                lightning bolt. On its cheeks are two circle-shaped
                red pouches used for storing electricity. They turn
                yellow and spark with electricity when its about to use an
                Electric attack, such as Thunderbolt. It has also been known
                to generate small surges of electrical energy in anger or
                for protection, like in the anime. A female Pikachu looks
                almost exactly the same as a male, with the exception of
                her tail, which is rounded at the end and has an inward dent,
                giving it the appearance of a heart. However, in earlier anime
                episodes, and in the games prior to Generation IV, female and male
                Pikachu look identical. As Gigantamax Pikachu, it becomes larger
                and chubbier (similar to its Generation 1 design). Its tail becomes
                longer and stores all of the electricity it generates, causing it
                to glow a bright yellow and enabling it to become as powerful as
                a lightning strike. Its power is equal to that a power plant;
                however, it is difficult to use it in peoples' homes since Pikachu
                can only remain in its Gigantamax form for a short time.
                When several of these Pokémon gather, their electricity can cause
                lightning storms. In SM091, according to Pikala, the fur from
                Pikachu in the Kanto region sparkles in sunlight, while the
                Pikachu from Alola fur is silky smooth and shines in sunlight.
                Pikachus are usually friendly creatures that love to be cuddled.
                They love having their tails rubbed, especially at the base; they
                also like being stroked. However, if threatened or angered, this
                Pokémon can be quite aggressive. If someone pulls or steps on its
                tail, it is most likely it will bite or shock anyone in the area,
                including the one who pulled its tail. The Pikachu that live in the
                Pikachu Valley in Alola in the anime, greet each other by
                sniffing one another and rubbing their tails together. Also they
                can start duels with one another by sending electric signals and
                the winner is decided when the opponent's tail is bitten.''',
    "Pokedex":"025",
    "Abilities": [{"name":"Static", "delete":False}, {"name":"Lightning Rod", "delete":False}]
    },
    {
    "id":11,
    "name":"Sandshrew",
    "picture":"https://vignette.wikia.nocookie.net/pokemon/images/9/9e/027Sandshrew.png/revision/latest?cb=20140328192538",
    "description":'''Sandshrew has a white belly and a yellow back.
    Its back resembles bricked pavement or walls. It has a short tail,
    four short legs and a small head. Sandshrew resembles an armadillo,
    and can curl into a very tight ball: about the size of a basketball.
    Alolan Sandshrew, having fled the desert due to frequent eruptions,
    has adapted to the cold climate of the snowy mountains.
    This Sandshrew has a white belly and an ice blue back.
    Its back resembles bricked pavement or walls albeit colored ice blueself.
    It has a short tail, four short legs and a small head. The majority
    of its ice blue body is clad in steel-hard ice armour (also sporting
    the ice brick pattern). All Sandshrew have the ability Sand Veil,
    which raises evasion while there is a Sandstorm. All Alolan
    Sandshrew have the ability Snow Cloak, which raises evasion in
    Hail. Sandshrew, when in danger, can curl into a ball to defend
    itself. Alolan Sandshrew lack flexibility and cannot curl into a
    ball but have an excelling natural defense which makes up for this.
    They also have natural maneuverability on ice. Most Sandshrew are
    timid and they usually run away by digging holes.
    Despite this nature, they can become braver and more courageous
    once they're trained by skilled trainers.''',
    "Pokedex":"027",
    "Abilities": [{"name":"Sand Veil", "delete":False}, {"name":"Sand Rush", "delete":False}]
    },
    {
    "id":12,
    "name":"Nidoran",
    "picture":"https://vignette.wikia.nocookie.net/pokemon/images/8/80/029Nidoran%E2%99%80.png/revision/latest?cb=20140328192708",
    "description":'''Nidoran♀ is a small, rabbit-shaped Pokémon with
                large whiskers and front teeth, she is said to resemble
                Nidoran♂, but is lavender-bluish and has a much smaller
                horn on her head. She has darker spots on her body. She
                has the ability Poison Point that allows a 30 percent chance of
                the foe being poisoned if hit by a direct attack. Nidoran♀
                evolves into Nidorina at level 17. In Generation I, Nidoran♀
                evolves into Nidorina at level 16. Nidorina evolves into
                Nidoqueen by use of a Moon Stone.''',
    "Pokedex":"029",
    "Abilities": [{"name":"Poison Point", "delete":False}, {"name":"Rivalry", "delete":False}, {"name":"Hustle", "delete":False}]
    },
    {
    "id":13,
    "name":"Clefairy",
    "picture":"https://vignette.wikia.nocookie.net/pokemon/images/f/f4/035Clefairy.png/revision/latest?cb=20140328193109",
    "description":'''Clefairy is a small, round, pink, star-shaped Pokémon.
                Its hands have two white claws and a thumb. Its ears are
                short and pointy with dark tips. It has a long, curled
                tail and swirly hair and pink cheeks. On its back, it has
                small wings. Clefairy can have the ability Magic Guard or
                Cute Charm. Cute Charm allows Clefairy to have a 30 percent chance
                to infatuate the foe if the foe is the opposite gender and a
                physical attack hits Clefairy. Magic Guard allows Clefairy to
                only get damage by attacks. Clefairy can jump very high, as seen
                in the anime, and can hear very well. This is often the reason why
                they are hard to find. Clefairy collects moonlight in its wings and
                uses it to fly. Clefairy is very timid and rarely appears in front
                of humans. But it is very clever, and there are awareness among
                social and religious groups. Clefairy is a nocturnal Pokémon and
                will come out during the full moon to dance.''',
    "Pokedex":"035",
    "Abilities": [{"name":"Cute Charm", "delete":False}, {"name":"Magic Guard", "delete":False}, {"name":"Friend Guard", "delete":False}]
    },
    {
    "id":14,
    "name":"Vulpix",
    "picture":"https://vignette.wikia.nocookie.net/pokemon/images/6/60/037Vulpix.png/revision/latest?cb=20140328193205",
    "description":'''Vulpix are fox-like Pokémon with reddish-brown fur.
                Vulpix's most distinctive feature is its six orange tails
                that are curled at the tips. According to the Pokédex,
                when it is born, Vulpix possesses one snow white tail that
                eventually splits into many tails as it grows older. On the
                top of its head, Vulpix has a tuft of bright orange fur
                that curls into three rolls at the top and falls over its
                forehead at the bottom. Its underbelly is cream-colored.
                Additionally, a shiny Vulpix has a golden color scheme as
                opposed to its original red-brown. Also, Vulpix do not have
                any differences in appearance between genders.
                Alolan Vulpix, having moved to the snowy mountains to
                avoid other Pokémon habitats, has adapted to the cold
                climate. It is a fox-like Pokémon with snow white fur and
                ice blue paws. Alolan Vulpix's most distinctive feature is
                its snow white body and its six ice blue tails which are
                connected by a tuft of snow white fur. On the top of its
                head, Alolan Vulpix has a tuft of snow white fur which
                curls back and falls over its forehead at the bottom.
                Vulpix appear to be feminine Pokémon in general, and
                females are more commonly found in the wild than males.
                Vulpix are very intelligent. When they face a stronger
                enemy, they'll distract the enemy by feigning injury and
                then escape. Alolan Vulpix, which lives on cold mountains,
                usually forms a group varying from 2-5 members, helping
                and living with one another.''',
    "Pokedex":"037",
    "Abilities": [{"name":"Flash Fire", "delete":False}, {"name":"Drought", "delete":False}]
    },
    {
    "id":15,
    "name":"Jigglypuff",
    "picture":"https://vignette.wikia.nocookie.net/pokemon/images/3/3e/039Jigglypuff.png/revision/latest?cb=20140328193313",
    "description":'''Jigglypuff is small, round, pink Pokémon.
                It has short, digitless limbs and pointy ears. It
                has large, blue eyes and a tuft of fur on its head.
                Jigglypuff can hypnotize people and Pokémon using its
                voice. Jigglypuff has very stretchy skin and will inflate
                itself if it gets angry. In the anime, it has been shown
                to draw on people's faces after they have fallen asleep.''',
    "Pokedex":"039",
    "Abilities": [{"name":"Cute Charm", "delete":False}, {"name":"Competitive", "delete":False}, {"name":"Friend Guard", "delete":False}]
    },
    {
    "id":16,
    "name":"Zubat",
    "picture":"https://vignette.wikia.nocookie.net/pokemon/images/d/da/041Zubat.png/revision/latest?cb=20140328194041",
    "description":'''Zubat resembles a blue bat. It has a short,
                round body, purple wings, and slim legs missing feet.
                Zubat has no eyes, so it uses sound waves (echolocation) to
                navigate, like a real bat does. A female Zubat has smaller teeth
                than those of a male's. Strangely, it can use the move Mean Look,
                despite not having any eyes. Zubat has the ability Inner Focus
                and the hidden ability Infiltrator. Inner Focus prevents Zubat
                from flinching. Infiltrator prevents the effects of Reflect,
                Magic Coat, and Light Screen to work. Male Zubat have bigger
                fangs than the female ones.''',
    "Pokedex":"041",
    "Abilities": [{"name":"Infiltrator", "delete":False}, {"name":"Inner Focus", "delete":False}]
    },
    {
    "id":17,
    "name":"Oddish",
    "picture":"https://vignette.wikia.nocookie.net/pokemon/images/4/43/043Oddish.png/revision/latest?cb=20140328194044",
    "description":'''Oddish is a nocturnal Pokémon, using moonlight
                rather than the sun's rays for photosynthesis.
                During the day, Oddish avoids the sun's heat and
                brightness by burying itself into the earth, leaving only
                the leaves on top of its head visible above ground.
                This way, it disguises itself as a plant, misdirecting
                its carnivorous diurnal predators. While buried,
                Oddish nourishes itself by absorbing nutrients from the
                soil using its feet, which are said to temporarily change
                into a root-like structure for this purpose. If anyone
                pulls at Oddish's leaves and tries to uproot it while it
                is buried underground, Oddish will react by shrieking in
                a horrible voice. Once nightfall comes, exposure to moonlight
                causes Oddish to become much more active. It extracts itself
                from the ground, and its extremities change back into the shape
                of legs. It then proceeds to bathe itself in the moonlight and
                grow, as well as wander around scattering its seeds. With the
                coming of dawn, the cycle repeats. Oddish is the only Pokémon
                for which we know the pseudo-Latin "scientific name", as it
                appears in a Pokédex entry: Oddium wanderus. Oddish looks like
                a small animated plant. Its body is blue, with two small feet
                and red eyes. On top of its head grows a large clump of five
                long green leaves.''',
    "Pokedex":"043",
    "Abilities": [{"name":"Chlorophyll", "delete":False}, {"name":"Run Away", "delete":False}]
    },
    {
    "id":18,
    "name":"Paras",
    "picture":"https://vignette.wikia.nocookie.net/pokemon/images/d/d4/046Paras.png/revision/latest?cb=20140328194045",
    "description":'''Paras is very crablike, as it has six legs.
                The front two legs are very large, allowing Paras to grip
                on to prey and its environment. The most distinct feature
                are the two mushrooms on its back. It also has very large
                eyes on the top of its head. Paras can have the ability
                Effect Spore or Dry Skin. Effect Spore makes the foe
                paralyzed, asleep or poisoned 30 percent of the time whenever the
                foe hits Paras with a physical move. Dry Skin causes Paras
                to recover HP when it is raining and lose HP when it is
                sunny. The mushrooms on Paras' back have a mutualism with
                each other. The mushrooms get energy from Paras, while
                Paras gets to create spores.''',
    "Pokedex":"046",
    "Abilities": [{"name":"Effect Spore", "delete":False}, {"name":"Dry Skin", "delete":False}, {"name":"Damp", "delete":False}]
    },
    {
    "id":19,
    "name":"Venonat",
    "picture":"https://vignette.wikia.nocookie.net/pokemon/images/a/ad/048Venonat.png/revision/latest?cb=20140328194045",
    "description":'''Venonat is covered in large, purple fur. The feet
                of Venonat are brown and are about half as long as
                Venonat itself with its hands being the same color but
                a third of the size. Venonat have two white antennae that
                stick out of their head. The most notable feature of
                Venonat is their large, red eyes. It also has a small nose
                just under its eyes. Venonat can have the ability
                Compoundeyes or the ability Tinted Lens. Compoundeyes
                increases Venonat's accuracy by 30%. Tinted Lens increases
                the power of not-very-effective moves by 1.5x. Venonat's
                eyes are very accurate: they enable Venonat to easily catch
                extremely small prey. Conway has one in the episode
                Camping It Up.''',
    "Pokedex":"048",
    "Abilities": [{"name":"Compound Eyes", "delete":False}, {"name":"Tinted Lens", "delete":False}, {"name":"Run Away", "delete":False}]
    },
    {
    "id":20,
    "name":"Diglett",
    "picture":"https://vignette.wikia.nocookie.net/pokemon/images/3/31/050Diglett.png/revision/latest?cb=20140328194046",
    "description":'''Digletts are small, brown moles with two small eyes
                and a large pink/red nose. Since part of its body is
                underground, we don't know whether or not Diglett has
                feet, tail(s), etc. However, in Pokémon Mystery Dungeon
                Red Rescue Team and Blue Rescue Team, the rescued
                Diglett (after Skarmory kidnapped him) claimed to say
                his feet were getting cold (Which thereafter caused an
                awkward moment of silence). However, in its Alolan form
                the Diglett has three pieces of blonde hair that is on
                top of its head. Diglett live only a few feet underground,
                and feed on plant roots. It burrows through the ground at
                a shallow depth, leaving raised earth in its wake, perfect
                for planting crops. Diglett are frequently kept on farms
                for this reason. Diglett has very thin skin, and thus if
                Diglett is exposed to light its blood will heat up,
                causing it to grow weak. This weakness to heat causes
                Diglett to prefer dark places, sticking its head up only
                when the sun is not bright. Otherwise, it pops up in
                caves. Diglett make their homes in tunnels and caves
                under the earth, most of which are made by burrowing Onix.
                Diglett can have the ability Sand Veil or the ability
                Arena Trap. Sand Veil increases Diglett's evasiveness
                when a Sandstorm is out. Arena Trap prevents any Pokémon
                from escaping it in battle. Diglett are proficient
                diggers and can Dig quickly. Alolan Diglett can have
                the Tangling Hair Ability. With the Tangling Hair Ability,
                opponents that hit Alolan Diglett with a move that
                makes direct contact will have their Speed lowered by 1.''',
    "Pokedex":"050",
    "Abilities": [{"name":"Sand Veil", "delete":False}, {"name":"Arena Trap", "delete":False}, {"name":"Sand Force", "delete":False}]
    },
    {
    "id":21,
    "name":"Meowth",
    "picture":"https://vignette.wikia.nocookie.net/pokemon/images/d/d6/052Meowth.png/revision/latest?cb=20140328195855",
    "description":'''Meowth is a small, bipedal, feline Pokémon. It has
                two white whiskers on each side of its oval-shaped
                face and two hairs sticking up on either side of the
                coin-like gem on its forehead, and highly resembles a cat.
                Meowth's tail and feet are cream-colored like the rest of
                it, but they are brown at the end. It has small paw pads
                on the undersides of its heels and toes. It is much like
                a Maneki Neko, a toy of Japanese descent known for bobbing
                its arm and hand up and down. Alolan Meowth is a light
                blue-grey with smaller, half-open eyes. It was bred by
                royalty in the past. They are very spoiler, selfish, and
                arrogant, which makes them popular. Galarian Meowth is a
                greyish-brown color with thicker fur and a grinning mouth with
                sharp teeth. It travelled with Vikings in ancient times, which
                caused its fur to harden into iron. It battles by extending its
                claws like daggers. It doesn't get along with its Kantonian
                variant.''',
    "Pokedex":"052",
    "Abilities": [{"name":"Pickup", "delete":False}, {"name":"Technician", "delete":False}, {"name":"Unnerve", "delete":False}]
    },
    {
    "id":22,
    "name":"Psyduck",
    "picture":"https://vignette.wikia.nocookie.net/pokemon/images/5/53/054Psyduck.png/revision/latest?cb=20140328195856",
    "description":'''Psyduck is a medium-sized, yellow duck Pokémon.
                Only the feet and bill are tan. The other body parts
                are all yellow. Psyduck has three black hairs on top of
                its head, and its hands are always on its head due to its
                constant headache.''',
    "Pokedex":"054",
    "Abilities": [{"name":"Damp", "delete":False}, {"name":"Cloud Nine", "delete":False}, {"name":"Swift Swim", "delete":False}]
    },
    {
    "id":23,
    "name":"Mankey",
    "picture":"https://vignette.wikia.nocookie.net/pokemon/images/4/41/056Mankey.png/revision/latest?cb=20140328195857",
    "description":'''Mankey is a small, monkey-like Pokémon.
                They are a mostly tan in color, with a round body,
                long limbs and a tail. They have a pig nose due to it
                being the Pig Monkey species. Mankey are also renowned
                for their pointy ears and medium length fur. They have
                triangular eyes with red irises; this clearly represents
                the anger this Pokémon is known for.''',
    "Pokedex":"056",
    "Abilities": [{"name":"Vital Spirit", "delete":False}, {"name":"Anger Point", "delete":False}, {"name":"Defiant", "delete":False}]
    },
    {
    "id":24,
    "name":"Growlithe",
    "picture":"https://vignette.wikia.nocookie.net/pokemon/images/3/3d/058Growlithe.png/revision/latest?cb=20140328195857",
    "description":'''This Pokémon resembles a puppy. It has bright orange
                fur with black stripes. Its belly, tail, and fluff on
                top of its head are a cream color. There are no gender
                differences. Much like Vulpix, its shiny form is a
                yellow/golden color.''',
    "Pokedex":"058",
    "Abilities": [{"name":"Intimidate", "delete":False}, {"name":"Flash Fire", "delete":False}, {"name":"Justified", "delete":False}]
    },
    {
    "id":25,
    "name":"Poliwag",
    "picture":"https://vignette.wikia.nocookie.net/pokemon/images/4/49/060Poliwag.png/revision/latest?cb=20140328195858",
    "description":'''It is so soft its organs are actually visible. It
                also has trouble walking on its feet due to its lack of
                arms which causes it to be unbalanced. The swirl on its
                belly is its internal organs showing through. If the swirl
                is tinged, that means it's affected by some disease.''',
    "Pokedex":"060",
    "Abilities": [{"name":"Water Absorb", "delete":False}, {"name":"Damp", "delete":False}, {"name":"Swift Swim", "delete":False}]
    },
    {
    "id":26,
    "name":"Abra",
    "picture":"https://vignette.wikia.nocookie.net/pokemon/images/6/62/063Abra.png/revision/latest?cb=20140328202819",
    "description":'''Abra is a golden-brown, human-like fox Pokémon with
                three fingers and toes on both arms and legs. Its eyes
                are mostly closed because of its tendency to sleep a lot.
                The shoulders are brown. Abra has a long tail with one
                brown stripe. Feet have 3 sharp claws, 2 on the front and
                1 on the heel. Abra stands 2'11" and has the same physical
                appearance, no matter what its gender is. It has
                slightly-pointed ears and its body looks slightly like it
                has a type of body armour on its top half.''',
    "Pokedex":"063",
    "Abilities": [{"name":"Synchronize", "delete":False}, {"name":"Inner Focus", "delete":False}, {"name":"Magic Guard", "delete":False}]
    },
    {
    "id":27,
    "name":"Machop",
    "picture":"https://vignette.wikia.nocookie.net/pokemon/images/8/85/066Machop.png/revision/latest?cb=20140328203356",
    "description":'''Machop is a bluish-gray Pokémon with large arm
                muscles. It has three brown ridges on its head,
                rib-like protrusions on its sides, has a tail, and
                resembles a human child. Machop can have the abilities
                Guts and No Guard. Guts increases Machop's attack when
                it has a status effect. No Guard allows both the opponent's
                and Machop's attacks to hit more often. Machop is very strong
                and is capable of mastering many types of martial arts.''',
    "Pokedex":"066",
    "Abilities": ["Guts", "No Guard", "Steadfast"]
    },
    {
    "id":28,
    "name":"Bellsprout",
    "picture":"https://vignette.wikia.nocookie.net/pokemon/images/a/a2/069Bellsprout.png/revision/latest?cb=20140328203359",
    "description":'''Bellsprout is a plant-like Pokémon. The body is
                a thin brown root and stem system. Bellsprout has two
                root-like legs. It has two leaves on each side. Its head
                is yellow and shaped like a bulb, the tip is colored pink, and it
                has the smallest amount of dirt on its feet.''',
    "Pokedex":"069",
    "Abilities": [{"name":"Chlorophyll", "delete":False}, {"name":"Gluttony", "delete":False}]
    },
    {
    "id":29,
    "name":"Tentacool",
    "picture":"https://vignette.wikia.nocookie.net/pokemon/images/4/4e/072Tentacool.png/revision/latest?cb=20140328203939",
    "description":'''Tentacool is an aquatic Pokémon based on the box
                jellyfish. Tentacool have two long tentacles that extend
                from the base of its large, blue head. There are three
                red gems on this Pokémon's head: two on the sides of its
                head and one on its forehead. It drifts aimlessly wherever
                the ocean currents take it, sometimes ending up in shallow
                waters where it may be accidentally caught in fishing
                lines. Tentacool may also end up stuck on beaches when low
                tide comes; since its body is largely composed of water,
                it will shrivel up, risking death from dehydration if it
                stays out of the sea for too long. Tentacool has two main
                weapons. At the tips of its tentacles are toxic feelers,
                which it uses to stab anything it touches with stinging
                acid. Due to its excellent camouflage in the water,
                Tentacool can often remain undetected by swimmers right
                up to the moment it stings them. Tentacool's gelatinous,
                watery body can also absorb sunlight and refract it
                within, producing beam energy it shoots from its
                crystal-like eyes.''',
    "Pokedex":"072",
    "Abilities": [{"name":"Clear Body", "delete":False}, {"name":"Liquid Ooze", "delete":False}, {"name":"Rain Dish", "delete":False}]
    },
    {
    "id":30,
    "name":"Geodude",
    "picture":"https://vignette.wikia.nocookie.net/pokemon/images/9/98/074Geodude.png/revision/latest?cb=20140328203940",
    "description":'''This Pokémon has a rock for a head, no nose, and
                two long arms that start with a bulging muscle and end
                with rock hands resembling a human's. Alolan variant
                Geodude are slate grey with black eyebrows and
                three-fingered hands (the middle, ring and pinky fingers
                are now one).''',
    "Pokedex":"074",
    "Abilities": [{"name":"Rock Head", "delete":False}, {"name":"Sturdy", "delete":False}, {"name":"Sand Veil", "delete":False}]
    },
]

@app.route('/')
def search_box(name=None):

    return render_template('start.html', data=pokemon)

@app.route('/view/<id>')
def view(id=id):
    global pokemon
    data = []
    id = int(id)
    for element in pokemon:
        if(element["id"] == id):
            data.append(element)

    name = data[0]["name"]
    picture = data[0]["picture"]
    description = data[0]["description"]
    pokedex = data[0]["Pokedex"]
    abilities = []
    for element in data[0]["Abilities"]:
        if(not element["delete"]):
            abilities.append(element["name"])

    return render_template('template.html', name=name, picture=picture, description=description, pokedex=pokedex, abilities=abilities)

@app.route('/edit/<id>')
def edit(id=id):
    global pokemon
    data = []
    id = int(id)
    for element in pokemon:
        if(element["id"] == id):
            data.append(element)
    description = data[0]["description"]


    return render_template('edit.html', description=description)


@app.route('/create')
def create(name=None):

    return render_template('create.html', data=pokemon)

@app.route('/search')
def search(name=None):

    return render_template('search.html', data=pokemon)

@app.route('/ten_names', methods=['GET', 'POST'])
def ten_names():
    global pokemon
    json_data = request.get_json()

    length = len(pokemon) - 10
    data = pokemon[length:len(pokemon)]
    data = data[::-1]
    return jsonify(data = data)

@app.route('/search_name', methods=['GET', 'POST'])
def search_name():
    global pokemon
    global lastSearch

    print("im in python")
    json_data = request.get_json()
    print(json_data)
    data = []
    print(lastSearch)
    for element in pokemon:
        if(lastSearch.lower() in element["name"].lower()):
            data.append(element)
            print(element["name"])
        elif(element["name"].lower() in lastSearch.lower()):
            data.append(element)
    data = [data, lastSearch]


    return jsonify(data = data)

@app.route('/save_name', methods=['GET', 'POST'])
def save_name():
    global pokemon
    global lastSearch
    print("im in python")
    json_data = request.get_json()
    print(json_data)
    lastSearch = json_data
    print(lastSearch)
    data = []

    return jsonify(data = data)


@app.route('/create_name', methods=['GET', 'POST'])
def create_name():
    global pokemon
    global current_id

    json_data = request.get_json()
    json_data["id"] = current_id
    pokemon.append(json_data)
    data = json_data
    current_id += 1

    return jsonify(data = data)

@app.route('/delete_name', methods=['GET', 'POST'])
def delete_name():
    global pokemon

    json_data = request.get_json()

    for item in pokemon:
        if(item["id"]==json_data):
            pokemon.remove(item)

    return jsonify(data = pokemon)

@app.route('/delete_attr', methods=['GET', 'POST'])
def delete_attr():
    global pokemon

    json_data = request.get_json()

    print(json_data[1])

    for item in pokemon:
        if(item["id"]==int(json_data[0])):
            print("idfound")
            for element in item["Abilities"]:
                print("found an element")
                if(element["name"] == json_data[1]):
                    element["delete"] = True
                    print("markedasdeleted")



    return jsonify(data = pokemon)

@app.route('/undo', methods=['GET', 'POST'])
def undo():
    global pokemon

    json_data = request.get_json()

    print(json_data[1])

    for item in pokemon:
        if(item["id"]==int(json_data[0])):
            print("idfound")
            for element in item["Abilities"]:
                print("found an element")
                if(element["name"] == json_data[1]):
                    element["delete"] = False
                    print("undid")



    return jsonify(data = pokemon)

@app.route('/update_description', methods=['GET', 'POST'])
def update_description():
    global pokemon

    json_data = request.get_json()
    description=json_data[0]
    idd = json_data[1]
    idd = int(idd)
    for element in pokemon:
        if(element['id'] == idd):
            print("charmander")
            element["description"] = description


    return jsonify(data = idd)

@app.route('/update_pokedex', methods=['GET', 'POST'])
def update_pokedex():
    global pokemon

    json_data = request.get_json()
    pokedex=json_data[0]
    idd = json_data[1]
    idd = int(idd)
    for element in pokemon:
        if(element['id'] == idd):
            print("squirtle")
            element["Pokedex"] = pokedex


    return jsonify(data = idd)

@app.route('/get_pokedex', methods=['GET', 'POST'])
def get_pokedex():
    global pokemon

    json_data = request.get_json()
    idd = json_data
    idd = int(idd)
    data = ""
    for element in pokemon:
        if(element['id'] == idd):
            print("bulbasaur")
            data = element["Pokedex"]


    return jsonify(data = data)


if __name__ == '__main__':
   app.run(debug = True)
