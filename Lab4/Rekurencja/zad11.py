def odwrocony_string(s):
    if len(s) <= 1:
        return s
    else:
        return odwrocony_string(s[1:]) + s[0]


text = "programowanie"
odwrocony_text = odwrocony_string(text)
print("Oryginalny string:", text)
print("Odwrócony string:", odwrocony_text)



