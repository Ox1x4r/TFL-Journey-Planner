import sys

stations = ["Harrow & Wealdstone", "Kenton", "South Kenton", "North Wembley", "Wembley Central", "Stonebridge Park", "Harlesden", "Willesden Junction", "Kensal Green", "Queen's Park", "Kilburn Park", "Maida Vale", "Warwick Avenue", "Paddington", "Edgware Road", "Marylebone", "Baker Street", "Regent's Park", "Oxford Circus", "Piccadilly Circus", "Charing Cross", "Embankment", "Waterloo", "Lambeth North", "Elephant & Castle", "Harrow & Wealdstone", "Kenton", "South Kenton", "North Wembley", "Wembley Central", "Stonebridge Park", "Harlesden", "Willesden Junction", "Kensal Green", "Queen's Park", "Kilburn Park", "Maida Vale", "Warwick Avenue", "Paddington", "Edgware Road", "Marylebone", "Baker Street", "Regent's Park", "Oxford Circus", "Piccadilly Circus", "Charing Cross", "Embankment", "Waterloo", "Lambeth North", "Epping", "Theydon Bois", "Debden", "Loughton", "Buckhurst Hill", "Woodford", "South Woodford", "Snaresbrook", "Roding Valley", "Chigwell", "Grange Hill", "Hainault", "Fairlop", "Barking'side", "Newbury Park", "Gants Hill", "Redbridge", "Wanstead", "Leytonstone", "Leyton", "Stratford", "Mile End", "Bethnal Green", "Liverpool Street", "Bank", "St. Paul's", "Chancery Lane", "Holborn", "Tottenham", "Oxford Circus", "Bond Street", "Marble Arch", "Lancaster Gate", "Queensway", "Notting Hill Gate", "Holland Park", "Shepherd's Bush", "White City", "East Acton", "North Acton", "West Acton", "Ealing Broadway", "Hanger Lane", "Perivale", "Greenford", "Northolt", "South Ruislip", "Ruislip Gardens", "West Ruislip", "Epping", "Theydon Bois", "Debden", "Loughton", "Buckhurst Hill", "Woodford", "South Woodford", "Snaresbrook", "Roding Valley", "Roding Valley", "Chigwell", "Grange Hill", "Hainault", "Fairlop", "Barkingside", "Newbury Park", "Gants Hill", "Redbridge", "Wanstead", "Leytonstone", "Leyton", "Stratford", "Mile End", "Bethnal Green", "Liverpool Street", "Bank", "St. Paul's", "Chancery Lane", "Holborn", "Tottenham", "Oxford Circus", "Bond Street", "Marble Arch", "Lancaster Gate", "Queensway", "Notting Hill Gate", "Holland Park", "Shepherd's Bush", "White City", "East Acton", "North Acton", "North Acton", "West Acton", "Hanger Lane", "Perivale", "Greenford", "Northolt", "South Ruislip", "Ruislip Gardens", "Edgware Road", "Paddington", "Bayswater", "Notting Hill Gate", "High Street Kensington", "Gloucester Road", "South Kensington", "Sloane Square", "Victoria", "St. James's Park", "Westminster", "Embankment", "Temple", "Blackfriars", "Mansion House", "Cannon Street", "Monument", "Tower Hill", "Aldgate", "Liverpool Street", "Moorgate", "Barbican", "Farringdon", "King's Cross St. Pancras", "Euston Square", "Great Portland Street", "Baker Street", "Royal Oak", "Westbourne Park", "Ladbroke Grove", "Latimer Road", "Wood Lane", "Shepherd's Bush Market", "Goldhawk Road", "Hammersmith", "Edgware Road", "Paddington", "Bayswater", "Notting Hill Gate", "High Street Kensington", "Gloucester Road", "South Kensington", "Sloane Square", "Victoria", "St. James's Park", "Westminster", "Embankment", "Temple", "Blackfriars", "Mansion House", "Cannon Street", "Monument", "Tower Hill", "Aldgate", "Liverpool Street", "Moorgate", "Barbican", "Farringdon", "King's Cross St. Pancras", "Euston Square", "Great Portland Street", "Baker Street", "Paddington", "Royal Oak", "Westbourne Park", "Ladbroke Grove", "Latimer Road", "Wood Lane", "Shepherd's Bush Market", "Goldhawk Road", "Upminster", "Upminster Bridge", "Hornchurch", "Elm Park", "Dagenham East", "Dagenham Heathway", "Becontree", "Upney", "Barking", "East Ham", "Upton Park", "Plaistow", "West Ham", "Bromley-by-Bow", "Bow Road", "Mile End", "Stepney Green", "Whitechapel", "Aldgate East", "Tower Hill", "Monument", "Cannon Street", "Mansion House", "Blackfriars", "Temple", "Embankment", "Westminster", "St. James's Park", "Victoria", "Sloane Square", "South Kensington", "Gloucester Road", "Earl's Court", "Kensington (Olympia)", "High Street Kensington", "Notting Hill Gate", "Bayswater", "Paddington", "Edgware Road", "West Brompton", "Fulham Broadway", "Parsons Green", "Putney Bridge", "East Putney", "Southfields", "Wimbledon Park", "Wimbledon", "West Kensington", "Barons Court", "Hammersmith", "Ravenscourt Park", "Stamford Brook", "Turnham Green", "Gunnersbury", "Kew Gardens", "Richmond", "Chiswick Park", "Acton Town", "Ealing Common", "Ealing Broadway", "Upminster", "Upminster Bridge", "Hornchurch", "Elm Park", "Dagenham East", "Dagenham Heathway", "Becontree", "Upney", "Barking", "East Ham", "Upton Park", "Plaistow", "West Ham", "Bromley-by-Bow", "Bow Road", "Mile End", "Stepney Green", "Whitechapel", "Aldgate East", "Tower Hill", "Monument", "Cannon Street", "Mansion House", "Blackfriars", "Temple", "Embankment", "Westminster", "St. James's Park", "Victoria", "Sloane Square", "South Kensington", "Gloucester Road", "Earl's Court", "Earl's Court", "High Street Kensington", "Notting Hill Gate", "Bayswater", "Paddington", "Earl's Court", "West Brompton", "Fulham Broadway", "Parsons Green", "Putney Bridge", "East Putney", "Southfields", "Wimbledon Park", "Earl's Court", "West Kensington", "Barons Court", "Hammersmith", "Ravenscourt Park", "Stamford Brook", "Turnham Green", "Gunnersbury", "Kew Gardens", "Turnham Green", "Chiswick Park", "Acton Town", "Ealing Common", "Barking", "East Ham", "Upton Park", "Plaistow", "West Ham", "Bromley-by-Bow", "Bow Road", "Mile End", "Stepney Green", "Whitechapel", "Aldgate East", "Liverpool Street", "Moorgate", "Barbican", "Farringdon", "King's Cross St. Pancras", "Euston Square", "Great Portland Street", "Baker Street", "Edgware Road", "Paddington", "Royal Oak", "Westbourne Park", "Ladbroke Grove", "Latimer Road", "Wood Lane", "Shepherd's Bush Market", "Goldhawk Road", "Hammersmith", "Barking", "East Ham", "Upton Park", "Plaistow", "West Ham", "Bromley-by-Bow", "Bow Road", "Mile End", "Stepney Green", "Whitechapel", "Aldgate East", "Liverpool Street", "Moorgate", "Barbican", "Farringdon", "King's Cross St. Pancras", "Euston Square", "Great Portland Street", "Baker Street", "Edgware Road", "Paddington", "Royal Oak", "Westbourne Park", "Ladbroke Grove", "Latimer Road", "Wood Lane", "Shepherd's Bush Market", "Goldhawk Road", "Stanmore", "Canons Park", "Queensbury", "Kingsbury", "Wembley Park", "Neasden", "Dollis Hill", "Willesden Green", "Kilburn", "West Hampstead", "Finchley Road", "Swiss Cottage", "St. John's Wood", "Baker Street", "Bond Street", "Green Park", "Westminster", "Waterloo", "Southwark", "London Bridge", "Bermondsey", "Canada Water", "Canary Wharf", "North Greenwich", "Canning Town", "West Ham", "Stratford", "Stanmore", "Canons Park", "Queensbury", "Kingsbury", "Wembley Park", "Neasden", "Dollis Hill", "Willesden Green", "Kilburn", "West Hampstead", "Finchley Road", "Swiss Cottage", "St. John's Wood", "Baker Street", "Bond Street", "Green Park", "Westminster", "Waterloo", "Southwark", "London Bridge", "Bermondsey", "Canada Water", "Canary Wharf", "North Greenwich", "Canning Town", "West Ham", "Amersham", "Chesham", "Chalfont & Latimer", "Chorleywood", "Rickmansworth", "Watford", "Croxley", "Uxbridge", "Hillingdon", "Ickenham", "Ruislip", "Ruislip Manor", "Eastcote", "Rayners Lane", "West Harrow", "Harrow-on-the-Hill", "North Harrow", "Pinner", "Northwood Hills", "Northwood", "Moor Park", "Northwick Park", "Preston Road", "Wembley Park", "Finchley Road", "Baker Street", "Great Portland Street", "Euston Square", "King's Cross St. Pancras", "Farringdon", "Barbican", "Moorgate", "Liverpool Street", "Aldgate", "Amersham", "Chesham", "Chalfont & Latimer", "Chorleywood", "Rickmansworth", "Watford", "Croxley", "Uxbridge", "Hillingdon", "Ickenham", "Ruislip", "Ruislip Manor", "Eastcote", "Rayners Lane", "West Harrow", "Harrow-on-the-Hill", "North Harrow", "Pinner", "Northwood Hills", "Northwood", "Moor Park", "Harrow-on-the-Hill", "Harrow-on-the-Hill", "Harrow-on-the-Hill", "Northwick Park", "Preston Road", "Wembley Park", "Finchley Road", "Baker Street", "Great Portland Street", "Euston Square", "King's Cross St. Pancras", "Farringdon", "Barbican", "Moorgate", "Liverpool Street", "High Barnet", "Totteridge & Whetstone", "Woodside Park", "West Finchley", "Mill Hill East", "Finchley Central", "East Finchley", "Highgate", "Archway", "Tufnell Park", "Kentish Town", "Edgware", "Burnt Oak", "Colindale", "Hendon Central", "Brent Cross", "Golders Green", "Hampstead", "Belsize Park", "Chalk Farm", "Camden Town", "Mornington Crescent", "Warren Street", "Goodge Street", "Tottenham Court Road", "Leicester Square", "Charing Cross", "Embankment", "Waterloo", "Euston", "King's Cross St. Pancras", "Angel", "Old Street", "Moorgate", "Bank", "London Bridge", "Borough", "Elephant & Castle", "Kennington", "Oval", "Stockwell", "Clapham North", "Clapham Common", "Clapham South", "Balham", "Tooting Bec", "Tooting Broadway", "Colliers Wood", "South Wimbledon", "Morden", "High Barnet", "Totteridge & Whetstone", "Woodside Park", "West Finchley", "Mill Hill East", "Finchley Central", "East Finchley", "Highgate", "Archway", "Tufnell Park", "Kentish Town", "Edgware", "Burnt Oak", "Colindale", "Hendon Central", "Brent Cross", "Golders Green", "Hampstead", "Belsize Park", "Chalk Farm", "Camden Town", "Mornington Crescent", "Warren Street", "Warren Street", "Goodge Street", "Tottenham Court Road", "Leicester Square", "Charing Cross", "Embankment", "Waterloo", "Euston", "Euston", "King's Cross St. Pancras", "Angel", "Old Street", "Moorgate", "Bank", "London Bridge", "Borough", "Elephant & Castle", "Kennington", "Oval", "Stockwell", "Clapham North", "Clapham Common", "Clapham South", "Balham", "Tooting Bec", "Tooting Broadway", "Colliers Wood", "South Wimbledon", "Cockfosters", "Oakwood", "Southgate", "Arnos Grove", "Bounds Green", "Wood Green", "Turnpike Lane", "Manor House", "Finsbury Park Victoria", "Arsenal", "Holloway Road", "Caledonian Road", "King's Cross St. Pancras", "Russell Square", "Holborn Central", "Covent Garden", "Leicester Square", "Piccadilly Circus", "Green Park", "Hyde Park Corner", "Knightsbridge", "South Kensington", "Gloucester Road", "Earl's Court", "Barons Court", "Hammersmith", "Turnham Green", "Acton Town", "South Ealing", "Northfields", "Boston Manor", "Osterley", "Hounslow East", "Hounslow Central", "Hounslow West", "Hatton Cross", "Heathrow Terminals 1, 2, 3", "Heathrow Terminal 5", "Heathrow Terminal 4", "Ealing Common", "North Ealing", "Park Royal", "Alperton", "Sudbury Town", "Sudbury Hill", "South Harrow", "Rayners Lane", "Eastcote", "Ruislip Manor", "Ruislip", "Ickenham", "Hillingdon", "Uxbridge", "Cockfosters", "Oakwood", "Southgate", "Arnos Grove", "Bounds Green", "Wood Green", "Turnpike Lane", "Manor House", "Finsbury Park Victoria", "Arsenal", "Holloway Road", "Caledonian Road", "King's Cross St. Pancras", "Russell Square", "Holborn Central", "Covent Garden", "Leicester Square", "Piccadilly Circus", "Green Park", "Hyde Park Corner", "Knightsbridge", "South Kensington", "Gloucester Road", "Earl's Court", "Barons Court", "Hammersmith", "Hammersmith", "Turnham Green", "Acton Town", "South Ealing", "Northfields", "Boston Manor", "Osterley", "Hounslow East", "Hounslow Central", "Hounslow West", "Hatton Cross", "Heathrow Terminals 1, 2, 3", "Hatton Cross", "Acton Town", "Ealing Common", "North Ealing", "Park Royal", "Alperton", "Sudbury Town", "Sudbury Hill", "South Harrow", "Rayners Lane", "Eastcote", "Ruislip Manor", "Ruislip", "Ickenham", "Hillingdon", "Walthamstow Central", "Blackhorse Road", "Tottenham Hale", "Seven Sisters", "Finsbury Park", "Highbury & Islington", "King's Cross St. Pancras", "Euston", "Warren Street", "Oxford Circus", "Green Park", "Victoria", "Pimlico", "Vauxhall", "Stockwell", "Brixton", "Walthamstow Central", "Blackhorse Road", "Tottenham Hale", "Seven Sisters", "Finsbury Park", "Highbury & Islington", "King's Cross St. Pancras", "Euston", "Warren Street", "Oxford Circus", "Green Park", "Victoria", "Pimlico", "Vauxhall", "Stockwell", "Bank", "Waterloo", "Bank"]

