
foo='abc'
for i in range(len(foo)):
    print foo[i],'(%d)' % i
squared=[x**2 for x in range(4)]
for i in squared:
    print i

sqdEvens=[x**2 for x in range(8) if not x%2]
for i in sqdEvens:
    print i

#try:
#    filename =raw_input('Enter file name:')
    #    fobj=open(filename,'r')
    #    for eachLine in fobj:
#       print eachLine,fobj.close()
#except IOError, e:
#   print 'file open error:',e



class ClassName(base_class[es]):
    "optional documentation string"
    static_member_declarations
    method_declarations

class FooClass(object):
    """my very first class: FooClass"""
    version=0.1
    def _int_(self,nm='John Doe'):
        """constructor"""
        self.name = nm
        print 'Created a class instance for', nm

        def showname(self):
            """display instance attribute and class name"""
            print ' your name is', self.name
            print 'my name is', self._class_._name_

            def showver(self):
                """display class(static) attribute"""
                print self.version

                def addMe2Me(self, x):
                    """apply + operation to argument"""
                    return x + x

