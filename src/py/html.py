# /* vim: set tabstop=2 softtabstop=2 shiftwidth=2 expandtab : */ 

class d:
  def __init__(i, tag, txt, nl="", kl=None):
    i.tag, i.nl, i.kl, i.txt = tag, nl, kl, txt
  def __repr__(i):
    s=""
    if isinstance(i.txt,(list,tuple)):
      s = ''.join([str(x) for x in i.txt])
    else:
      s = str(i.txt)
    kl = " class=\"%s\"" % i.kl if i.kl else ""
    return "%s<%s%s>%s</%s>" % (
              i.nl,i.tag,kl,s,i.tag)

def dnl(tag,txt,kl=None, ) :  
  return d(tag, txt,kl=kl,nl="\n")

# n different licences
# sidenav
# top nav
# news
# all the following should be sub-classed

def page(t,x  )      : return dnl( "html", [ head(t), 
                                             body(
                                               div(x, "wrapper")) ])
def body(x, kl=None) : return dnl( "body", x,                  kl=kl)     
def head(t, kl=None) : return dnl( "head", title(t),           kl=kl)
def title(x,kl=None) : return dnl( "title",x,                  kl=kl)     
def div(x,  kl=None) : return dnl( "div",  x,                  kl=kl)     
def ul(x,   kl=None) : return d(   "ul",   x,                  kl=kl)     
def i(x,    kl=None) : return d(   "em",   x,                  kl=kl)     
def b(x,    kl=None) : return d(   "b" ,   x,                  kl=kl)     
def p(x,    kl=None) : return dnl( "p" ,   x,                  kl=kl)     
def li(x,   kl=None) : return dnl( "li",   x,                  kl=kl)     
def ol(*l,  kl=None) : return dnl( "ol",   [li(y) for y in l], kl=kl)
def ul(*l,  kl=None) : return dnl( "ul",   [li(y) for y in l], kl=kl)

def uls(*l, kl=None, odd="li0", even="li1"): 
  return ls(*l,what="ul",kl=None,odd=odd,even=even)

def ols(*l, kl=None, odd="li0", even="li1"): 
  return ls(*l,what="ol",kl=None,odd=odd,even=even)

def ls(*l,  what="ul", kl=None, odd="li0", even="li1"):
  oddp=[False]
  def show(x):
    oddp[0] = not oddp[0]
    return dnl("li",  x, kl = odd if oddp[0]  else even)
  return dnl( what, [show(y) for y in l],kl=kl)     

print(page("love",uls("asdas",["sdasas", b("bols")], "dadas","apple", 
          "banana","ws","white",odd="odd", even="even")))

print(b("asdas"))
