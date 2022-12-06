hex_to_bin = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}

input = '''8054F9C95F9C1C973D000D0A79F6635986270B054AE9EE51F8001D395CCFE21042497E4A2F6200E1803B0C20846820043630C1F8A840087C6C8BB1688018395559A30997A8AE60064D17980291734016100622F41F8DC200F4118D3175400E896C068E98016E00790169A600590141EE0062801E8041E800F1A0036C28010402CD3801A60053007928018CA8014400EF2801D359FFA732A000D2623CADE7C907C2C96F5F6992AC440157F002032CE92CE9352AF9F4C0119BDEE93E6F9C55D004E66A8B335445009E1CCCEAFD299AA4C066AB1BD4C5804149C1193EE1967AB7F214CF74752B1E5CEDC02297838C649F6F9138300424B9C34B004A63CCF238A56B71520142A5A7FC672E5E00B080350663B44F1006A2047B8C51CC80286C0055253951F98469F1D86D3C1E600F80021118A124261006E23C7E8260008641A8D51F0C01299EC3F4B6A37CABD80252211221A600BC930D0057B2FAA31CDCEF6B76DADF1666FE2E000FA4905CB7239AFAC0660114B39C9BA492D4EBB180252E472AD6C00BF48C350F9F47D2012B6C014000436284628BE00087C5D8671F27F0C480259C9FE16D1F4B224942B6F39CAF767931CFC36BC800EA4FF9CE0CCE4FCA4600ACCC690DE738D39D006A000087C2A89D0DC401987B136259006AFA00ACA7DBA53EDB31F9F3DBF31900559C00BCCC4936473A639A559BC433EB625404300564D67001F59C8E3172892F498C802B1B0052690A69024F3C95554C0129484C370010196269D071003A079802DE0084E4A53E8CCDC2CA7350ED6549CEC4AC00404D3C30044D1BA78F25EF2CFF28A60084967D9C975003992DF8C240923C45300BE7DAA540E6936194E311802D800D2CB8FC9FA388A84DEFB1CB2CBCBDE9E9C8803A6B00526359F734673F28C367D2DE2F3005256B532D004C40198DF152130803D11211C7550056706E6F3E9D24B0'''
test = '''C200B40A82'''

b = ''.join([hex_to_bin[char] for char in input])
part_1 = 0


def operate(t, results, number):
    if t == 0:
        return sum(results)
    elif t == 1:
        p = 1
        for r in results:
            p *= r
        return p
    elif t == 2:
        return min(results)
    elif t == 3:
        return max(results)
    elif t == 5:
        if results[0] > results[1]:
            return 1
        else:
            return 0
    elif t == 6:
        if results[0] < results[1]:
            return 1
        else:
            return 0
    elif t == 7:
        if results[0] == results[1]:
            return 1
        else:
            return 0


def read_packet(binary):
    global part_1
    v = int(binary[:3], base=2)
    part_1 += v
    t = int(binary[3:6], base=2)

    # Version 4
    if t == 4:
        j = 0
        packets = binary[6:]
        number = ''
        while True:
            try:
                bits = packets[j+1:j+5]
                if len(bits) == 4:
                    number += str(packets[j+1:j+5])
                if packets[j] == '0':
                    break
                j += 5
            except:
                break
        return len(binary[:j+11]), int(number, base=2)

    # Other versions
    else:
        try:
            len_type = int(binary[6])

            # length type is 1 -> 11
            if len_type:
                subpackets = int(binary[7:18], base=2)
                length = 0
                results = []
                for _ in range(subpackets):
                    j, number = read_packet(binary[length + 18:])
                    length += j
                    results.append(number)
                result = operate(t, results, number)
                return length+18, result

            # length type is 0 -> 15
            else:
                length = int(binary[7:22], base=2)
                current_length = 0
                result = 0
                results = []
                while current_length < length:
                    j, number = read_packet(binary[current_length + 22:])
                    current_length += j
                    results.append(number)
                result = operate(t, results, number)
                return current_length+22, result
        except:
            print('ERror')


print(read_packet(b))
