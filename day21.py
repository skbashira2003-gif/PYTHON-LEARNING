
# EXCEPTION HANDLING

# ============================================================
# 1. PROGRAM TERMINATES WITHOUT EXCEPTION HANDLING
# ============================================================

print("----- 1. Program Termination -----")

print('1')
print('2')

# This causes ZeroDivisionError and terminates the program.
# Uncomment to see the error.
# a = 4 / 0

print('3')
print('4')


# ============================================================
# 2. TRY-EXCEPT: HANDLE ERROR AND CONTINUE PROGRAM
# ============================================================

print("\n----- 2. Try-Except -----")

print('1')
print('2')

try:
    a = 4 / 0
except ZeroDivisionError:
    print("Message: Zero Division Error has occurred")

print('3')
print('4')


# ============================================================
# 3. SYNTAX ERROR EXAMPLES
# ============================================================

print("\n----- 3. Syntax Error Examples -----")

# Syntax errors are detected before the program runs.
# try-except cannot normally handle syntax errors in the
# same source code.

# a = (1, 2, 3))       # Unmatched parenthesis
# s = "bashira""       # Unmatched quotes
# 5 = x                # Invalid assignment
# l = [1 2 3]          # Missing comma
# if = 21              # Using keyword as variable
#     b = 20           # Incorrect indentation
# if 10                # Missing colon
#     print(True)

print("Syntax error examples are commented out.")


# ============================================================
# 4. RUNTIME ERROR EXAMPLES
# ============================================================

print("\n----- 4. Runtime Error Examples -----")

print('A')

try:
    print("Examples of runtime errors")

    # Uncomment ONE at a time to test the errors.

    # x = 10 / 0
    # print(y)
    # a = [1, 2, 3]
    # print(a[5])
    # d = {"a": 1}
    # print(d["b"])
    # int("abc")
    # "a" + 10

    import abcdef

except IndexError:
    print("1 - Index Error")

except KeyError as ke:
    print("2 - Key Error:", ke)

except (ValueError, TypeError):
    print("3 - Value Error or Type Error")

except ModuleNotFoundError as e:
    print("4 - Module Not Found Error:", e)

except ZeroDivisionError:
    print("5 - Zero Division Error")

# Catch-all exception
except Exception as e:
    print("6 - Other Exception:", e)

print('B')
print('C')


# ============================================================
# 5. ELSE AND FINALLY - NO ERROR
# ============================================================

print("\n----- 5. Else and Finally - No Error -----")

print('A')

try:
    a = 10 / 4

except IndexError:
    print(1)

except ZeroDivisionError:
    print(2)

else:
    print(3)

finally:
    print(4)

print('B')
print('C')


# ============================================================
# 6. ELSE AND FINALLY - WITH ERROR
# ============================================================

print("\n----- 6. Else and Finally - With Error -----")

print('A')

try:
    a = 10 / 0

except IndexError:
    print(1)

except ZeroDivisionError:
    print(2)

else:
    print(3)

finally:
    print(4)

print('B')
print('C')


# ============================================================
# 7. FINALLY EXECUTES EVEN IF ERROR IS NOT HANDLED
# ============================================================

print("\n----- 7. Finally With Unhandled Error -----")

print('A')

try:
    a = 10 / 0

except IndexError:
    print(1)

except ModuleNotFoundError:
    print(2)

finally:
    print(3)

# The ZeroDivisionError is not handled above.
# So we demonstrate the same concept safely below
# using a catch-all exception.


# ============================================================
# 8. MULTIPLE EXCEPT + ONE ELSE + ONE FINALLY
# ============================================================

print("\n----- 8. Multiple Except, One Else, One Finally -----")

print('A')

try:
    a = 10 / 0

except IndexError:
    print(1)

except ModuleNotFoundError:
    print(2)

except ZeroDivisionError:
    print(3)

else:
    print(4)

finally:
    print(5)
    print(6)
    print(7)

print('B')
print('C')


# ============================================================
# 9. CHILD EXCEPTION BEFORE PARENT EXCEPTION
# ============================================================

print("\n----- 9. Child Exception Before Parent Exception -----")

try:
    10 % 0

except ZeroDivisionError:
    print('Zero Division Error')

except ArithmeticError:
    print('Arithmetic Error')


# ============================================================
# 10. PARENT EXCEPTION FIRST - NOT RECOMMENDED
# ============================================================

print("\n----- 10. Parent Exception First -----")

try:
    10 % 0

except ArithmeticError:
    print('Arithmetic Error')

# This will never be reached for ZeroDivisionError
# because ArithmeticError already catches it.

except ZeroDivisionError:
    print('Zero Division Error')


# ============================================================
# 11. KEYERROR AND EXCEPTION
# ============================================================

print("\n----- 11. KeyError -----")

try:
    a = {1: 'a'}
    print(a[2])

except KeyError:
    print('Key Error')

except Exception:
    print('Exception')


# ============================================================
# 12. EXCEPTION PARENT FIRST
# ============================================================

print("\n----- 12. Exception Parent First -----")

try:
    a = {1: 'a'}
    print(a[2])

except Exception:
    print('Exception')

# KeyError below will not be reached for KeyError
# because Exception already catches it.

except KeyError:
    print('Key Error')


# ============================================================
# 13. USER-DEFINED EXCEPTION - SIMPLE
# ============================================================

print("\n----- 13. Simple User-Defined Exception -----")


class StudentAlreadyExists(Exception):
    pass


try:
    raise StudentAlreadyExists(
        'Student with rollno 23 already exists'
    )

except StudentAlreadyExists as sae:
    print(sae)


# ============================================================
# 14. PARAMETERIZED USER-DEFINED EXCEPTION
# ============================================================

print("\n----- 14. Parameterized User-Defined Exception -----")


class StudentNotFound(Exception):

    def __init__(self, rollno, name):
        self.rollno = rollno
        self.name = name

        super().__init__(
            f'Student rollno: {rollno} with name {name} is not found'
        )


try:
    raise StudentNotFound(1, 'bashira')

except StudentNotFound as snf:
    print(snf)

    # Individual variables
    print("Roll Number:", snf.rollno)
    print("Name:", snf.name)


# ============================================================
# 15. ANOTHER USER-DEFINED EXCEPTION EXAMPLE
# ============================================================

print("\n----- 15. Another UDE Example -----")

try:
    raise StudentNotFound(2, 'narmaja sis')

except StudentNotFound as snf:
    print(snf)
    print("Roll Number:", snf.rollno)
    print("Name:", snf.name)






