class Super( object ):
   def __init__( self, this, that ):
       self.this = this
       self.that = that

class Sub( Super ):
   def __init__( self, myStuff, *args, **kw ):
       super(Sub, self).__init__( *args, **kw )
       self.myStuff= myStuff
       print(self.myStuff, self.this, self.that)

x= Super( 2.7, 3.1 )
y= Sub( "green", 7, 6 )