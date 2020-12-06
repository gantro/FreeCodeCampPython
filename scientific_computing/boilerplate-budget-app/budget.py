class Category:

  def __init__(self, name):
    self.name = name
    self.ledger = []

    self.bal = 0
    self.spending = 0

  def __repr__(self):
    budget = '*' * (15 - (len(self.name) // 2)) + self.name
    budget += '*' * (30 - len(budget)) + '\n'
    for i in range(len(self.ledger)):
      tmp = self.ledger[i]['description'] + ' ' * 23
      budget += tmp[:23] + ('%7.2f\n' % self.ledger[i]['amount'])
    return budget + ('Total:%7.2f' % self.bal)

  def deposit(self, val, desc=''):
    self.ledger.append({'amount': val, 'description': desc})
    self.bal += val

  def withdraw(self, val, desc=''):

    if self.check_funds(val):
      self.ledger.append({'amount': -val, 'description': desc})
      self.bal -= val
      self.spending += val
      return True

    else:
      return False

  def get_balance(self):
    return self.bal

  def transfer(self, val, cat):

    if self.check_funds(val):
      self.withdraw(val, 'Transfer to ' + cat.name)
      cat.deposit(val, 'Transfer from ' + self.name)
      return True

    else:
      return False

  def check_funds(self, val):
    return (self.bal >= val)


def create_spend_chart(categories):
  sum_spend = 0
  spend = []

  max_name = 0
  names = []

  for i in range(len(categories)):
    spend.append(categories[i].spending)
    sum_spend += categories[i].spending

    names.append(categories[i].name)

    max_name = max(max_name, len(categories[i].name))

  report = 'Percentage spent by category\n'

  for i in range(100, -1, -10):
    report += ('%3d|' % i)
    for j in range(len(spend)):
      if (spend[j] / sum_spend) * 100.0 >= i:
        report += ' o '
      else:
        report += '   '

    report += ' \n'

  report += '    ' + '---' * len(categories) + '-\n'

  for i in range(max_name):
    report += '    '
    for j in range(len(names)):
      if i < len(names[j]):
        report += ' ' + names[j][i] + ' '
      else:
        report += '   '

    if i == (max_name - 1):
      report += ' '
    else:
      report += ' \n'

  return report