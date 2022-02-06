from framework.product import Product
from framework.manager import Manager
from message_box import MessageBox
from under_line_pen import UnderLinePen

def main():
    manager :Manager = Manager()
    upen: UnderLinePen = UnderLinePen('~')
    mbox :MessageBox = MessageBox('*')
    sbox :MessageBox = MessageBox('/')
    manager.register('strong message', upen)
    manager.register('warning box', mbox)
    manager.register('slash box', sbox)

    p1 :Product = manager.create('strong message')
    p1.use('Hello, world.')
    p2 :Product = manager.create('warning box')
    p2.use('Hello, world.')
    p3 :Product = manager.create('slash box')
    p3.use('Hello, world.')

if __name__ == '__main__':
    main()
