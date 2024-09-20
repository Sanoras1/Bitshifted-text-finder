import base64

#datab64 = "uJRwhbNjBHwWdzPJCABFAAEVIDQAAIARAADAqAG1LNr+ucfxHmYBAe8DE8iHler///9/J5ER/GW+NRSRrGi8/xgrQAAAjn9hfyFAAEBebYGKjxMgUtwBAABAAMD/fydApLgDAE6BSHEfAJz30OI+/38gTagA/P///z+oBAhAAQAAUGRX5kbnEkRHFza25oKURucCEwMAAAAAEMADAABgaOrrhyrsrKfIrsyNziWIji5sbM0FKY3OBSbmCwagCVsMeHYL/ZcItdKBVtT0h2v8mJEwO/xX6ucopm+f+qdfVvakYhkWKHnUe+T5SBJ47PGqZh83BQgAAAAgAAD+B8D7//v///0HAAAAvP///adKnAMGMqK/zFqAIhLAk+wH12Zm5t4B"
#datab64 = datab64.encode("ascii")
#datab64 = "uJRwhbNjBHwWdzPJCABFAAGCIx4AAIARAADAqAG1LNr+ucfxHmYBbu9wE7yQf+3/////4IERksEAA7Sa4CxB16inEPR0xAsSAIBazWY4qL5SAlnrYzKBoD89hYKgRrOZEaqvlEDW+phMQBiADUisNe1cg075TiBvPSYTDWBbZplgEIF+gmAAAABABAAAQI7MDQ5OTpgYzkyNmA2NTA0AAAAAAAAAAAAZ4WDmjEMRyY7G+6CxAgQA4PIY8BgCBADgBWPn9zjTIGz+E5jmxzfLaXSmQdj8J+BMg655UMB5BnHzm8A/UoEOwP///39AKUEAABQAAABFdmVudC5BdHRhY2suSGl0LjAyAAAAAAABPAAAAIamvn6ows56iuzK3OhcgujowsbWXJDS6FxgZL5wAACkw77U5i9+p5MdO+1FnX8stYGIZPi8f/uc3XjjJdZ/rFpLRLHLYIGEZwtA7mwSgSUWuXx1LMaAjMtLAgIA4H/KUpfE///ff4KWl8T7/99/qsQBZKCIBPAk+8G1mZm5Zw=="
#datab64 = datab64.encode("ascii")
#datab64 = "uJRwhbNjBHwWdzPJCABFAAG2IpsAAIARAADAqAG1LNr+ucfxHmYBou+kE2yO/Oz///9/Z4ERkMJ+BDQa4SuCxYmmELRtXZQRAIDajWb5yn6EAR8CPuMogBJHNIWgbeuijAAA1HM0k1n2Iwz4EPAZRwE8xc8UgmquazICAFDN0ky/2VdK4DvAbxwABmADEmtNO9Ogd54SiBHwjEMDzJZZJhhEoJ8gGAAAABABAABgZgNTU1ZGBoMTcwNTYzZzAwAAAAAAAAAAQEYYmBn3UESSx/E2cbQAAQC4LYYshgABAH4AAAAAzkJIp1cE1kSjCrznnIWQTq8IOAmhn34R+Ecq0AH4////Fygo0IkAAAAQgvoiGkJKoxN6w/sSeiPLA3iZtMMNAIACAACgyK7Mjc4liI4ubGzNBSmNzgUmBgAAAAAggAcAAMDQ1NcPVdhZT5FdmRudSxAdXdjYmgtSGp0LTMwXDIBWRQV86GnoL7aOqblzw/gPJniEyQRY+s92+OyRu/Tvr7cP9eiPJCzQh6MWggcBInDYx8BTRYIXkDakFEoAAPxPS58UBgAA/M/TRSmM///7T5U4ZQwUkQCeZO+4NjMz9ww="
#datab64 = "uJRwhbNjBHwWdzPJCABFAAEWb0AAAIARAADAqAG1LNr+ufocHnQBAu8EGjzB0dv/////RdEDhGf+NaSz7Gi8DxrbRAAArkODQyNAAECeNyO1j1P73t3mAfytXP1yQqf2vbvNA07t+3e7B5zad+3mDvwrTYMB/P///z+DBRBAAQAAUGRX5kbnEkRHFza25oKURucCEwMAAAAAEOADAABgaOrrhyrsrKfIrsyNziWIji5sbM0FKY3OBSbmK4YGwJqtEhV1BvmHZnCc73UZ92cgghiC8nT89+KuB79ACv1XLmfqbOAGFPhXRmnAUncXaOKmbtDXdQ0IAAAAIAAA/gfA+//7///9BwAAALz///2nShwVDXqg8MxagHQWwJPsg9tmZubeAQ=="
#datab64 = "uJRwhbNjBHwWdzPJCABFAAEWb3EAAIARAADAqAG1LNr+ufocHnQBAu8EGtjBAtz///9/ztEDiWf+NaSz7Gi8DxrbRAAADkbjRSNAAEBehHOgj1P73t3mAfytXP1yQqf2vbvNA07t23ezB5zaN+3WDvwrTYMB/P///z+DBRBAAQAAUGRX5kbnEkRHFza25oKURucCEwMAAAAAEOADAABgaOrrhyrsrKfIrsyNziWIji5sbM0FKY3OBSbmK4YG4Bs+n0tE7viHJg5NJS6k98clyL1ctXf895dlZZIWB/1XbTXJD8QGFJhYZTg9OncXiP88gv0BcQ0IAAAAIAAA/gfA+//7///9BwAAALz///2nShwcDXpA8cxagHQWwJPsg9tmZubeAQ=="
datab64 = "uJRwhbNjBHwWdzPJCABFAAEWb7EAAIARAADAqAG1LNr+ufocHnQBAu8EGrTCQtz/////YtEDjmf+NaSz7Gi8DxrbRAAAbkhDSCNAAEAe+AzRj1P73t3mAfytXP1yQqf2vbvNA07te3jTB5zad+4mD/wrTYMB/P///z+DBRBAAQAAUGRX5kbnEkRHFza25oKURucCEwMAAAAAEOADAABgaOrrhyrsrKfIrsyNziWIji5sbM0FKY3OBSbmK4YG4ItrQdOROfmHveFZ5iHe9Sey/eMUC27893tmbI5aEP2X/BCSrx8HFLieo4cGiHcXKN1VyLwBgA0IAAAAIAAA/gfA+//7///9BwAAALz///2nSpwlDXrg8cxagHQWwJPsg9tmZubeAQ=="
datab64.encode("ascii")
decoded = base64.b64decode(datab64)

value = int.from_bytes(decoded, byteorder='big')
shifted = (value << 1)


def binary_int_to_utf8(binary_int):
    # Ensure the integer is non-negative
    if binary_int < 0:
        raise ValueError("Negative integers cannot be converted to UTF-8.")

    # Determine the number of bytes needed
    byte_length = (binary_int.bit_length() + 7) // 8 or 1  # At least 1 byte for 0

    # Convert to bytes
    byte_array = binary_int.to_bytes(byte_length, byteorder='big')

    # Decode bytes to UTF-8 string
    utf8_string = byte_array.decode('ascii', errors='replace')

    return utf8_string


for i in range(1, 20):
    try:
        shifted = (value << i)
        print(i)
        myText = binary_int_to_utf8(shifted)
        if 'Event' in myText:
            print(myText)
    except Exception as e: 
        print(e)