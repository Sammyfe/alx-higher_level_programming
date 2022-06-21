#!/usr/bin/python3
def list_division(m_list_1, m_list_2, list_length):
    division = []
    for index in range(list_length):
        result = 0
        try:
            result = m_list_1[index] / m_list_2[index]
        except ZeroDivisionError:
            print('division by 0')
        except TypeError:
            print('wrong type')
        except IndexError:
            print('out of range')
        finally:
            division.append(result)

    return division
