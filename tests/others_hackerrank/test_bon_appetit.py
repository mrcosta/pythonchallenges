def check_overcharge(total_and_declined_item, list_of_prices, charged):
    index_declined_item = int(total_and_declined_item.split(" ")[1])
    prices_in_int = [int(i) for i in list_of_prices.split()]
    sum_price_without_declined_item = sum(prices_in_int) - prices_in_int[index_declined_item]
    bill_split_by_two = sum_price_without_declined_item / 2
    difference = int(charged) - bill_split_by_two
    print(bill_split_by_two)

    return difference if bill_split_by_two != float(charged) else 'Bon Appetit'

def test_incorrect_change_to_friend():
    total_and_declined_item = '4 1'
    list_of_prices = '3 10 2 9'
    charged = '12'

    assert check_overcharge(total_and_declined_item, list_of_prices, charged) == 5

def test_correct_change_to_friend():
    total_and_declined_item = '4 1'
    list_of_prices = '3 10 2 9'
    charged = '7'

    assert check_overcharge(total_and_declined_item, list_of_prices, charged) == 'Bon Appetit'

# hacker_rank read from input:
# total_and_declined_item = input()
# list_of_prices = input()
# charged = input()
