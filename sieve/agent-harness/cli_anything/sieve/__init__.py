import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('sieve running')
@cli.command()
def start(): click.echo('sieve started')
if __name__ == '__main__': cli()
