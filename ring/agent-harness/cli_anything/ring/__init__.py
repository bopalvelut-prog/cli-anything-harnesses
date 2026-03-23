import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ring running')
@cli.command()
def start(): click.echo('ring started')
if __name__ == '__main__': cli()
