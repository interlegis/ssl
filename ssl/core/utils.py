import xlrd

def read_excel(filename:
    book = xlrd.open_workbook(filename)
    sh = book.sheet_by_index(0)
    obras = []

    for i in range(sh.nrows):
        titulo = sh.cell(rowx=i, colx=0).value
        quantidade = sh.cell(rowx=i, colx=1).value

        if titulo:
            obras.append({'titulo': titulo, 'quantidade': int(quantidade)})

    return obras
