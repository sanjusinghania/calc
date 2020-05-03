import sys
import math
## Imported math library to run sin(), cos(), tan() and other such functions in the calculator




def calc(term):
    """
        input: term of type str
        output: returns the result of the computed term.
        purpose: This function is the actual calculator and the heart of the application
    """

    # This part is for reading and converting arithmetic terms.
    term = term.replace(' ', '')
    term = term.replace('^', '**')
    term = term.replace('=', '')
    term = term.replace('?', '')
    term = term.replace('%', '/100.00')
    term = term.replace('rad', 'radians')
    term = term.replace('mod', '%')
    term = term.replace('aval', 'abs')

    functions = ['sin', 'cos', 'tan', 'pow', 'cosh', 'sinh', 'tanh', 'sqrt', 'pi', 'radians', 'e']

    # This part is for reading and converting function expressions.
    term = term.lower()

    for func in functions:
        if func in term:
            withmath = 'math.' + func
            term = term.replace(func, withmath)

    try:

        # here goes the actual evaluating.
         term = eval(term)

    # here goes to the error cases.
    except ZeroDivisionError:

        print("Can't divide by 0.  Please try again.")

    except NameError:

        print('Invalid input.  Please try again')

    except AttributeError:

        print('Please check usage method and try again.')
    except TypeError:
        print("please enter inputs of correct datatype ")

    except Exception:
        print("Wrong operator")

    return term


def result(term):
    """
        input:  term of type str
        output: none
        purpose: passes the argument to the function calc(...) and
                prints the result onto console.
    """
    print("\n" + str(calc(term)))


def main():
    """
        main-program
        purpose: handles user input and prints
                 information to the console.
    """


    if sys.version_info.major >= 3:
        while True:
            k = input("\nWhat is ")
            if k == 'quit':
                break
            result(k)

    else:
        while True:
            k = raw_input("\nWhat is ")
            if k == 'quit':
                break
            result(k)


if __name__ == '__main__':
    main()