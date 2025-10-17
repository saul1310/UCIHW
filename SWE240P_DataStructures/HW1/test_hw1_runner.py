from HW1 import LinkedList, Node


def reset_node_state():
    Node._currentIDNum = 0
    Node._free_ids = []


def bank_state(bank: LinkedList):
    """Serialize bank to list of dicts for clear comparison."""
    out = []
    cur = bank.head
    while cur:
        out.append({
            'id': cur.id,
            'name': cur.name,
            'address': cur.address,
            'ss': cur.ss,
            'balance': cur.balance,
        })
        cur = cur.next
    return out


def print_test_result(name, before, after, expected):
    match = after == expected
    print("\n1: Name of test:", name)
    print("2: before input:", before)
    print("3: input after test has been done:", after)
    print("4: expected input:", expected)
    print("5: check if result matches expected input:", match)
    return match


def test_add_basic():
    reset_node_state()
    bank = LinkedList()
    before = bank_state(bank)

    bank.addUser('A', 'AddrA', 111, 10)
    bank.addUser('B', 'AddrB', 222, 20)
    bank.addUser('C', 'AddrC', 333, 30)

    after = bank_state(bank)
    expected = [
        {'id': 0, 'name': 'A', 'address': 'AddrA', 'ss': 111, 'balance': 10},
        {'id': 1, 'name': 'B', 'address': 'AddrB', 'ss': 222, 'balance': 20},
        {'id': 2, 'name': 'C', 'address': 'AddrC', 'ss': 333, 'balance': 30},
    ]
    return print_test_result('add_basic', before, after, expected)


def test_delete_and_reuse():
    reset_node_state()
    bank = LinkedList()
    bank.addUser('A', 'AddrA', 111, 10)
    bank.addUser('B', 'AddrB', 222, 20)
    bank.addUser('C', 'AddrC', 333, 30)
    before = bank_state(bank)

    bank.deleteUser(1)  # delete B
    # after deletion add new user, should reuse id 1
    new_id = bank.addUser('D', 'AddrD', 444, 40)
    after = bank_state(bank)
    expected = [
        {'id': 0, 'name': 'A', 'address': 'AddrA', 'ss': 111, 'balance': 10},
        {'id': 1, 'name': 'D', 'address': 'AddrD', 'ss': 444, 'balance': 40},
        {'id': 2, 'name': 'C', 'address': 'AddrC', 'ss': 333, 'balance': 30},
    ]
    return print_test_result('delete_and_reuse', before, after, expected)


def test_pay_transfer():
    reset_node_state()
    bank = LinkedList()
    id0 = bank.addUser('Payer', 'Addr0', 101, 50)
    id1 = bank.addUser('Payee', 'Addr1', 102, 20)
    before = bank_state(bank)

    bank.payUserToUser(id0, id1, 15)
    after = bank_state(bank)
    expected = [
        {'id': id0, 'name': 'Payer', 'address': 'Addr0', 'ss': 101, 'balance': 35},
        {'id': id1, 'name': 'Payee', 'address': 'Addr1', 'ss': 102, 'balance': 35},
    ]
    return print_test_result('pay_transfer', before, after, expected)


def test_get_median_odd_even():
    # odd case
    reset_node_state()
    bank = LinkedList()
    for i in range(5):
        bank.addUser(f'u{i}', f'a{i}', 100 + i, 10)
    before_odd = bank_state(bank)
    median_odd = bank.getMedianID()

    # even case
    reset_node_state()
    bank2 = LinkedList()
    for i in range(4):
        bank2.addUser(f'v{i}', f'b{i}', 200 + i, 5)
    before_even = bank_state(bank2)
    median_even = bank2.getMedianID()

    after = {'median_odd': median_odd, 'median_even': median_even}
    expected = {'median_odd': 2, 'median_even': (1 + 2) / 2}
    return print_test_result('get_median_odd_even', {'odd': before_odd, 'even': before_even}, after, expected)


def test_merge_accounts():
    reset_node_state()
    bank = LinkedList()
    id1 = bank.addUser('Sam', 'Addr', 111, 40)
    id2 = bank.addUser('Sam', 'Addr', 111, 60)
    before = bank_state(bank)

    bank.mergeAccounts(id1, id2)
    after = bank_state(bank)
    # keep smaller id (id1) and combined balance
    expected = [
        {'id': id1, 'name': 'Sam', 'address': 'Addr', 'ss': 111, 'balance': 100},
    ]
    return print_test_result('merge_accounts', before, after, expected)


def test_merge_banks_no_collision():
    reset_node_state()
    b1 = LinkedList()
    b1.addUser('A', 'x', 1, 10)
    b1.addUser('B', 'y', 2, 20)
    b2 = LinkedList()
    b2.addUser('C', 'z', 3, 30)
    before_b1 = bank_state(b1)
    before_b2 = bank_state(b2)

    merged = LinkedList.mergeBanks(b1, b2)
    after = bank_state(merged)
    # expected is concatenation preserving ids
    expected = before_b1 + before_b2
    return print_test_result('merge_banks_no_collision', {'b1': before_b1, 'b2': before_b2}, after, expected)


def run_all_tests():
    tests = [
        test_add_basic,
        test_delete_and_reuse,
        test_pay_transfer,
        test_get_median_odd_even,
        test_merge_accounts,
        test_merge_banks_no_collision,
    ]
    results = []
    for t in tests:
        try:
            ok = t()
        except Exception as e:
            print('\nTest', t.__name__, 'raised exception:', e)
            ok = False
        results.append((t.__name__, ok))

    print('\nSummary:')
    for name, ok in results:
        print(f'  {name}:', 'PASS' if ok else 'FAIL')


if __name__ == '__main__':
    run_all_tests()
