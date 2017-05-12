import click

@click.command()

def createuser():
    user = {name:b_no}

    name = raw_input("Please enter your name: ")
        print "you entered", name

    b_no = raw_input("Please enter your bootcamp id: ")
        print "you entered", b_no

    user.update({name:b_no})

    return name


if __name__ == "__main__":
    createuser()