def format_prob(val):
  val_arr = val.split(' ')
  max_width = 0

  for i in val_arr:
    if max_width < len(i):
        max_width = len(i)

  max_width += 2

  sol = str(int(val_arr[0]) + int(val_arr[1] + val_arr[2]))

  out = [(' ' * (max_width - len(val_arr[0])) + val_arr[0]),
         (val_arr[1] + ' ' * (max_width - len(val_arr[2]) - 1) + val_arr[2]), 
         ('-' * max_width),
         (' ' * (max_width - len(sol)) + sol)]
  return out

def arithmetic_arranger(problems, solve=False):

  out = ['', '', '', '']

  if len(problems) > 5:
    return 'Error: Too many problems.'

  for i in range(len(problems)):
    if 'x' in problems[i] or '/' in problems[i]:
      return 'Error: Operator must be \'+\' or \'-\'.'

    var = problems[i].lower()
    if var.islower():
      return 'Error: Numbers must only contain digits.'

    var = problems[i].split(' ')
    for j in range(len(var)):
      if len(var[j]) > 4:
        return 'Error: Numbers cannot be more than four digits.'

  for i in range(len(problems)):
    sub_out = format_prob(problems[i])
    out[0] += sub_out[0]
    out[1] += sub_out[1]
    out[2] += sub_out[2]
    out[3] += sub_out[3]

    if i < len(problems) - 1:
      out[0] += '    '
      out[1] += '    '
      out[2] += '    '
      out[3] += '    '

  if solve:
    return out[0] + '\n' + out[1] + '\n' + out[2] + '\n' + out[3]
  else:
    return out[0] + '\n' + out[1] + '\n' + out[2]