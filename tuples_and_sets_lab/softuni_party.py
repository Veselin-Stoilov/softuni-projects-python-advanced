def is_vip_guest(guest_name):
    return guest_name[0].isdigit


n = int(input())
guest_list = set()

for _ in range(n):
    invited_name = input()
    guest_list.add(invited_name)

guest = input()
while guest != 'END':
    if guest in guest_list:
        guest_list.remove(guest)
    guest = input()

vip_list = set([g for g in guest_list if is_vip_guest(g)])
guest_list = set([g for g in guest_list if not is_vip_guest(g)])

print(len(guest_list) + len(vip_list))

for name in sorted(vip_list):
    print(name)
for name in sorted(guest_list):
    print(name)

