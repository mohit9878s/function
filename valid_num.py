# valid mobile number function

def valid_num(number,starting_first_digit=0):
    """
        valid number example
                ["7065333302", "919966666247",
                "917077777802.0", "9871888834.0"]

        valid number clean 
        
        invalid number example 
                ["119998888808", "959999988860",
                "919873310545.1", "1519310057759.0"]

        invalid number convert in 0                 
    """

    num = str(number)
    num_1st_str=str(starting_first_digit)
    if num.endswith(".0"):
        num = num.replace(".0", "")
    if (len(num) == 12 and num[:2] == '91') or len(num) == 10:
        num = num[-10:]
        try:
            num = int(num)
        except ValueError:
            return 0
        if str(num)[:1] > num_1st_str:
            return num
        else:
            return 0
    else:
        return 0
if __name__ == "__main__":
    valid_num()
