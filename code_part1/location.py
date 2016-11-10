import re

states = {
        'AK': ['Alaska', ',Ak', 'alaska'],
        'AL': ['Alabama', ',Al', 'alabama'],
        'AR': ['Arkansas', ',Ar', 'arkansas'],
        'AZ': ['Arizona', ',Az', 'arizona'],
        'CA': ['California', ',Ca', 'california'],
        'CO': ['Colorado', ',Co', 'colorado'],
        'CT': ['Connecticut', ',Ct', 'connecticut'],
        'DC': ['D.C.', 'District of Columbia', 'Washington DC'],
        'DE': ['Delaware', ',De', 'delaware'],
        'FL': ['Florida', ',Fl', 'florida'],
        'GA': ['Georgia', ',Ga', 'georgia'],
        'HI': ['Hawaii', ',Hi', 'hawaii'],
        'IA': ['Iowa', ',Ia', 'iowa'],
        'ID': ['Idaho', ',Id', 'idaho'],
        'IL': ['Illinois', ',Il', 'illinois'],
        'IN': ['Indiana', ',In', 'indiana'],
        'KS': ['Kansas', ',Ks', 'kansas'],
        'KY': ['Kentucky', ',Ky', 'kentucky'],
        'LA': ['Louisiana', ',La', 'louisiana'],
        'MA': ['Massachusetts', ',Ma', 'massachusetts'],
        'MD': ['Maryland', ',Md', 'maryland'],
        'ME': ['Maine' , ',Me', 'maine'],
        'MI': ['Michigan', ',Mi', 'michigan'],
        'MN': ['Minnesota', ',Mn', 'minnesota'],
        'MO': ['Missouri', ',Mo', 'missouri'],
        'MS': ['Mississippi', ',Ms', 'mississippi'],
        'MT': ['Montana', ',Mt', 'montana'],
        'NC': ['North Carolina', ',Nc', 'north carolina'],
        'ND': ['North Dakota', ',Nd', 'north dakota'],
        'NE': ['Nebraska', ',Ne', 'nebraska'],
        'NH': ['New Hampshire', ',Nh', 'new hampshire'],
        'NJ': ['New Jersey', ',Nj', 'new jersey'],
        'NM': ['New Mexico', ',Nm', 'new mexico'],
        'NV': ['Nevada', ',Nv', 'nevada'],
        'NY': ['New York', ',Ny', 'new york'],
        'OH': ['Ohio', ',Oh', 'ohio'],
        'OK': ['Oklahoma', ',Ok', 'oklahoma'],
        'OR': ['Oregon', ',Or', 'oregon'],
        'PA': ['Pennsylvania', ',Pa', 'pennsylvania'],
        'RI': ['Rhode Island', ',Ri', 'rhode island'],
        'SC': ['South Carolina', ',Sc', 'south carolina'],
        'SD': ['South Dakota', ',Sd', 'south dakota'],
        'TN': ['Tennessee', ',Tn', 'tennessee'],
        'TX': ['Texas', ',Tx', 'texas'],
        'UT': ['Utah', ',Ut', 'utah'],
        'VA': ['Virginia', ',Va', 'virginia'],
        'VT': ['Vermont', ',Vt', 'vermont'],
        'WA': ['Washington', ',Wa', 'washington'],
        'WI': ['Wisconsin', ',Wi', 'wisconsin'],
        'WV': ['West Virginia', ',Wv', 'west virgnia'],
        'WY': ['Wyoming', ',Wy', 'wyoming'],
    }

def location(value, abb, other_criteria=None):
    regex1 = re.compile(abb)
    regex2 = re.compile(other_criteria[0])
    regex3 = re.compile(other_criteria[1])
    regex4 = re.compile(other_criteria[2])
    if regex1.search(value) is not None:
        return abb
    elif regex2.search(value) is not None:
        return abb
    elif regex3.search(value) is not None:
        return abb
    elif regex4.search(value) is not None:
        return abb
    else:
        return value
