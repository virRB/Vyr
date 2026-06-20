import modules.rand as rand
Guy = {
    "name": "Vir"
}
Other = {
    "name": "Bob"
}
def alwaysTrue():
    return True
def alwaysFalse():
    return False
print("=== TEST 1: Basic if without /+ ===")
if True:
    print("PASS 1")
else:
    print("FAIL 1")
print("=== TEST 2: Basic if with not ===")
if not False:
    print("PASS 2")
else:
    print("FAIL 2")
print("=== TEST 3: Data comparison with /+ ===")
if Guy["name"] == "Vir":
    print("PASS 3")
else:
    print("FAIL 3")
print("=== TEST 4: Two /+ blocks ===")
if Guy["name"] == Guy["name"]:
    print("PASS 4")
else:
    print("FAIL 4")
print("=== TEST 5: Different data values ===")
if Guy["name"] == Other["name"]:
    print("FAIL 5")
else:
    print("PASS 5")
print("=== TEST 6: Function call in /+ ===")
if alwaysTrue():
    print("PASS 6")
else:
    print("FAIL 6")
print("=== TEST 7: not + function call ===")
if not alwaysFalse():
    print("PASS 7")
else:
    print("FAIL 7")
print("=== TEST 8: if /+ then othif without /+ ===")
if False:
    print("FAIL 8A")
elif True:
    print("PASS 8")
else:
    print("FAIL 8B")
print("=== TEST 9: if without /+, othif with /+ ===")
if False:
    print("FAIL 9A")
elif     alwaysTrue():
    print("PASS 9")
else:
    print("FAIL 9B")
print("=== TEST 10: if with /+, othif with /+ ===")
if alwaysFalse():
    print("FAIL 10A")
elif     alwaysTrue():
    print("PASS 10")
else:
    print("FAIL 10B")
print("=== TEST 11: otherwise path ===")
if False:
    print("FAIL 11A")
elif False:
    print("FAIL 11B")
else:
    print("PASS 11")
print("=== TEST 12: Random expression parsing ===")
if rand.pick(1, 1) == 1:
    print("PASS 12")
else:
    print("FAIL 12")
print("=== TEST 13: not with data comparison ===")
if not Guy["name"] == "Bob":
    print("PASS 13")
else:
    print("FAIL 13")
print("=== TEST 14: nested chain ===")
if False:
    print("FAIL 14A")
elif False:
    print("FAIL 14B")
elif Guy["name"] == "Vir":
    print("PASS 14")
else:
    print("FAIL 14C")
print("=== TEST COMPLETE ===")
