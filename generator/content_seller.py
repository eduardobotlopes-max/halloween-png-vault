# -*- coding: utf-8 -*-
"""Copy for BONUS #5 · Halloween Seller Kit. Plain data, no layout."""

PLAN = [
    ("Day 1", "Pick three designs", "Open the Vault and choose three designs only: one cute, one funny, "
                                    "one spooky. Three is enough to learn what your buyers like."),
    ("Day 2", "Choose one product", "T-shirt, mug or tumbler. One. You will be faster, your photos will "
                                    "match and your postage will be predictable."),
    ("Day 3", "Make one sample", "Press or print one item for yourself. You need it for photos, and you "
                                 "need to know how it feels before someone pays for it."),
    ("Day 4", "Photograph it", "Five photos: front, worn or held, close-up of the print, packaged, and "
                               "one lifestyle shot. Daylight, plain background, no flash."),
    ("Day 5", "Write the listing", "Use the title formula and the description template in this kit. "
                                   "Fill all 13 tags."),
    ("Day 6", "Publish and tell people", "Publish the listing. Post the photos in two local Facebook "
                                         "groups and send them to ten people who know you."),
    ("Day 7", "Read the numbers", "Views but no sales means the photos or the price. No views means the "
                                  "title and tags. Change one thing, not five."),
]

SELLS = [
    ("Funny quote tees", "Adults, 25-45", "Highest volume. People buy a joke they identify with, not art."),
    ("Cute ghost anything", "Women, 18-35", "The safest seller. Works on mugs, tumblers, totes, stickers."),
    ("Kids' Halloween tees", "Parents", "Bought in the last two weeks of October. Size range matters."),
    ("Teacher Halloween", "Teachers, TAs", "Small but loyal. Sells from mid-September."),
    ("Family matching sets", "Parents", "Highest order value: 3-5 items in one sale."),
    ("Dog & cat mums", "Pet owners", "Year-round buyers who spend at Halloween too."),
    ("Party décor prints", "Party hosts", "Low cost, easy postage, good add-on."),
    ("Retro / groovy", "18-30", "Strong in the UK for sweatshirts and tote bags."),
]

METHODS = [
    ("DTF transfers", "£0 (buy transfers)", "£2-4", "Any colour cotton", "Buy pressed transfers online, "
     "apply with a heat press. Cheapest way to start with no printer."),
    ("Sublimation", "£150-300 kit", "£1-3", "White polyester, mugs, tumblers", "Best colours, but only on "
     "light polyester or coated items."),
    ("HTV vinyl", "£200+ cutter", "£1-2", "Bold, simple shapes", "Great for single-colour quotes. Slow "
     "for detailed artwork."),
    ("Print on demand", "£0", "Their price", "Testing designs", "No stock, no press, smaller margin. "
     "Good for finding out what sells."),
]

PRICING_ROWS = [
    ("Sale price", "£18.00"),
    ("Blank T-shirt", "-£4.20"),
    ("DTF transfer + press", "-£2.40"),
    ("Postage (large letter, 2nd class)", "-£1.75"),
    ("Packaging", "-£0.35"),
    ("Platform fees (approx. 10-12%)", "-£2.10"),
    ("Your profit", "£7.20"),
]

PLACES = [
    ("Etsy", "Ready-made buyers searching for Halloween right now. Fees and competition are the trade-off. "
             "Start here if you want traffic without building an audience."),
    ("eBay", "Underrated for Halloween tees. Less design-led, but buyers are ready to pay and postage is simple."),
    ("Facebook groups & Marketplace", "Free, local, fast. Post in parent groups, village groups and "
                                      "Halloween event groups. Offer local collection."),
    ("School fairs & local markets", "October fairs sell out of kids' tees and party décor. Take card payments."),
    ("Your own shop (Shopify, Etsy Pattern)", "Only worth it once you have repeat buyers. Don't start here."),
]

PHOTOS = [
    "The flat lay: product on a plain surface with two small props (a pumpkin and dried leaves).",
    "Worn or held: a person wearing the tee or holding the mug. Faces optional, hands are fine.",
    "Close-up: the print filling the frame so people see the quality.",
    "Scale: the item next to something familiar so size is obvious.",
    "Packaged: how it arrives. This single photo reduces \"when will it come?\" messages.",
]

