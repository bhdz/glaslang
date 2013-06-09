glaslang: The Glas Programming Language
========

Hi.

Glas is a Pythonic Offshot language that got out of hand.

Author: 

    Boril Boyanov <borko.boyanov@gmail.com>

License: 

    BSD4: use it, abuse it (modify it), sell it, keep my name out of it, and 
        don't advertise Glas (that's my job ;))

Motto:
 
    "SYNTAX_ERROR? Mission Impossible!"

Description:

    Glas is a Pythonic Offshot language that got out of hand, with which 
     you can speak like this: 
     
        why: cookie jar ~ empty: -> cookie monster  ~ why: "?"
        #> cookie_monster.why(cookie_jar.empty()).why("?")
        
    In fact, Glas is hardly a computer language at all. It's more like 
     training wheels for the machine to understand common English language.
     
    The aims of Glas is for the code to be an easy text to read and understand,
    not so much ternseness and speed of writing, although those are some of
    the effects of the syntax.
     
Examples:

    Person (object):
        __init__: my, name, age, sex =>
            my ~ name = name
            my ~ age = age
            my ~ sex = sex
            ... # pass ...
            
            work: "cv" -> my
        
        do: my, action =>
            append: action -> my ~ action list
            ...
        
        go: my, place, reason? =>
            ...
        
        get job: my, company =>
            send: my ~ cv -> to: ->> company
            go: interview -> company
            
        work: my =>
            go: my ~ job -> my ~ company
            
        play: my, what =>
            interact: what -> my
    
    #
    # you don't have to inherit like that
    # this is just for showing off multiple inheritance
    #
    Developer (Person, object):     
        __init__: my, company, project, *, ** =>
            with: my ~ on: company, project => =

            base = { "name": "unknown", "age": 0 }
            
            if: "name" in **: # Warning: extended syntax; if: ... ~ in: ... =>
                base ~ name = ** ~ name
                base ~ age  = ** ~ age
                
            __init__: **base -> super: Developer, my
        
        slack off: my, game =>
            play: game?"Soliataire" -> my
        
        work: my, project =>
            if: project ~ started: == False =>
                slack off: "DooM" -> my
            => # else statement
                my ~ project = project
                asssign: my -> project
                
                do:

    # New quick idea?
    make account: my, person(Person), initial amount (Money) =>
        account = Account: person
        my ~ accounts += account
        put: initial amount -> account
    
    -> Bank Clerk (Person):
            __init__: my, department, *, **
            with: my ~ on: department => =
            
    # or Make a new method in a new class defined by \: operator
    
    
Your choice of wording:

    open: -> the ~ doors
    the ~ doors ~ open:
    # the.doors.open()
    
    open: -> the doors ~ with: "key"
    the doors ~ open: ~ with: "key"
    # the_doors.open().with("key")
    
When you slap object names and existing types together with parenthesis, you 
 create a new type:
 
    Mamal (Animal, Lifeform)
    (Animal, Lifeform) Mamal
    (Animal) Mamal (Lifeform)
 
are all the same. 
    
Check out welcome.glas or Genesis.glas in the examples. You will understand much more about it.

I hope you like it.

Enjoy!


~
     
I would be surprised if Glas doesn't become one of the most popular
 languages for teaching. Teach the kid to form sentences in pure 
 English and then simply help him/her with Glasification of the sentence.

Like this:
 "Petar went for a banana, a pear, a big orange, and carried them in a 
  basket home"

Petar went for a banana, a pear, a big orange, 
    and carried them in a basket home
 > ERROR! weak! 
 > F--!
 
Petar ~ went: for a banana, a pear, a big orange, 
    and carried them in a basket home
 > Petar.went(for_a_banana, a_pear, a_big_orange, and_carried_...
 > ERROR! getting better ... 
 > E+ ...

Petar ~ went: for a banana, a pear, a big orange, 
    and: carried them in a basket home
 > Petar.went(for_a_banana, a_pear, a_big_orange, and(carried_...
 > ERROR! Almost there, don't give up ;) 
 > C-!

Petar ~ went: for a banana, a pear, a big orange ~
    and: carried them in a basket home
 > Petar.went(for_a_banana, a_pear, a_big_orange).and(carried_...
 > ERROR! Almost there, you can sense yourself gloating with an 'A' infront 
 >  of your parents. 
 > B-

Petar ~ went: for a banana, a pear, a big orange ~
    and: carried them in a basket home
 > Warning! You did it... just finish it for a perfect score. 
 > A--

Petar ~ went: for a banana, a pear, a big orange ~
    and: ~ carried them: in a basket home
 > BINGO! You've got your A! 
 >  Now go ask your parents for more allowance, or score a FATAL

Petar ~ went: for a banana, a pear, a big orange ~
    and: ~ carried: them, in a basket, home
 > FATALITY! A+! You're a star, and you ROCK!

:-) 

