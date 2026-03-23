import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bcrypt running')
@cli.command()
def start(): click.echo('bcrypt started')
if __name__ == '__main__': cli()
