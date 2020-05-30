class Sol:
    def has_alternative_bits(self,n):
        bin_num=''
        while n>1:
            bin_num+=str(n%2)
            if len(bin_num)>1 and bin_num[-1]==bin_num[-2]:
                return False
            n=n//2
        bin_num+='1'
        if len(bin_num) > 1 and bin_num[-1] == bin_num[-2]:
            return False
        return True

if __name__ == '__main__':
    p=Sol()
    print(p.has_alternative_bits(3))