TITLE_FORMULA = [
    ("1", "What it is", "Halloween Ghost T-Shirt"),
    ("2", "Who it's for / occasion", "Halloween Gift for Her"),
    ("3", "Style words buyers type", "Cute Spooky Season Tee"),
    ("4", "Trust or delivery", "UK Seller, Fast Dispatch"),
]

TAG_RULES = [
    "Use all 13 tags. Empty tags are free traffic you are throwing away.",
    "Maximum 20 characters per tag, so \"halloween sweatshirt\" fits but \"cute halloween sweatshirt\" does not.",
    "Multi-word tags beat single words: \"spooky season tee\" beats \"spooky\".",
    "Repeat your best tag inside the title and the first line of the description.",
    "Don't use brand names, film characters or \"Disney style\". That's how shops get closed.",
]

DESCRIPTION_TEMPLATE = """[FIRST LINE = your main keyword, written like a sentence]
Cute ghost Halloween T-shirt, printed and posted from the UK.

WHAT YOU GET
- [Product] in [material], [colour options]
- Design printed with [method], soft to the touch and machine washable
- Sizes [S-XXL] - see the size guide photo

POSTAGE
- Dispatched within [1-2] working days
- Royal Mail [2nd class], usually [2-3] days
- Order by [26 October] for delivery before Halloween

CARE
- Wash inside out at 30 degrees, do not tumble dry, iron on the reverse

Questions? Message me - I usually reply the same day."""

MESSAGES = [
    ("When the order comes in",
     "Hi [name], thanks so much for your order! I'm making your [item] today and it will be posted by "
     "[date]. I'll message you with the tracking as soon as it's on its way. - [your name]"),
    ("When you post it",
     "Hi [name], your [item] is on its way. Royal Mail [2nd class], so it should arrive by [date]. "
     "I hope you love it - any problems at all, just message me."),
    ("A few days after delivery",
     "Hi [name], just checking your [item] arrived safely and you're happy with it. If anything isn't "
     "right, tell me and I'll sort it. If you have a minute, an honest review really helps a small shop."),
    ("If something goes wrong",
     "Hi [name], I'm really sorry about this. I'll [replace it / refund you] straight away - you don't "
     "need to send anything back. Thanks for letting me know."),
]

CHECKLIST = [
    "Three designs chosen from the Vault",
    "One product type decided",
    "Sample made and photographed (five shots)",
    "Title written with the four-part formula",
    "All 13 tags filled in",
    "Description uses the template, with your real dispatch times",
    "Postage cost checked on the Royal Mail price finder",
    "\"Order by\" date added to the listing (26 October)",
    "Listing published",
    "Photos posted in two local groups",
    "Price checked against three similar listings",
    "Review request message saved as a template",
]

CALENDAR = [
    ("Mid-September", "List your first designs. Early listings gather views before the rush."),
    ("1-10 October", "Add two more designs. Start posting photos locally twice a week."),
    ("11-20 October", "Peak buying. Keep dispatch times honest and stock your blanks."),
    ("21-26 October", "Last posting days. Add \"order by\" dates to every listing."),
    ("27-31 October", "Local collection and market days only. Switch to digital/printable items."),
    ("1 November", "Note what sold. Those designs are your starting point next year."),
]

