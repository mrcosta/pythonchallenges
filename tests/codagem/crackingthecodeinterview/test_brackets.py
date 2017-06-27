from codagem.crackingthecodeinterview.brackets import balance


def test_is_balanced_brackets():
    assert balance("{[]()}") == True
    assert balance("{[}") == False
    assert balance("{[(])}") == False
    assert balance("}][}}(}][))]") == False
    assert balance("[](){()}") == True
    assert balance("()") == True
    assert balance("({}([][]))[]()") == True
    assert balance("{)[](}]}]}))}(())(") == False
