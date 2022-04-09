def coconut_translator(txt):
    a_byte_array = bytearray(txt,"utf8")
    byte_list = []
    a ="coconuts"
    coco_list = []
    coco_list_2 = []


    for byte in a_byte_array:
        binary_representation = bin(byte)
        if len(binary_representation)==8:
            byte_list.append("0"+binary_representation[0]+binary_representation[2:])
        else:
            byte_list.append(binary_representation[0]+binary_representation[2:])



    for a in range(len(byte_list)):
        coco_list_2.append("")


    for a in range(len(byte_list)):
        coco_list.append("coconuts")

    for a in range(len(byte_list)):
        for i in range(8):
            if byte_list[a][i]=="1":
                coco_list_2[a] += coco_list[a][i].upper()
            else:
                coco_list_2[a] += coco_list[a][i]


    return " ".join(coco_list_2)


print(coconut_translator("123")) ## Melih Çeliktaş