# ---------------------------------------------------------------- 100 titles
TITLES = {
    "T-shirts (20)": [
        "Cute Ghost Halloween T-Shirt, Spooky Season Tee, Halloween Gift for Her, UK Seller",
        "Funny Halloween T-Shirt, This Is My Human Costume Tee, Sarcastic Halloween Gift",
        "Retro Groovy Halloween T-Shirt, 70s Style Spooky Tee, Vintage Halloween Shirt",
        "Pumpkin Patch T-Shirt, Autumn Halloween Tee, Cosy Season Shirt, Gift for Her",
        "Ghouls Just Wanna Have Fun T-Shirt, Funny Halloween Tee, Girls Night Shirt",
        "Halloween Skeleton T-Shirt, Dead Inside But Caffeinated Tee, Funny Coffee Gift",
        "Witch Please T-Shirt, Funny Witch Halloween Tee, Gift for Best Friend",
        "Black Cat Halloween T-Shirt, Cute Cat Lover Tee, Spooky Kitty Shirt",
        "Halloween Teacher T-Shirt, Spooky Teacher Tee, Classroom Halloween Gift",
        "Matching Family Halloween T-Shirts, Boo Crew Tee, Family Costume Shirt",
        "Horror Night T-Shirt, Vintage Horror Movie Style Tee, Scary Halloween Shirt",
        "Coquette Halloween T-Shirt, Pink Bow Ghost Tee, Cute Spooky Girly Shirt",
        "Trick or Treat T-Shirt, Classic Halloween Tee, Unisex Halloween Shirt",
        "Dog Mum Halloween T-Shirt, Spooky Dog Mama Tee, Gift for Dog Lover",
        "Halloween Pregnancy Announcement T-Shirt, Pumpkin Bump Tee, Mum to Be Gift",
        "Stay Spooky T-Shirt, Minimal Halloween Tee, Everyday Autumn Shirt",
        "Creep It Real T-Shirt, Funny Pun Halloween Tee, Gift for Him",
        "Halloween Nurse T-Shirt, Spooky Shift Tee, NHS Halloween Gift",
        "Bats and Moon T-Shirt, Celestial Halloween Tee, Witchy Aesthetic Shirt",
        "Too Cute To Spook T-Shirt, Kids Halloween Tee, Toddler Halloween Shirt",
    ],
    "Mugs (15)": [
        "Cute Ghost Halloween Mug, Spooky Season Coffee Cup, Gift for Her, UK Made",
        "Witch Better Have My Coffee Mug, Funny Halloween Gift, Novelty Cup",
        "Pumpkin Spice Mug, Autumn Coffee Cup, Cosy Season Gift for Coffee Lover",
        "Halloween Skeleton Mug, Dead Inside But Caffeinated Cup, Funny Office Gift",
        "Black Cat Mug, Cute Halloween Cat Cup, Gift for Cat Lover",
        "Personalised Halloween Mug, Custom Name Spooky Cup, Trick or Treat Gift",
        "Retro Halloween Mug, Groovy 70s Pumpkin Cup, Vintage Style Gift",
        "Boo-jee Mug, Funny Ghost Coffee Cup, Halloween Gift for Best Friend",
        "Witchy Vibes Mug, Potion Bottle Coffee Cup, Gift for Witch Lover",
        "Halloween Teacher Mug, Spooky Teacher Gift, End of Term Present",
        "Hot Chocolate Halloween Mug, Kids Spooky Cup, Family Halloween Gift",
        "Horror Movie Mug, Scary Night Coffee Cup, Gift for Horror Fan",
        "Coquette Halloween Mug, Pink Bow Ghost Cup, Cute Girly Gift",
        "Halloween Couples Mugs, His and Hers Spooky Set, Matching Gift",
        "Trick or Treat Mug, Classic Halloween Cup, Party Table Gift",
    ],
    "Tumblers & bottles (15)": [
        "Halloween Tumbler 20oz, Cute Ghost Skinny Tumbler, Spooky Season Gift",
        "Retro Halloween Tumbler, Groovy Pumpkin 20oz Cup, Vintage Style Gift",
        "Personalised Halloween Tumbler, Custom Name Spooky Cup with Straw",
        "Witchy Tumbler 20oz, Potion and Moon Skinny Cup, Gift for Her",
        "Black Cat Tumbler, Cute Halloween Cat Travel Cup, Cat Lover Gift",
        "Neon Halloween Tumbler, Glow Style Spooky Cup, Party Gift",
        "Coquette Halloween Tumbler, Pink Bow Ghost Cup, Cute Gift for Her",
        "Skeleton Tumbler 20oz, Funny Coffee Skinny Cup, Gift for Him",
        "Halloween Teacher Tumbler, Spooky Classroom Cup, Teacher Gift",
        "Trick or Treat Tumbler, Kids Halloween Cup with Lid and Straw",
        "Pumpkin Spice Tumbler, Autumn Travel Cup, Cosy Season Gift",
        "Horror Night Tumbler, Scary Movie Skinny Cup, Horror Fan Gift",
        "Halloween Water Bottle, Spooky Season Sports Bottle, Gym Gift",
        "Bats and Moon Tumbler, Celestial Halloween Cup, Witchy Gift",
        "Matching Halloween Tumblers, Couples Spooky Cup Set, Gift Idea",
    ],
    "Bags & accessories (15)": [
        "Trick or Treat Bag, Canvas Halloween Tote, Kids Sweet Bag, UK Seller",
        "Personalised Trick or Treat Bag, Custom Name Halloween Tote for Kids",
        "Cute Ghost Tote Bag, Spooky Season Shopper, Gift for Her",
        "Halloween Book Bag, Spooky Library Tote, Gift for Book Lover",
        "Black Cat Tote Bag, Cute Halloween Shopper, Cat Lover Gift",
        "Witchy Tote Bag, Moon and Potion Canvas Bag, Gift for Her",
        "Retro Halloween Tote Bag, Groovy Pumpkin Shopper, Vintage Style",
        "Halloween Drawstring Bag, Kids Party Bag, Sweet Loot Bag",
        "Spooky Makeup Bag, Halloween Wash Bag, Gift for Her",
        "Halloween Apron, Spooky Baking Apron, Gift for Baker",
        "Halloween Tea Towel, Spooky Kitchen Gift, Autumn Home Decor",
        "Trick or Treat Basket Tag, Personalised Halloween Bag Tag",
        "Halloween Keyring, Cute Ghost Charm, Party Bag Filler",
        "Spooky Lanyard, Halloween Teacher Lanyard, Staff Gift",
        "Halloween Bandana for Dogs, Spooky Pet Scarf, Dog Halloween Costume",
    ],
    "Stickers, décor & kids (35)": [
        "Halloween Sticker Sheet, Cute Ghost Stickers, Journal and Laptop Stickers",
        "Spooky Season Sticker Pack, Waterproof Halloween Stickers, Water Bottle Set",
        "Halloween Party Bag Stickers, Kids Treat Bag Labels, Party Favours",
        "Personalised Halloween Name Stickers, Custom Trick or Treat Labels",
        "Retro Halloween Stickers, Groovy Pumpkin Sticker Sheet, Vintage Style",
        "Halloween Reward Stickers for Teachers, Classroom Sticker Sheet",
        "Halloween Bunting, Happy Halloween Banner, Party Decoration",
        "Trick or Treaters Welcome Sign, Halloween Door Sign, Porch Decor",
        "Enter If You Dare Sign, Halloween Door Decoration, Party Prop",
        "Halloween Cupcake Toppers, Spooky Party Cake Picks, Set of 12",
        "Halloween Party Invitations, Spooky Kids Party Invites, Pack of 10",
        "Personalised Halloween Party Invitations, Custom Kids Invites",
        "Halloween Table Decorations, Food Labels for Party Buffet",
        "Halloween Bingo Game for Kids, Printed Party Game, Set of 8 Cards",
        "Halloween Scavenger Hunt, Kids Party Game, Trick or Treat Activity",
        "Halloween Cushion Cover, Spooky Home Decor, Autumn Cushion",
        "Halloween Wall Print, Spooky Season Poster, Autumn Home Decor",
        "Personalised Halloween Print, Custom Family Spooky Poster",
        "Halloween Tealight Holder Wrap, Spooky Candle Decor, Set of 4",
        "Halloween Chocolate Bar Wrappers, Party Favour Sweets, Pack of 12",
        "Kids Halloween T-Shirt, Little Monster Tee, Toddler Spooky Shirt",
        "Baby Halloween Bodysuit, My First Halloween Vest, Newborn Gift",
        "Kids Halloween Hoodie, Spooky Pumpkin Jumper, Child Autumn Top",
        "Halloween Sweatshirt Women, Cute Ghost Jumper, Cosy Autumn Top",
        "Oversized Halloween Sweatshirt, Spooky Season Jumper, Gift for Her",
        "Halloween Pyjamas Kids, Spooky Sleep Set, Family Matching PJs",
        "Halloween Socks, Spooky Season Socks, Stocking Filler Gift",
        "Halloween Hair Bow, Spooky Ghost Bow for Girls, Party Accessory",
        "Halloween Cake Topper, Happy Halloween Cake Decoration",
        "Halloween Treat Boxes, Kids Party Favour Boxes, Set of 10",
        "Spooky Placemats for Kids, Halloween Table Setting, Party Decor",
        "Halloween Colouring Pages for Kids, Printable Activity Sheets",
        "Halloween Advent Countdown, Spooky Countdown Calendar for Kids",
        "Pumpkin Carving Stencils, Halloween Pumpkin Templates, Printable",
        "Halloween Photo Booth Props, Party Selfie Props, Set of 12",
    ],
}

