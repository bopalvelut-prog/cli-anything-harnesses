import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ballerina running')
@cli.command()
def start(): click.echo('ballerina started')
if __name__ == '__main__': cli()
