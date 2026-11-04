import hw4
from datetime import date
import pandas as pd

#Method 1 

def test_count_simba():
    test_list = ["Simba and Pumba are friends and Simba is crazy"]
    output = hw4.count_simba(test_list)
    expected_output = 2
    assert output == expected_output

#Method 2

def test_get_day_month_year():
    dates = [date(2024, 1, 9), date(2025, 12, 31)]

    result = hw4.get_day_month_year(dates)

    expected = pd.DataFrame(
        [[9, 1, 2024], [31, 12, 2025]], columns=["day", "month", "year"]
    )
    #assert result == expected -- not worked
    pd.testing.assert_frame_equal(result, expected)


#Method 3
def test_compute_distance():
    coordinate_pairs = [((0, 0), (0, 1))]

    result = hw4.compute_distance(coordinate_pairs)

    assert len(result) == 1
    # One degree of longitude at the equator is about 111.2 km.
    assert 111 < result[0] < 112

#Method 4
def test_sum_general_int_list():
    a = [[2], 3, [[1,2],5]]
    expected_sum = 13
    b = hw4.sum_general_int_list(a)
    assert expected_sum == b