def test_soft_assertions():
    actual_title = "Gmail"
    expected_title = "Google Chrome"
    assert actual_title == expected_title, "Title is not matching"
    title = "Google Chrome Gmail"
    assert "Gmails" in title, "Gmails is not matching in the title"
    print('Test soft_assertions beginning')
    assert False, "Should not be reached"
    print('Test soft_assertions ending')
