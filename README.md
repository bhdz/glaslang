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
        
        my ~ roast: Beef ~ is: ready
        #> my.roast(Beef).is(ready)
        
        hello: ~ take: bag, money ->> Honey <: and buy: some, Bread, Salami 
            -> Maharaji
            
        #> Maharaji.hello().and_buy(Honey.take(bag, money), some, Bread, Salami)
        
    In fact, Glas is hardly a computer language at all. It's more like 
     training wheels for the machine to understand common English language.
     
    The aims of Glas is for the code to be an easy text to read and understand,
    not so much ternseness and speed of writing, although those are some of
    it's features.
     
Examples:

    Person (object):
        __init__: my, name, age, sex =>
            my ~ name = name # or name = name -> my
            my ~ age = age
            my ~ sex = sex
            ... # pass ...
            
            do: "cv" -> my
        
        do: my, action =>
            append: action -> my ~ action list
            ...
            
        done: my, action =>
            if: action ~ in: done list ->> my =>
                {{ "Sorry guy!", "{action} already done" $ 
                    toggle ->> indent: "\t" -> Glas ~ Term }}
                return True
            =>
                return False

        #       
        # optional parameter?
        # optional parameter ?= with optional value besides None
        #
        go: my, place, reason? =>
            ...
        
        get a job: my, company =>
            send: my ~ cv -> to: ->> company
            go: interview -> company
            # ... You Hippie! :-)
            
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
            
            # Warning: extended syntax; if: ... ~ in: ... =>
            if: "name" in ** =>             
                base['name'] = **['name']
                base['age']  = **['age'] 
                # Or use:
                #   key name !! dict
                #   dict ! key name
                
            __init__: **base -> super: Developer, my
        
        slack off: my, game =>
            play: game ?= "Soliataire" -> my
        
        work: my, project =>
            if: project ~ started: == False =>
                slack off: "DooM" -> my
            => # else statement
                my ~ project = project
                asssign: my -> project
                
                do: my ~ project -> my
    #
    # A new quick idea to test out? Or, how to focus Reader's attention on the 
    #  methods inside a Class module?
    #
    make account: my, person(Person), initial amount (Money) =>
        account = Account: person
        my ~ accounts += account
        put: initial amount -> account
    
    -> Bank Clerk (Person):
            __init__: my, department, *, ** =>
                with: my ~ on: department => =
            
    # in other words:
    #  "make a new method in a new class defined by ':' operator"
    
    # ~
    # Your choice of wording:

    open: -> the ~ doors
    the ~ doors ~ open:
    # the.doors.open()
    
    open: -> the doors ~ with: "key"
    the doors ~ open: ~ with: "key"
    # the_doors.open().with("key")
        
    # When you slap object names and existing types together with parenthesis, 
    # you create a new type, for instance:
     
    Mamal (Animal, Lifeform):
    Animal, Lifeform) Mamal:
    (Animal) Mamal (Lifeform):
    German (Dog) Sheppard:
     
    # ... are all the same. 
    
Check out welcome.glas, Genesis.glas in the examples.
You will understand much more about it.

I hope you like it ;-)

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

>:D If you think this might be _a_ .viable: Programming language ->>>

I am _happy_ to tell you that I might work for ...virtual money... {@ comming soon |>> Bitcoin, Dogecoin@} <:D >:D


{> The power is with you %s | Luke <}

{+ output +}

{-- input?no. --}

{@ comment??no.. @}
{$ I _don't_ know: yet $}

dj ->> next: `Song; !and ``Now:spacetime:: date+%s``Timespace::lebowski::timewatch::``!stop;
