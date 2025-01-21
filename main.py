from develop import utils


def main():
    OPERATIONS_URL = "https://www.jsonkeeper.com/b/VK9M"
    data, info = utils.get_operations_url(OPERATIONS_URL)
    if not data:
        print(info)
        exit()
    else:
        print(info)
    write_info, write_data_path = utils.write_requested_data('new_transactions', data)
    print(write_info)
    print(write_data_path)
    my_num_of_operations = int(input("Введите количество желаемых операций: "))
    my_order = input("Тип сортировки прямая/обратная (по умолчанию обратная): ")
    all_operations = utils.get_local_operations(write_data_path)
    # all_operations = utils.get_local_operations(r'transactions\my_transactions.json')
    operations_executed = utils.get_operations_executed(all_operations)
    operations_from = utils.get_operations_with_from(operations_executed)
    operations_last = utils.get_last_num_of_operations(operations_from, my_num_of_operations, my_order)
    operations_formatted = utils.get_formatted_operations(operations_last)
    [print(f"{formatted}\n") for formatted in operations_formatted]


if __name__ == "__main__":
    main()
