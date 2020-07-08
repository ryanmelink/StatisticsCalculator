# How to Find a Sample Size Given a Confidence Interval and Width (unknown population standard deviation)

def find_sample_size(p, q, za2, e):
    try:
        p = float(p)
        q = float(q)
        za2 = float(za2)
        e = float(e)

        num1 = p * q
        num2 = za2 / e
        num3 = num2 * num2
        result = int(num1 * num3)
        return result

    except ZeroDivisionError:
        print('Error! Cannot divide by 0')
    except ValueError:
        print('Error! Invalid data entry')
