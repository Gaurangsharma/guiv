for _ in range(int(input())):
    rupee=int(input())
    tax_slab=[0,.05,.10,.15,.20,.25,.30]
    tax_amount=[0,12.5,37.5,75,125,187.5]
    new_rupee=0
    if rupee>250000:
        new_rupee=rupee
        new_rupee-=(rupee-250000)*tax_slab[1]
        new_rupee-=tax_amount[0]*1000
        if rupee>500000:
            new_rupee=rupee
            new_rupee-=(rupee-500000)*tax_slab[2]
            new_rupee-=tax_amount[1]*1000
            if rupee>750000:
                new_rupee=rupee
                new_rupee-=(rupee-750000)*tax_slab[3]
                new_rupee-=tax_amount[2]*1000
                if rupee>1000000:
                    new_rupee=rupee
                    new_rupee-=(rupee-1000000)*tax_slab[4]
                    new_rupee-=tax_amount[3]*1000
                    if rupee>1250000:
                        new_rupee=rupee
                        new_rupee-=(rupee-1250000)*tax_slab[5]
                        new_rupee-=tax_amount[4]*1000
                        if rupee>1500000:
                            new_rupee=rupee
                            new_rupee-=(rupee-1500000)*tax_slab[6]
                            new_rupee-=tax_amount[5]*1000
                            print(int(new_rupee))
                        else:
                            print(int(new_rupee))
                    else:
                        print(int(new_rupee))
                else:
                    print(int(new_rupee))
            else:
                print(int(new_rupee))    
        else:
            print(int(new_rupee))        
    else:
        print(rupee)