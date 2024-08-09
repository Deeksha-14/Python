def rot13(s):
    result = []
    for v in s:
        if 'a' <= v <= 'z':
            result.append(chr((ord(v) - ord('a') + 13) % 26 + ord('a')))
        elif 'A' <= v <= 'Z':
            result.append(chr((ord(v) - ord('A') + 13) % 26 + ord('A')))
        else:
            result.append(v)
    return ''.join(result)

decoded_string = "1c$721E\M1+>bks1c$721E\M1+>bks1c$721E\\4+>ttt1c$741*AD0+>bks1c$741*AD0+>bks1c$721E\M1+>bks1c$741*AD0+>bks1c$721E\M1+>bks1c$721E\M1+>bks2D?730H`8-+>tnr1c6C91E\S2+>ttt2DQC32'=_5+>bqu1c?I51E\M4+>bqu1c6C42'=_6+>bks1c$722BXn5+>bqu1c6C42'=_5+>bqu1c?I70H`21+>ttt1c6C42'=_5+>bqu1c6C42'=_5+>bqu1c6C42'=_5+>bu!2D?711E\M1+>bks1c?I71*AD0+>bks1c$721E\M1+>bks1c$721E\M1+>bks1c$722BXn3+>bu!1c$721E\M1+>bks1c$721E\M4+>bqu1c6C42'=_5+>bqu1c6C42'=_5+>bqu1c6C42'=_6+>bks1c$721E\M1+>bks1c$722BXn5+>bks1c$721E\M1+>bks1c$721E\M1+>bks1c$721E\M1+>bks1c$721E\M1+>bks1c$721E\M1+>bks1c$721E\M1+>bks1c$721E\M1+>bu!2D?711E\M1+>bks1c$721E\M1+>bks1c$721E\M1+>bks1c?I51E\M1+>bu!1c$721E\M4+>bqu1c6C42'=_5+>bqu1c6C42'=_5+>bqu1c?I51E\M4+>bqu1c6C42'=_5+>bqu1c6C42'=_5+>bqu1c6C42BXh4+>bks1c$721E\M1+>bks1c$721E\M1+>bks1c$721E\M1+>bks1c$721E\M1+>bks1c?I52'=_5+>bqu1c6C42BXh6+>bqu1c6C42'=_5+>bqu1c6C42'=_5+>bqu1c6C42'=_5+>bu!1c$721E\M1+>bks1c$721E\M4+>ttt1c$721E\M4"
rot13_output = rot13(decoded_string)

print(rot13_output)
