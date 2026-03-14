# --- TRICODE OFFICIAL WHITE PAPER & INTERPRETER ---
# Author: Aaris
# Logic: Ternary Base-3 (0, 1, 2)
# Date: 2026-03-14

"""
DESCRIPTION:
TriCode is a custom encoding system that moves beyond traditional Binary (0,1).
By using three states (0, 1, 2), it explores the efficiency of Ternary Logic.

LOGIC MAPPING:
0 = Ground / Neutral
1 = Mid / Positive
2 = High / Peak
"""

# The TriCode Dictionary
tc_map = {
    'A':'001', 'B':'002', 'C':'010', 'D':'011', 'E':'012',
    'F':'020', 'G':'021', 'H':'022', 'I':'100', 'J':'101',
    'K':'102', 'L':'110', 'M':'111', 'N':'112', 'O':'120',
    'P':'121', 'Q':'122', 'R':'200', 'S':'201', 'T':'202',
    'U':'210', 'V':'211', 'W':'212', 'X':'220', 'Y':'221', 'Z':'222',
    'a':'0011', 'b':'0022', 'c':'0100', 'd':'0111', 'e':'0122',
    'f':'0200', 'g':'0211', 'h':'0222', 'i':'1000', 'j':'1011',
    'k':'1022', 'l':'1100', 'm':'1111', 'n':'1122', 'o':'1200',
    'p':'1211', 'q':'1222', 'r':'2000', 's':'2011', 't':'2022',
    'u':'2100', 'v':'2111', 'w':'2122', 'x':'2200', 'y':'2211', 'z':'2222',
    ' ':'000', '.':'1111', '?':'2222'
}

def translate_to_tricode(text):
    return "-".join([tc_map.get(c, '???') for c in text])

# Official Launch Message
print("--- TRICODE SYSTEM ONLINE ---")
print("Developer: Aaris")
print("Status: Official Repository Created")