map = {}
for station in stations:
    map[station] = {}


# Bakerloo Line
map["Harrow & Wealdstone"]["Kenton"]=2
map["Kenton"]["South Kenton"]=2
map["South Kenton"]["North Wembley"]=2
map["North Wembley"]["Wembley Central"]=2
map["Wembley Central"]["Stonebridge Park"]=2
map["Stonebridge Park"]["Harlesden"]=2
map["Harlesden"]["Willesden Junction"]=2
map["Willesden Junction"]["Kensal Green"]=3
map["Kensal Green"]["Queen's Park"]=2
map["Queen's Park"]["Kilburn Park"]=2
map["Kilburn Park"]["Maida Vale"]=2
map["Maida Vale"]["Warwick Avenue"]=1
map["Warwick Avenue"]["Paddington"]=2
map["Paddington"]["Edgware Road"]=2
map["Edgware Road"]["Marylebone"]=1
map["Marylebone"]["Baker Street"]=2
map["Baker Street"]["Regent's Park"]=2
map["Regent's Park"]["Oxford Circus"]=2
map["Oxford Circus"]["Piccadilly Circus"]=2
map["Piccadilly Circus"]["Charing Cross"]=2
map["Charing Cross"]["Embankment"]=1
map["Embankment"]["Waterloo"]=2
map["Waterloo"]["Lambeth North"]=2
map["Lambeth North"]["Elephant & Castle"]=3
# Central Line
map["Epping"]["Theydon Bois"]=3
map["Theydon Bois"]["Debden"]=3
map["Debden"]["Loughton"]=2
map["Loughton"]["Buckhurst Hill"]=3
map["Buckhurst Hill"]["Woodford"]=2
map["Woodford"]["South Woodford"]=3
map["South Woodford"]["Snaresbrook"]=2
map["Snaresbrook"]["Leytonstone"]=2
map["Roding Valley"]["Woodford"]=4
map["Roding Valley"]["Chigwell"]=3
map["Chigwell"]["Grange Hill"]=2
map["Grange Hill"]["Hainault"]=5
map["Hainault"]["Fairlop"]=2
map["Fairlop"]["Barking'side"]=2
map["Barking'side"]["Newbury Park"]=2
map["Newbury Park"]["Gants Hill"]=3
map["Gants Hill"]["Redbridge"]=2
map["Redbridge"]["Wanstead"]=2
map["Wanstead"]["Leytonstone"]=2
map["Leytonstone"]["Leyton"]=2
map["Leyton"]["Stratford"]=3
map["Stratford"]["Mile End"]=4
map["Mile End"]["Bethnal Green"]=2
map["Bethnal Green"]["Liverpool Street"]=3
map["Liverpool Street"]["Bank"]=2
map["Bank"]["St. Paul's"]=2
map["St. Paul's"]["Chancery Lane"]=2
map["Chancery Lane"]["Holborn"]=1
map["Holborn"]["Tottenham"]=2
map["Tottenham"]["Oxford Circus"]=1
map["Oxford Circus"]["Bond Street"]=2
map["Bond Street"]["Marble Arch"]=2
map["Marble Arch"]["Lancaster Gate"]=3
map["Lancaster Gate"]["Queensway"]=2
map["Queensway"]["Notting Hill Gate"]=2
map["Notting Hill Gate"]["Holland Park"]=1
map["Holland Park"]["Shepherd's Bush"]=2
map["Shepherd's Bush"]["White City"]=3
map["White City"]["East Acton"]=3
map["East Acton"]["North Acton"]=2
map["North Acton"]["Hanger Lane"]=3
map["North Acton"]["West Acton"]=2
map["West Acton"]["Ealing Broadway"]=3
map["Hanger Lane"]["Perivale"]=3
map["Perivale"]["Greenford"]=2
map["Greenford"]["Northolt"]=2
map["Northolt"]["South Ruislip"]=3
map["South Ruislip"]["Ruislip Gardens"]=2
map["Ruislip Gardens"]["West Ruislip"]=2
# Circle Line
map["Edgware Road"]["Paddington"]=3
map["Paddington"]["Bayswater"]=2
map["Bayswater"]["Notting Hill Gate"]=2
map["Notting Hill Gate"]["High Street Kensington"]=2
map["High Street Kensington"]["Gloucester Road"]=3
map["Gloucester Road"]["South Kensington"]=3
map["South Kensington"]["Sloane Square"]=2
map["Sloane Square"]["Victoria"]=2
map["Victoria"]["St. James's Park"]=2
map["St. James's Park"]["Westminster"]=2
map["Westminster"]["Embankment"]=1
map["Embankment"]["Temple"]=2
map["Temple"]["Blackfriars"]=1
map["Blackfriars"]["Mansion House"]=2
map["Mansion House"]["Cannon Street"]=2
map["Cannon Street"]["Monument"]=1
map["Monument"]["Tower Hill"]=2
map["Tower Hill"]["Aldgate"]=2
map["Aldgate"]["Liverpool Street"]=3
map["Liverpool Street"]["Moorgate"]=2
map["Moorgate"]["Barbican"]=2
map["Barbican"]["Farringdon"]=1
map["Farringdon"]["King's Cross St. Pancras"]=4
map["King's Cross St. Pancras"]["Euston Square"]=2
map["Euston Square"]["Great Portland Street"]=2
map["Great Portland Street"]["Baker Street"]=2
map["Baker Street"]["Edgware Road"]=3
map["Paddington"]["Royal Oak"]=2
map["Royal Oak"]["Westbourne Park"]=2
map["Westbourne Park"]["Ladbroke Grove"]=2
map["Ladbroke Grove"]["Latimer Road"]=2
map["Latimer Road"]["Wood Lane"]=2
map["Wood Lane"]["Shepherd's Bush Market"]=2
map["Shepherd's Bush Market"]["Goldhawk Road"]=1
map["Goldhawk Road"]["Hammersmith"]=2
# District Line
map["Upminster"]["Upminster Bridge"]=2
map["Upminster Bridge"]["Hornchurch"]=2
map["Hornchurch"]["Elm Park"]=2
map["Elm Park"]["Dagenham East"]=3
map["Dagenham East"]["Dagenham Heathway"]=2
map["Dagenham Heathway"]["Becontree"]=3
map["Becontree"]["Upney"]=2
map["Upney"]["Barking"]=3
map["Barking"]["East Ham"]=4
map["East Ham"]["Upton Park"]=2
map["Upton Park"]["Plaistow"]=2
map["Plaistow"]["West Ham"]=2
map["West Ham"]["Bromley-by-Bow"]=2
map["Bromley-by-Bow"]["Bow Road"]=2
map["Bow Road"]["Mile End"]=2
map["Mile End"]["Stepney Green"]=2
map["Stepney Green"]["Whitechapel"]=3
map["Whitechapel"]["Aldgate East"]=2
map["Aldgate East"]["Tower Hill"]=3
map["Tower Hill"]["Monument"]=2
map["Monument"]["Cannon Street"]=1
map["Cannon Street"]["Mansion House"]=2
map["Mansion House"]["Blackfriars"]=2
map["Blackfriars"]["Temple"]=1
map["Temple"]["Embankment"]=2
map["Embankment"]["Westminster"]=1
map["Westminster"]["St. James's Park"]=2
map["St. James's Park"]["Victoria"]=2
map["Victoria"]["Sloane Square"]=2
map["Sloane Square"]["South Kensington"]=2
map["South Kensington"]["Gloucester Road"]=3
map["Gloucester Road"]["Earl's Court"]=2
map["Earl's Court"]["Kensington (Olympia)"]=3
map["Earl's Court"]["High Street Kensington"]=5
map["High Street Kensington"]["Notting Hill Gate"]=2
map["Notting Hill Gate"]["Bayswater"]=2
map["Bayswater"]["Paddington"]=2
map["Paddington"]["Edgware Road"]=3
map["Earl's Court"]["West Brompton"]=2
map["West Brompton"]["Fulham Broadway"]=2
map["Fulham Broadway"]["Parsons Green"]=2
map["Parsons Green"]["Putney Bridge"]=3
map["Putney Bridge"]["East Putney"]=3
map["East Putney"]["Southfields"]=2
map["Southfields"]["Wimbledon Park"]=2
map["Wimbledon Park"]["Wimbledon"]=4
map["Earl's Court"]["West Kensington"]=2
map["West Kensington"]["Barons Court"]=2
map["Barons Court"]["Hammersmith"]=3
map["Hammersmith"]["Ravenscourt Park"]=2
map["Ravenscourt Park"]["Stamford Brook"]=2
map["Stamford Brook"]["Turnham Green"]=1
map["Turnham Green"]["Gunnersbury"]=3
map["Gunnersbury"]["Kew Gardens"]=2
map["Kew Gardens"]["Richmond"]=4
map["Turnham Green"]["Chiswick Park"]=2
map["Chiswick Park"]["Acton Town"]=2
map["Acton Town"]["Ealing Common"]=2
map["Ealing Common"]["Ealing Broadway"]=5
# Hammersmith & City Line
map["Barking"]["East Ham"]=4
map["East Ham"]["Upton Park"]=2
map["Upton Park"]["Plaistow"]=2
map["Plaistow"]["West Ham"]=2
map["West Ham"]["Bromley-by-Bow"]=2
map["Bromley-by-Bow"]["Bow Road"]=2
map["Bow Road"]["Mile End"]=2
map["Mile End"]["Stepney Green"]=2
map["Stepney Green"]["Whitechapel"]=3
map["Whitechapel"]["Aldgate East"]=2
map["Aldgate East"]["Liverpool Street"]=3
map["Liverpool Street"]["Moorgate"]=2
map["Moorgate"]["Barbican"]=2
map["Barbican"]["Farringdon"]=1
map["Farringdon"]["King's Cross St. Pancras"]=4
map["King's Cross St. Pancras"]["Euston Square"]=2
map["Euston Square"]["Great Portland Street"]=2
map["Great Portland Street"]["Baker Street"]=2
map["Baker Street"]["Edgware Road"]=3
map["Edgware Road"]["Paddington"]=3
map["Paddington"]["Royal Oak"]=2
map["Royal Oak"]["Westbourne Park"]=2
map["Westbourne Park"]["Ladbroke Grove"]=2
map["Ladbroke Grove"]["Latimer Road"]=2
map["Latimer Road"]["Wood Lane"]=2
map["Wood Lane"]["Shepherd's Bush Market"]=2
map["Shepherd's Bush Market"]["Goldhawk Road"]=1
map["Goldhawk Road"]["Hammersmith"]=2
# Jubilee Line
map["Stanmore"]["Canons Park"]=4
map["Canons Park"]["Queensbury"]=3
map["Queensbury"]["Kingsbury"]=2
map["Kingsbury"]["Wembley Park"]=3
map["Wembley Park"]["Neasden"]=4
map["Neasden"]["Dollis Hill"]=2
map["Dollis Hill"]["Willesden Green"]=2
map["Willesden Green"]["Kilburn"]=2
map["Kilburn"]["West Hampstead"]=2
map["West Hampstead"]["Finchley Road"]=1
map["Finchley Road"]["Swiss Cottage"]=2
map["Swiss Cottage"]["St. John's Wood"]=2
map["St. John's Wood"]["Baker Street"]=3
map["Baker Street"]["Bond Street"]=2
map["Bond Street"]["Green Park"]=2
map["Green Park"]["Westminster"]=2
map["Westminster"]["Waterloo"]=2
map["Waterloo"]["Southwark"]=2
map["Southwark"]["London Bridge"]=2
map["London Bridge"]["Bermondsey"]=2
map["Bermondsey"]["Canada Water"]=2
map["Canada Water"]["Canary Wharf"]=3
map["Canary Wharf"]["North Greenwich"]=3
map["North Greenwich"]["Canning Town"]=3
map["Canning Town"]["West Ham"]=3
map["West Ham"]["Stratford"]=2
# Metropolitan Line
map["Amersham"]["Chalfont & Latimer"]=4
map["Chesham"]["Chalfont & Latimer"]=9
map["Chalfont & Latimer"]["Chorleywood"]=4
map["Chorleywood"]["Rickmansworth"]=4
map["Rickmansworth"]["Moor Park"]=5
map["Watford"]["Croxley"]=4
map["Croxley"]["Moor Park"]=4
map["Uxbridge"]["Hillingdon"]=4
map["Hillingdon"]["Ickenham"]=2
map["Ickenham"]["Ruislip"]=2
map["Ruislip"]["Ruislip Manor"]=2
map["Ruislip Manor"]["Eastcote"]=2
map["Eastcote"]["Rayners Lane"]=2
map["Rayners Lane"]["West Harrow"]=3
map["West Harrow"]["Harrow-on-the-Hill"]=2
map["Harrow-on-the-Hill"]["North Harrow"]=3
map["North Harrow"]["Pinner"]=2
map["Pinner"]["Northwood Hills"]=3
map["Northwood Hills"]["Northwood"]=3
map["Northwood"]["Moor Park"]=3
map["Moor Park"]["Harrow-on-the-Hill"]=14
map["Harrow-on-the-Hill"]["Finchley Road"]=16
map["Harrow-on-the-Hill"]["Wembley Park"]=9
map["Harrow-on-the-Hill"]["Northwick Park"]=3
map["Northwick Park"]["Preston Road"]=3
map["Preston Road"]["Wembley Park"]=3
map["Wembley Park"]["Finchley Road"]=7
map["Finchley Road"]["Baker Street"]=5
map["Baker Street"]["Great Portland Street"]=2
map["Great Portland Street"]["Euston Square"]=2
map["Euston Square"]["King's Cross St. Pancras"]=2
map["King's Cross St. Pancras"]["Farringdon"]=2
map["Farringdon"]["Barbican"]=4
map["Barbican"]["Moorgate"]=2
map["Moorgate"]["Liverpool Street"]=2
map["Liverpool Street"]["Aldgate"]=3
# Northern Line
map["High Barnet"]["Totteridge & Whetstone"]=4
map["Totteridge & Whetstone"]["Woodside Park"]=2
map["Woodside Park"]["West Finchley"]=2
map["West Finchley"]["Finchley Central"]=2
map["Mill Hill East"]["Finchley Central"]=4
map["Finchley Central"]["East Finchley"]=4
map["East Finchley"]["Highgate"]=3
map["Highgate"]["Archway"]=3
map["Archway"]["Tufnell Park"]=2
map["Tufnell Park"]["Kentish Town"]=1
map["Kentish Town"]["Camden Town"]=2
map["Edgware"]["Burnt Oak"]=4
map["Burnt Oak"]["Colindale"]=2
map["Colindale"]["Hendon Central"]=3
map["Hendon Central"]["Brent Cross"]=2
map["Brent Cross"]["Golders Green"]=3
map["Golders Green"]["Hampstead"]=4
map["Hampstead"]["Belsize Park"]=3
map["Belsize Park"]["Chalk Farm"]=2
map["Chalk Farm"]["Camden Town"]=1
map["Camden Town"]["Mornington Crescent"]=2
map["Mornington Crescent"]["Euston"]=2
map["Warren Street"]["Euston"]=1
map["Warren Street"]["Goodge Street"]=2
map["Goodge Street"]["Tottenham Court Road"]=1
map["Tottenham Court Road"]["Leicester Square"]=2
map["Leicester Square"]["Charing Cross"]=1
map["Charing Cross"]["Embankment"]=1
map["Embankment"]["Waterloo"]=2
map["Waterloo"]["Kennington"]=3
map["Euston"]["Camden Town"]=4
map["Euston"]["King's Cross St. Pancras"]=2
map["King's Cross St. Pancras"]["Angel"]=3
map["Angel"]["Old Street"]=3
map["Old Street"]["Moorgate"]=2
map["Moorgate"]["Bank"]=2
map["Bank"]["London Bridge"]=2
map["London Bridge"]["Borough"]=2
map["Borough"]["Elephant & Castle"]=2
map["Elephant & Castle"]["Kennington"]=2
map["Kennington"]["Oval"]=3
map["Oval"]["Stockwell"]=2
map["Stockwell"]["Clapham North"]=2
map["Clapham North"]["Clapham Common"]=2
map["Clapham Common"]["Clapham South"]=2
map["Clapham South"]["Balham"]=2
map["Balham"]["Tooting Bec"]=2
map["Tooting Bec"]["Tooting Broadway"]=2
map["Tooting Broadway"]["Colliers Wood"]=2
map["Colliers Wood"]["South Wimbledon"]=2
map["South Wimbledon"]["Morden"]=3
# Picadilly Line
map["Cockfosters"]["Oakwood"]=2
map["Oakwood"]["Southgate"]=3
map["Southgate"]["Arnos Grove"]=4
map["Arnos Grove"]["Bounds Green"]=2
map["Bounds Green"]["Wood Green"]=3
map["Wood Green"]["Turnpike Lane"]=2
map["Turnpike Lane"]["Manor House"]=4
map["Manor House"]["Finsbury Park Victoria"]=2
map["Finsbury Park Victoria"]["Arsenal"]=1
map["Arsenal"]["Holloway Road"]=2
map["Holloway Road"]["Caledonian Road"]=2
map["Caledonian Road"]["King's Cross St. Pancras"]=4
map["King's Cross St. Pancras"]["Russell Square"]=2
map["Russell Square"]["Holborn Central"]=2
map["Holborn Central"]["Covent Garden"]=2
map["Covent Garden"]["Leicester Square"]=1
map["Leicester Square"]["Piccadilly Circus"]=1
map["Piccadilly Circus"]["Green Park"]=2
map["Green Park"]["Hyde Park Corner"]=2
map["Hyde Park Corner"]["Knightsbridge"]=2
map["Knightsbridge"]["South Kensington"]=2
map["South Kensington"]["Gloucester Road"]=2
map["Gloucester Road"]["Earl's Court"]=2
map["Earl's Court"]["Barons Court"]=3
map["Barons Court"]["Hammersmith"]=3
map["Hammersmith"]["Acton Town"]=8
map["Hammersmith"]["Turnham Green"]=4
map["Turnham Green"]["Acton Town"]=4
map["Acton Town"]["South Ealing"]=3
map["South Ealing"]["Northfields"]=1
map["Northfields"]["Boston Manor"]=2
map["Boston Manor"]["Osterley"]=3
map["Osterley"]["Hounslow East"]=2
map["Hounslow East"]["Hounslow Central"]=1
map["Hounslow Central"]["Hounslow West"]=3
map["Hounslow West"]["Hatton Cross"]=4
map["Hatton Cross"]["Heathrow Terminals 1, 2, 3"]=4
map["Heathrow Terminals 1, 2, 3"]["Heathrow Terminal 5"]=4
map["Hatton Cross"]["Heathrow Terminal 4"]=3
map["Acton Town"]["Ealing Common"]=2
map["Ealing Common"]["North Ealing"]=2
map["North Ealing"]["Park Royal"]=2
map["Park Royal"]["Alperton"]=2
map["Alperton"]["Sudbury Town"]=3
map["Sudbury Town"]["Sudbury Hill"]=2
map["Sudbury Hill"]["South Harrow"]=3
map["South Harrow"]["Rayners Lane"]=5
map["Rayners Lane"]["Eastcote"]=2
map["Eastcote"]["Ruislip Manor"]=2
map["Ruislip Manor"]["Ruislip"]=2
map["Ruislip"]["Ickenham"]=4
map["Ickenham"]["Hillingdon"]=2
map["Hillingdon"]["Uxbridge"]=4
# Victoria Line
map["Walthamstow Central"]["Blackhorse Road"]=3
map["Blackhorse Road"]["Tottenham Hale"]=3
map["Tottenham Hale"]["Seven Sisters"]=2
map["Seven Sisters"]["Finsbury Park"]=5
map["Finsbury Park"]["Highbury & Islington"]=2
map["Highbury & Islington"]["King's Cross St. Pancras"]=3
map["King's Cross St. Pancras"]["Euston"]=2
map["Euston"]["Warren Street"]=2
map["Warren Street"]["Oxford Circus"]=2
map["Oxford Circus"]["Green Park"]=2
map["Green Park"]["Victoria"]=2
map["Victoria"]["Pimlico"]=2
map["Pimlico"]["Vauxhall"]=2
map["Vauxhall"]["Stockwell"]=3
map["Stockwell"]["Brixton"]=2
# Waterloo & City Line
map["Bank"]["Waterloo"]=5


