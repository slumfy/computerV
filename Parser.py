import sys
import re

def ft_return_error(bad_elem, error):
    if error == 1: print("Its not an equation ... (try Ax2 + bX + C = 0 with A,B,C equal to any number)")
    elif error == 2: print("Bad formated element : ", '"',bad_elem[0],'"')
    elif error == 3: print("Equation with more than One \'=\' ? nevermind ")
    elif error == 4: print("Enter at least one character after the \'=\' ?")
    elif error == 5: print(bad_elem[0], " is a bit too much isn\'t it ?")
    sys.exit()

def parsing(splitted):
    if len(splitted) < 2:
        ft_return_error(None, 1)
    if len(splitted) > 2:
        ft_return_error(None, 3)
    if len(splitted[1].strip()) < 1 or len(splitted[0].strip()) < 1:
        ft_return_error(None, 4)
    left = re.split(r"[+-]", splitted[0])
    right = re.split(r"[+-]", splitted[1])
    left = list(map(str.strip, left))
    right = list(map(str.strip, right)) 
    #### Gros parsing avec Regex
    left = ft_parse_token(left)
    right = ft_parse_token(right)
     #### Recuperation des + et -
    sign_left = ft_get_sign(splitted[0], len(left))
    sign_right = ft_get_sign(splitted[1], len(right))
    #### Fusion des signes et des valeurs sous forme [valeur, exposant]
    left = ft_merge_sign(sign_left, left)
    right = ft_merge_sign(sign_right, right)
    #### Récuperation du degré
    degree = ft_get_max_degree([left, right])
    #### Resolution de chaque côtés d'équation
    left = ft_calcul_side(left)
    right = ft_calcul_side(right)
    token = ft_reduced_form(left, right)
    new_degree = ft_get_max_degree([token])
    if new_degree > 3:
        ft_return_error(new_degree.__str__(), 5)
    # print("degre: ", new_degree)
    return(token)

def ft_parse_token(token):
    parsed_token = []
    i = 0
    for tok in token:
        tmp = tok.replace(" ", "")
        if i == 0 and len(tmp) == 0:
            pass
        elif re.match(r'^\d+(?:\.\d+)?\*?[Xx](\^?\d+)?$',tmp): #### cas ou on a un multiplicateur  et X
            split_on_x = tmp.replace("x", "X").split('X')
            multiplicateur = float(re.search(r'\d+(?:\.\d+)?', split_on_x[0])[0])
            exposant_raw = re.search(r'\d+', split_on_x[1])
            exposant = int(exposant_raw[0]) if exposant_raw is not None else 1
            if int(exposant) > 99:
                ft_return_error([str(exposant_raw[0])],5)
            parsed_token.append((multiplicateur, exposant))
            
        elif re.match(r'^\d+(?:\.\d+)?(\*?[xX](\^?\d)?)?$', tmp): #### cas ou on a un multiplicateur
            multiplicateur = float(tmp)
            parsed_token.append((multiplicateur,0))

        elif re.match(r'^[Xx](\^?\d+)?$', tmp): #### cas avec X seul
            exposant_raw = re.search(r'\d+', tmp)
            exposant = int(exposant_raw[0]) if exposant_raw is not None else 1
            if int(exposant) > 99:
                ft_return_error([str(exposant_raw[0])],5)
            parsed_token.append((1.0,exposant))

        else :
            ft_return_error([tmp], 2)
        i +=1
    return parsed_token

def ft_get_max_degree(arrs):
    dmax = 0

    for arr in arrs:
        for item in arr:
            dmax = item[1] if dmax < item[1] and item[0] != 0 else dmax
    return dmax

def ft_get_sign(s, length):
    sign_tab = []
    nb = 0
    for c in s[::-1]:
        if c == '+' or c == '-':
            sign_tab.append(c)
            nb +=1
    if length != nb:
        sign_tab.append('+')
    return sign_tab[::-1]

def ft_merge_sign(sign_tab, side):
    merged = []
    for sign, poly in zip(sign_tab, side):
        merged.append([float(sign + str(poly[0])), poly[1]])
    return merged

def ft_calcul_side(side):
    i = 0
    result = []
    while(i < ft_get_max_degree([side]) + 1):
        val = float(sum([x for x,y in side if y == i]))
        val = [val, i]
        result.append(val)
        i += 1
    return result

def ft_zero_filter(equation):
    for item in equation[1:][::-1]:
        if item[0] == 0: equation.pop()
        else : break
    return equation

def ft_reduced_form(left, right):
    for item in right:
        item[0] *= -1
        left.append(item)
    result = ft_calcul_side(left)
    result = ft_zero_filter(result)
    return result