TAG_PACKS = [
    ("Cute ghost tee", ["halloween tshirt", "ghost tshirt", "cute halloween", "spooky season tee",
                        "halloween gift", "boo tshirt", "halloween top", "womens halloween",
                        "spooky tshirt", "ghost gift", "halloween uk", "autumn tshirt", "trick or treat"]),
    ("Funny quote tee", ["funny halloween", "halloween tshirt", "sarcastic tshirt", "funny tee",
                         "halloween humour", "joke tshirt", "spooky tshirt", "halloween gift",
                         "funny gift", "novelty tshirt", "halloween top", "banter tshirt", "mens halloween"]),
    ("Retro Halloween", ["retro halloween", "groovy halloween", "vintage tshirt", "70s halloween",
                         "retro tshirt", "halloween tee", "spooky season", "retro pumpkin",
                         "halloween gift", "boho halloween", "autumn tshirt", "wavy text tee", "retro ghost"]),
    ("Halloween mug", ["halloween mug", "spooky mug", "ghost mug", "halloween gift",
                       "coffee mug gift", "novelty mug", "autumn mug", "pumpkin mug",
                       "witch mug", "cute mug", "halloween cup", "mug for her", "trick or treat"]),
    ("20oz tumbler", ["halloween tumbler", "20oz tumbler", "skinny tumbler", "spooky tumbler",
                      "halloween cup", "tumbler gift", "ghost tumbler", "witch tumbler",
                      "halloween gift", "travel cup", "autumn tumbler", "cute tumbler", "straw cup"]),
    ("Trick or treat bag", ["trick or treat", "halloween bag", "sweet bag", "kids halloween",
                            "tote bag kids", "candy bag", "halloween tote", "party bag",
                            "personalised bag", "halloween gift", "treat bag", "canvas tote", "spooky bag"]),
    ("Kids Halloween", ["kids halloween", "toddler tshirt", "childrens top", "little monster",
                        "halloween kids", "boys halloween", "girls halloween", "spooky kids",
                        "first halloween", "halloween gift", "kids tee", "pumpkin tshirt", "cute spooky"]),
    ("Teacher Halloween", ["teacher gift", "halloween teacher", "teacher tshirt", "school halloween",
                           "classroom gift", "spooky teacher", "teaching assistant", "ta gift",
                           "halloween gift", "teacher mug", "school gift", "staff gift", "term gift"]),
    ("Witchy", ["witchy gift", "witch tshirt", "halloween witch", "potion print",
                "witchy vibes", "moon and stars", "celestial gift", "witch mug",
                "spooky gift", "halloween gift", "basic witch", "tarot gift", "magic gift"]),
    ("Coquette Halloween", ["coquette", "pink halloween", "bow print", "cute halloween",
                            "girly halloween", "coquette gift", "pink ghost", "soft girl",
                            "halloween gift", "spooky cute", "bow tshirt", "pastel halloween", "her gift"]),
    ("Party printables", ["halloween party", "party printable", "kids party game", "party decor",
                          "halloween decor", "party invites", "cupcake toppers", "party bunting",
                          "halloween banner", "party favours", "trick or treat", "kids activity", "party pack"]),
    ("Pet Halloween", ["dog halloween", "pet bandana", "dog mum gift", "cat mum gift",
                       "spooky pet", "dog tshirt", "pet costume", "halloween pet",
                       "dog lover gift", "cat lover gift", "pet gift uk", "dog bandana", "puppy halloween"]),
]
