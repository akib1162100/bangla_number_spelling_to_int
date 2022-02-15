bn_num = ['শূন্য', 'এক', 'দুই', 'তিন', 'চার', 'পাঁচ', 'ছয়', 'সাত', 'আট', 'নয়', 'দশ', 'এগারো', 'বারো', 'তেরো', 'চৌদ্দ', 'পনেরো', 'ষোল', 'সতেরো', 'আঠারো', 'উনিশ','বিশ','একুশ', 'বাইশ', 'তেইশ', 'চব্বিশ', 'পঁচিশ', 'ছাব্বিশ', 'সাতাশ', 'আঠাশ', 'ঊনত্রিশ', 'ত্রিশ', 'একত্রিশ', 'বত্রিশ', 'তেত্রিশ', 'চৌত্রিশ', 'পঁয়ত্রিশ', 'ছত্রিশ', 'সাঁইত্রিশ', 'আটত্রিশ', 'ঊনচল্লিশ','চল্লিশ','একচল্লিশ', 'বিয়াল্লিশ', 'তেতাল্লিশ', 'চুয়াল্লিশ', 'পঁয়তাল্লিশ', 'ছেচল্লিশ', 'সাতচল্লিশ', 'আটচল্লিশ', 'ঊনপঞ্চাশ', 'পঞ্চাশ', 'একান্ন','বাহান্ন', 'তিপ্পান্ন', 'চুয়ান্ন', 'পঞ্চান্ন', 'ছাপ্পান্ন', 'সাতান্ন', 'আটান্ন', 'ঊনষাট','ষাট','একষট্টি', 'বাষট্টি', 'তেষট্টি', 'চৌষট্টি', 'পঁয়ষট্টি', 'ছেষট্টি', 'সাতষট্টি', 'আটষট্টি', 'ঊনসত্তর', 'সত্তর', 'একাত্তর','বাহাত্তর', 'তিয়াত্তর', 'চুয়াত্তর', 'পঁচাত্তর', 'ছিয়াত্তর', 'সাতাত্তর', 'আটাত্তর', 'ঊনআশি','আশি','একাশি', 'বিরাশি', 'তিরাশি', 'চুরাশি','পঁচাশি', 'ছিয়াশি', 'সাতাশি', 'আটাশি', 'ঊননব্বই', 'নব্বই', 'একানব্বই','বিরানব্বই', 'তিরানব্বই', 'চুরানব্বই', 'পঁচানব্বই', 'ছিয়ানব্বই', 'সাতানব্বই', 'আটানব্বই', 'নিরানব্বই']
positional= ['কোটি','লক্ষ','হাজার','শত']
positional_dict={'শত':2,'হাজার':3,'লক্ষ':5,'কোটি':7}
# hundreds=['একশ','দুইশ','তিনশ','চারশ','পাঁচশ','ছয়শ','সাতশ','আটশ','নয়শ','দশশ','এগারশো','বারোশো','তেরোশো','চদ্দশো','পনেরোশো','ষোলশো','সতেরোশো','আঠারশো','উনিশশো']
bn_num_dict={}
all_kWords=[]
all_kWords.extend(positional)
# all_kWords.extend(hundreds)
all_kWords.extend(bn_num)
for i in range(len(bn_num)):
    bn_num_dict[bn_num[i]]=i

def int_spell_by_part(remainder):
    part_spelling = ""
    # if remainder >10**7:
    #     crore = remainder//(10**7)
    #     part_spelling =  bn_num[crore] + " কোটি " + part_spelling
    #     remainder = remainder%(10**7)
    if remainder >10**5:
        lac = remainder//(10**5)
        part_spelling =   part_spelling + bn_num[lac] + " লক্ষ "
        remainder = remainder%(10**5)
    if remainder >10**3:
        hazar = remainder//(10**3)
        part_spelling =  part_spelling + bn_num[hazar] + " হাজার " 
        remainder = remainder%(10**3)
    if remainder >10**2:
        shata = remainder//(10**2)
        part_spelling =  part_spelling + bn_num[shata] + " শত "
        remainder = remainder%(10**2)
    if remainder :
        part_spelling =   part_spelling + bn_num[remainder]+" " 
    return part_spelling

def int_to_spell(number):
    spelling = ""
    koti_flag = False
    while number:
        part_spelling = int_spell_by_part(number%(10**7))
        if not koti_flag:
            spelling = part_spelling + spelling
        if koti_flag:
            spelling = part_spelling + " কোটি " + spelling
        number = number//(10**7)
        koti_flag = True
    return spelling

number = int(input("Enter a number: "))
print(int_to_spell(number))