class plot(object):
    def __init__(self, stations, map):
        self.stations = stations
        self.plot = self.construct_plot(stations, map)

    def construct_plot(self, stations, map):
        # This will make sure that the plot graph is symetrical. If there's a path from one station to another station with a value of V, there must be a path from station B to station A with the value of V.
        plot = {}
        for station in stations:
            plot[station] = {}

        plot.update(map)

        for station, edges in plot.items():
            for adjacent_station, value in edges.items():
                if plot[adjacent_station].get(station, False) == False:
                    plot[adjacent_station][station] = value

        return plot


    def get_stations(self):
        # Returns the station from the graph.
        return self.stations

    def get_outgoing_edges(self, station):
        # This will return the adjacent stations.
        connections = []
        for out_station in self.stations:
            if self.plot[station].get(out_station, False) != False:
                connections.append(out_station)
        return connections

    def value(self, station1, station2):
        # This will show the value between each station.
        return self.plot[station1][station2]


def dijkstra_algorithm(plot, start_station):
    not_visited = list(plot.get_stations())

    # This part of the code will store the cost it takes to visit each station and then update this value as the we move through the map. 
    min_path = {}

    # This value will store the last stations that were visitied.
    last_station = {}


    # We assign a max value in order to state the value of unvisited stations so none are missed.
    inf = sys.maxsize
    for station in not_visited:
        min_path[station] = inf
    # The station we start with has to start with a zero.
    min_path[start_station] = 0

    # This loop will keep running until all the stations and number of routes have been calculated.
    while not_visited:
        # Method to find the stations that will cost less.
        current_min_station = None
        for station in not_visited:  # Iterate over the stations that were not visited.
            if current_min_station == None:
                current_min_station = station
            elif min_path[station] < min_path[current_min_station]:
                current_min_station = station

        
        # This part of the code finds and works out adjacent stations next to each other and their distances. 
        adjacents = plot.get_outgoing_edges(current_min_station)
        # Loop will iterate for the number of times a station has an adjacent station.
        for adjacent in adjacents:
            tentative_value = min_path[current_min_station] + plot.value(current_min_station, adjacent)
            if tentative_value < min_path[adjacent]:
                min_path[adjacent] = tentative_value
                # We also update the best path to the current station.
                last_station[adjacent] = current_min_station

        # After we have travelled to all the adjacent station we then mark this station as we have visited.
        # All this does is remove the station that we just were on so we do not come across it again. 
        not_visited.remove(current_min_station)

    return last_station, min_path


def print_result(last_station, min_path, start_station, target_station):
    path = []
    station = target_station

    while station != start_station:
        path.append(station)
        station = last_station[station]

    # Add the start station manually.
    path.append(start_station)

    print("We found the following best path that will take the time of {} minutes.".format(min_path[target_station]))
    print(" -> ".join(reversed(path)))
    
plot = plot(stations, map)

# This will get the input of the user and present a prompt for them to enter what stations they would like to use.

start = input("Where would you like to start? ")
end = input("Where would you like to finish? ")

# This will print an error if not recognised in the graph.

if start not in stations or end not in stations:
    print("error")

else:

    last_station, min_path = dijkstra_algorithm(plot=plot, start_station=start)

    # This will print the result of the stations input by the user.
    print_result(last_station, min_path, start_station=start, target_station=end)

