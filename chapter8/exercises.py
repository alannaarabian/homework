prefixes = "JKLMNOPQ"
suffix = "ack"

for p in prefixes:
    if p == "O" or p == "Q":
        print(p+"u"+suffix)
    else:
      print(p + suffix)


